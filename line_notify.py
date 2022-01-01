#-*- coding:utf-8 -*-
import requests
import os
import csv
import time

last_notified = 'last_notified'
csv_path = 'latest_environ_data.csv'
now = time.time()
headers = {
    'Authorization': 'Bearer ' + os.environ.get('LINE_NOTIFY_API_TOKEN')
}

def send_line_notify(notification_message):
    # 前回通知時刻の取得
    if(os.path.exists(last_notified)):
        with open(last_notified, mode='r') as f:
            s = f.read()
            last_notified_dt = float(s)
    else:
        last_notified_dt = 0.0

    # 通知処理
    if(last_notified_dt + 600 < now): # 前回から10分以上経過していたら通知
        data = {
            'message': notification_message
        }
        response = requests.post(
            'https://notify-api.line.me/api/notify',
            headers=headers,
            data=data
        )
        # 最終通知時刻を記録
        with open(last_notified, mode='w') as f:
            f.write(str(now))
    

## 環境計測情報に応じてメッセージを通知
if(os.path.exists(csv_path)):
    with open(csv_path, 'r') as f:
        reader = csv.reader(f)
        data = reader.__next__()
        co2 = data[1]    # co2センサーのco2
        temp = data[2]   # co2センサーの温度 
        temp_r = data[3] # nature remoの温度
        hum = data[4]    # nature remoの湿度
        il = data[5]     # nature remoの明るさ
    message = ""
    if float(hum) <= 45.0:
        message += "加湿"
    if float(co2) >= 900:
        if len(message) > 0:
            message += "、"
        message += "換気"
    if len(message) > 0:
        message += "をしましょう。\n"
    message += f"現在、温度{round(float(temp), 1)}℃、相対湿度{hum}%、CO₂濃度{co2}ppmです。"
    if float(hum) <= 45.0 or float(co2) >= 900:
        send_line_notify(message)
