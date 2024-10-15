from airflow.decorators import dag, task
from datetime import datetime, timedelta
# from airflow.providers.ssh.operators.ssh import SSHOperator
# import os



default_args = {
    'owner': 'khalid',
    'retries': 3,
    'retry_delay': timedelta(seconds=3)
}


@dag(
    dag_id="pythonDag", 
    default_args=default_args, 
    start_date=datetime(2024, 9, 23),
    schedule='@daily'
)
def my_dags(): 

    @task
    def printing1(): 
        print("hello guy")

    printing1() 


my_d = my_dags()






