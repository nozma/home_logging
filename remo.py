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
  d = response.json()
  return(
    {
      'temp_remo': d[0]["newest_events"]["te"]["val"],
      'humidity': d[0]["newest_events"]["hu"]["val"],
      'illumination': d[0]["newest_events"]["il"]["val"],
      'move': d[0]["newest_events"]["mo"]["val"]
    }
  )


if __name__ == "__main__":
  print(get_remo())