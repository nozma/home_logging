# -*- coding:utf-8 -*-
import gsheet

gsheet.write_data(
  values=gsheet.collect_data(), 
  service=gsheet.get_authentication(),
  range='sensor!A1'
)

