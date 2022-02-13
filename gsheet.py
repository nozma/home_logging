# -*- coding:utf-8 -*-
from __future__ import print_function
import pickle
import os.path
import datetime as dt
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build
from google.auth.transport.requests import Request

import remo
import co2

SCOPES = 'https://www.googleapis.com/auth/spreadsheets'

def get_authentication():
  scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
  credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
  service = build('sheets', 'v4', credentials=credentials)
  return service

def write_data(spreadsheet_id, values, service, range):
  body = {
    'values': [values],
  }
  service.spreadsheets().values().append(
    spreadsheetId=spreadsheet_id,
    range=range,
    valueInputOption='USER_ENTERED',
    body=body
  ).execute()

def collect_data():
  d = co2.get_co2()
  d2 = remo.get_remo()
  darray = [
    d[0].strftime('%Y-%m-%d %H:%M:%S'),
    d[1],
    round(d[2], 4),
    d2['temp_remo'],
    d2['humidity'],
    d2['illumination']
  ]
  return(darray)

def collect_remoe_data():
  d = remo.get_remo_e()
  darray = [
    d['updated_at'],
    d['normal_direction_cumlative_electric_energy'],
    d['measured_instantaneous']
  ]
  return(darray)
