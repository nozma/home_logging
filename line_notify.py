#-*- coding:utf-8 -*-
import requests
import os

headers = {
    'Authorization': 'Bearer ' + os.environ.get('LINE_NOTIFY_API_TOKEN')
}

def send_line_notify(notification_message):
    data = {
        'message': notification_message
    }
    response = requests.post(
        'https://notify-api.line.me/api/notify',
        headers=headers,
        data=data
    )
    print(response)
    print(headers)

