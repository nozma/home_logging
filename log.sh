cd /home/pi/home_logging
PATH=/usr/local/bin:$PATH
pipenv run python write_sheet.py
pipenv run python write_bq.py
