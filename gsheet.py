# -*- coding:utf-8 -*-
from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pandas as pd
import numpy as np

import remo
import co2

SCOPES = 'https://www.googleapis.com/auth/spreadsheets'

def get_authentication():
  creds = None
  # The file token.pickle stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
      creds = pickle.load(token)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
        'credentials.json', SCOPES)
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.pickle', 'wb') as token:
      pickle.dump(creds, token)

  service = build('sheets', 'v4', credentials=creds)
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
  time = d.index.values[0]
  time = pd.to_datetime(time)
  d2 = remo.get_remo()
  darray = [
    time.strftime('%Y/%m/%d %H:%M:%S'),
    str(d['co2'][0]),
    d['temp'][0],
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