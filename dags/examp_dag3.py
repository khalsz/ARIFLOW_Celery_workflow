from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def task1():
    print("This is task 1")

def task2():
    print("This is task 2")

with DAG(
    dag_id='simple_dag',
    start_date=datetime(2023, 1, 1),
    schedule_interval='@daily'  # Run daily
) as dag:

    t1 = PythonOperator(
        task_id='task_1',
        python_callable=task1
    )

    t2 = PythonOperator(
        task_id='task_2',
        python_callable=task2
    )

    t1 >> t2