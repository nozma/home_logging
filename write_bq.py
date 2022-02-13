# -*- coding:utf-8 -*-
import gsheet
import os
import csv
from google.cloud import bigquery

client = bigquery.Client()

## 環境計測情報の記録
values = gsheet.collect_data()

table = client.get_table("home_log.room_env")
errors = client.insert_rows(table, [values])

## 最新値をローカルにも保存しておく
#with open('latest_environ_data.csv', 'w') as f:
#    writer = csv.writer(f)
#    writer.writerow(values)

