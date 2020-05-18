# -*- coding:utf-8 -*-
import gsheet
import os

gsheet.write_data(
  spreadsheet_id=os.environ.get('SPREADSHEET_ID'), # 環境計測情報記録用シートID
  values=gsheet.collect_data(), 
  service=gsheet.get_authentication(),
  range='sensor!A1'
)

gsheet.write_data(
  spreadsheet_id=os.environ.get('SPREADSHEET_ID_REMOE'), # 消費電力記録用シートID
  values=gsheet.collect_remoe_data(),
  service=gsheet.get_authentication(),
  range='energy!A1'
)