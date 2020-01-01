#-*- coding:utf-8 -*-
import requests
import os

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


if __name__ == "__main__":
  print(get_remo())