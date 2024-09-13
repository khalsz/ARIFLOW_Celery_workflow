from datetime import datetime, timedelta
from airflow.decorators import dag, task
from airflow import DAG

    
default_args = {
    'owner': 'khalid', 
    'retries': 5, 
    'retry_delay': timedelta(hours=2)
}

@task.bash
def task1(): 
    return "echo 'hello my people'"

@task.bash
def task2(): 
    return "echo 'This is the second message'"

@dag(
    dag_id= "newdagsback", 
    default_args=default_args, 
    start_date=datetime(2024, 9, 12, 2), 
    schedule='@daily'
)
def pipeline(): 
    
    t1 = task1()

    t2 = task2()
    

    t1 >> t2

dag_instance = pipeline()
