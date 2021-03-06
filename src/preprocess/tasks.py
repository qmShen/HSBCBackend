"""
Tasks for preprocessing
"""

from src.preprocess.weather_data_helper import fetch_and_store_weather_data
from src.utils import Logger, task_thread
import time

CURRENT_INTERVAL = 600
FORECAST_INTERVAL = 3600*12

TOTAL_RUNNING_TIME = 3600*24*7

if __name__ == '__main__':
    tasks = []
    tasks.append(task_thread(fetch_and_store_weather_data, False, CURRENT_INTERVAL, TOTAL_RUNNING_TIME))
    tasks.append(task_thread(fetch_and_store_weather_data, True, FORECAST_INTERVAL, TOTAL_RUNNING_TIME))
    for task in tasks:
        task.start()
    time.sleep(TOTAL_RUNNING_TIME)
    for task in tasks:
        task.join(0.1)

