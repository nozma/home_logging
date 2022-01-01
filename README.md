自宅の環境測定をするアレコレ。

### 必要な機器

- Raspberry Pi
    - Pythonはシステムのものを使ったほうが良い。
- Nature Remo  / Nature Remo E
    - [Nature](https://nature.global/jp/top)
- CO₂モニター CO₂-mini
    - [CO₂モニター CO2-mini | 自然環境測定器 - 製品情報 - 計測器のカスタム](https://www.kk-custom.co.jp/emp/CO2-mini.html)

### 記録するまで

- CO₂センサ
    - [vfilimonov/co2meter: A Python library for USB CO2 meter](https://github.com/vfilimonov/co2meter)を参考にudevの設定をしておく。
    - Raspberry Piにセンサを接続する。先に接続していた場合、物理的に抜き差しする必要がある。
- Nature Remo
    - tokenを取得しておく。
- Spreadsheet
    - [Python Quickstart  |  Sheets API  |  Google Developers](https://developers.google.com/sheets/api/quickstart/python)を参考に設定しておく。
    - `credentials.json`はダウンロードしてこのファイルと同じディレクトリに置いておく。
    - 記録を作成したいSpreadsheetを作成しておく。
    - Spreadsheetには`sensor`と`move`という名前のシートを用意しておく。
    - 実行時は値だけが追記されていくので、1行目にラベルを書いておく。次の順で入ってくるのでよしなに。
        - `sensor`
            1. 時刻
            2. CO₂濃度（ppm）
            3. 気温（℃、CO₂モニターの測定値）
            4. 気温（℃、Nature Remoの測定値）
            5. 相対湿度（%）
            6. 明るさ（Nature Remoの独自の値）
        - `move`
            1. 人感センサー反応時刻
    - 電力消費記録用のSpreadsheetは別にした。
        - `energy`という名前のシートを用意しておく。
        - 値は次の順で記録されていく。
            1. 更新時刻
            2. 積算電力量（kWh）
                - 上限値を上回ったら0に戻るため、消費電力は前回との差分が正か負かで上手く判断する必要がある。
            3. 瞬時電力計測値（W）
        - 参考: [スマートメーターの値から電力データを算出する — Nature Inc](https://developer.nature.global/jp/how-to-calculate-energy-data-from-smart-meter-values)
- 環境変数
    - このディレクトリに`.env`ファイルを作成する。
    - 次の環境変数を用意しておく。
        - `REMO_TOKEN`...Nature RemoのAPIトークン。
        - `SPREADSHEET_ID`...記録を記入したいSpreadsheetのID。URLの中に書いてある。
        - `SPREADSHEET_ID_REMOE`...電力を記録したいSpreadsheetのID。
        - `LINE_NOTIFY_API_TOKEN`...LINE NotifyのAPIトークン。LINEにアラートを飛ばすために使用。
- crontab
    - 次のファイルに実行権限を付けておき、適度に実行する。
        - `log.sh` ... 部屋の環境記録
        - `log_move.sh` ... nature remoの人感センサー記録
        - `line_notify.sh` ... 部屋の環境が良くない場合にLINEに通知する
