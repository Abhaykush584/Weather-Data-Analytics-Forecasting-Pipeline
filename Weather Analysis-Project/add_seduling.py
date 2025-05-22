import schedule
import time
from insert_data import insert_data

schedule.every(1).minutes.do(insert_data)

while True:
    schedule.run_pending()
    time.sleep(60)


