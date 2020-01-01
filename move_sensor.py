#-*- coding:utf-8 -*-
import requests
import os
import datetime

headers = {
  'accept': 'application/json',
  'Authorization': 'Bearer ' + os.environ.get('REMO_TOKEN')
}

def move_sensor_last_update():
  response = requests.get(
    'https://api.nature.global/1/devices',
    headers=headers
  )
  data = response.json()
  for i in range(len(data)):
    if(data[i]['name'] == 'remo'):
      d = data[i]
      break
  
  return(d['newest_events']['mo']['created_at'])

def move_updated(now):
  if not os.path.isfile('move_last_update'):
    return True
  with open('move_last_update') as f:
    s = f.read()
    if s == now:
      return False
    else:
      return True


if __name__ == '__main__':
  #print(move_sensor_last_update())
  print(move_updated('2019-10-15T10:10:11Z'))
