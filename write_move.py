# -*- coding:utf-8 -*-
import gsheet
import move_sensor as ms
import datetime as dt
import os.path

now = ms.move_sensor_last_update()

if ms.move_updated(now):
  with open('move_last_update', mode = 'w') as f:
    f.write(now)

  now_jst = dt.datetime.strptime(now, '%Y-%m-%dT%H:%M:%SZ') + dt.timedelta(hours=9)

  values = [
    now_jst.strftime('%Y/%m/%d %H:%M:%S')
  ]

  gsheet.write_data(
    spreadsheet_id=os.environ.get('SPREADSHEET_ID'), # 環境計測情報記録用シートID
    values=values, 
    service=gsheet.get_authentication(),
    range='move!A1'
  )
