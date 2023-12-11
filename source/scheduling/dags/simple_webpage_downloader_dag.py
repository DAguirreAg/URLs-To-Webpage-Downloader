from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime

import requests

HOSTNAME = "localhost"
PORT = 80

def call_api(url: str):
    response = requests.get(url)
    
    if not (200<=response.status_code<=299):
        raise Exception('Something went wrong.')

def _download_webpages_hourly():
    url = f"http://{HOSTNAME}:{PORT}/download_webpages?frequency=hourly"    
    call_api(url)

def _download_webpages_daily():
    url = f"http://{HOSTNAME}:{PORT}/download_webpages?frequency=daily"    
    call_api(url)

def _download_webpages_weekly():
    url = f"http://{HOSTNAME}:{PORT}/download_webpages?frequency=weekly"    
    call_api(url)

def _download_webpages_monthly():
    url = f"http://{HOSTNAME}:{PORT}/download_webpages?frequency=monthly"    
    call_api(url)

def _download_webpages_yearly():
    url = f"http://{HOSTNAME}:{PORT}/download_webpages?frequency=yearly"    
    call_api(url)

with DAG("simple_webpage_downloader_hourly_dag", # Dag id
    start_date=datetime(2023, 10 ,5), # start date, the 1st of January 2023 
    schedule='@hourly', # Cron expression, here @hourly means once every week.
    catchup=False):

    # Tasks are implemented under the dag object
    download_webpages_hourly = PythonOperator(
        task_id="download_webpages_hourly",
        python_callable=_download_webpages_hourly
    )

    download_webpages_hourly

with DAG("simple_webpage_downloader_daily_dag", # Dag id
    start_date=datetime(2023, 10 ,5), # start date, the 1st of January 2023 
    schedule='@daily', # Cron expression, here @daily means once every day.
    catchup=False):

    # Tasks are implemented under the dag object
    download_webpages_daily = PythonOperator(
        task_id="download_webpages_daily",
        python_callable=_download_webpages_daily
    )

    download_webpages_daily

with DAG("simple_webpage_downloader_weekly_dag", # Dag id
    start_date=datetime(2023, 10 ,5), # start date, the 1st of January 2023 
    schedule='@weekly', # Cron expression, here @weekly means once every week.
    catchup=False):

    # Tasks are implemented under the dag object
    download_webpages_weekly = PythonOperator(
        task_id="download_webpages_weekly",
        python_callable=_download_webpages_weekly
    )

    download_webpages_weekly

with DAG("simple_webpage_downloader_monthly_dag", # Dag id
    start_date=datetime(2023, 10 ,5), # start date, the 1st of January 2023 
    schedule='@monthly', # Cron expression, here @monthly means once every week.
    catchup=False):

    # Tasks are implemented under the dag object
    download_webpages_monthly = PythonOperator(
        task_id="download_webpages_monthly",
        python_callable=_download_webpages_monthly
    )

    download_webpages_monthly

with DAG("simple_webpage_downloader_yearly_dag", # Dag id
    start_date=datetime(2023, 10 ,5), # start date, the 1st of January 2023 
    schedule='@yearly', # Cron expression, here @yearly means once every week.
    catchup=False):

    # Tasks are implemented under the dag object
    download_webpages_yearly = PythonOperator(
        task_id="download_webpages_yearly",
        python_callable=_download_webpages_yearly
    )

    download_webpages_yearly