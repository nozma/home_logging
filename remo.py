#-*- coding:utf-8 -*-
import requests
import os
import datetime as dt

headers = {
  'accept': 'application/json',
  'Authorization': 'Bearer ' + os.environ.get('REMO_TOKEN')
}

def get_remo():
  response = requests.get(
    'https://api.nature.global/1/devices',
    headers=headers
  )
  data = response.json()
  for i in range(len(data)):
    if(data[i]['name'] == 'remo'):
      d = data[i]
      break

  return(
    {
      'temp_remo': d["newest_events"]["te"]["val"],
      'humidity': d["newest_events"]["hu"]["val"],
      'illumination': d["newest_events"]["il"]["val"],
      'move': d["newest_events"]["mo"]["val"]
    }
  )

def get_remo_e():
  response = requests.get(
    'https://api.nature.global/1/appliances',
    headers=headers
  )
  data = response.json()
  # EPCと計測値を取得
  for i in range(len(data)):
    if(data[i]['device']['name'] == 'Remo E'):
      properties_raw = data[i]['smart_meter']['echonetlite_properties']
      break
  properties = {d.get('epc'): int(d.get('val')) for d in properties_raw}
  # EPCごとにデータを抽出
  normal_direction_cumlative_electric_eneryg = properties[224] # 積算電力量計測値(正方向)
  #reverse_direction_cumlative_electric_energy = properties[227] # 積算電力量計測値(逆方向) （今回は使わない）
  coefficient = properties[211] # 係数
  cumlative_electric_energy_unit = properties[225] # 積算電力量単位
  #cumlative_electric_energy_effective_digits = properties[215] # 積算電力量有効桁数　（今回は使わない）
  measured_instantaneous = properties[231] # 瞬時電力計測値

  # 更新時刻は多分全部一緒だが、念の為瞬間消費電力の値を使う
  for d in properties_raw:
    if d['epc'] == 231:
      updated_at = d['updated_at']
      break

  updated_jst = dt.datetime.strptime(updated_at, '%Y-%m-%dT%H:%M:%SZ') + dt.timedelta(hours=9)
  updated_jst_formatted = updated_jst.strftime('%Y/%m/%d %H:%M:%S')

  # 単位情報に基づいてkWh単位にするための係数を求める（合ってるのか…？）
  if cumlative_electric_energy_unit <= 4:
    unit_coefficient = 1 / (10 ** cumlative_electric_energy_unit)
  else:
    unit_coefficient = 10 ** (cumlative_electric_energy_unit - 9)

  #とりあえず正方向電力値と瞬間電力計測値を返す
  return(
    {
      'updated_at': updated_jst_formatted,
      'normal_direction_cumlative_electric_energy': normal_direction_cumlative_electric_eneryg * coefficient * unit_coefficient,
      'measured_instantaneous': measured_instantaneous
    }
  )


if __name__ == "__main__":
  print(get_remo())
  print(get_remo_e())