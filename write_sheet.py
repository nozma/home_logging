# -*- coding:utf-8 -*-
import gsheet
import os
import csv

## 環境計測情報の記録
values = gsheet.collect_data()
gsheet.write_data(
  spreadsheet_id=os.environ.get('SPREADSHEET_ID'), # 環境計測情報記録用シートID
  values=values, 
  service=gsheet.get_authentication(),
  range='sensor!A1'
)
## 最新値をローカルにも保存しておく
with open('latest_environ_data.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(values)


## 消費電力情報の記録
gsheet.write_data(
  spreadsheet_id=os.environ.get('SPREADSHEET_ID_REMOE'), # 消費電力記録用シートID
  values=gsheet.collect_remoe_data(),
  service=gsheet.get_authentication(),
  range='energy!A1'
)