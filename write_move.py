# -*- coding:utf-8 -*-
import gsheet
import move_sensor as ms
import datetime as dt

now = ms.move_sensor_last_update()

if ms.move_updated(now):
  with open('move_last_update', mode = 'w') as f:
    f.write(now)

  now_jst = dt.datetime.strptime(now, '%Y-%m-%dT%H:%M:%SZ') + dt.timedelta(hours=9)

  values = [
    now_jst.strftime('%Y/%m/%d %H:%M:%S')
  ]

  gsheet.write_data(
    values=values, 
    service=gsheet.get_authentication(),
    range='move!A1'
  )
