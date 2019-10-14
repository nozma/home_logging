自宅の環境測定をするアレコレ。

### 必要な機器

- Raspberry Pi
- Nature Remo
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
    - 実行時は値だけが追記されていくので、1行目にラベルを書いておく。次の順で入ってくるのでよしなに。
        1. 時刻
        2. CO₂濃度（ppm）
        3. 気温（℃、CO₂モニターの測定値）
        4. 気温（℃、Nature Remoの測定値）
        5. 相対湿度（%）
        6. 明るさ（Nature Remoの独自の値）
        7. 人感センサ値
- 環境変数
    - このディレクトリに`.env`ファイルを作成する。
    - 次の環境変数を用意しておく。
        - `REMO_TOKEN`...Nature RemoのAPIトークン。
        - `SPREADSHEET_ID`...記録を記入したいSpreadsheetのID。URLの中に書いてある。
- crontab
    - `log.sh`に実行権限をつけておく。
    - `log.sh`を実行する感じで設定しておく。