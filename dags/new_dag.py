# from airflow.decorators import dag, task
from datetime import datetime, timedelta
from celery import Celery
from airflow.operators.python import PythonOperator
from airflow import DAG

# Default arguments for the DAG
default_args = {
    'owner': 'user',  # Replace with your name or identifier
    'retries': 1,  # Number of retries before failing
    'retry_delay': timedelta(seconds=3)  # Delay between retries
}


celery_app = Celery('airflow_sender', broker='amqp://khalid:reg@localhost:5672//')

# Custom function to send tasks to the Celery worker via RabbitMQ
def celery_task_instance(task_id, task_name, command):
    task_data = {
        "task_id": task_id,
        "command": command
    }
    # This will send the task to the corresponding Celery worker
    celery_app.send_task(task_name, args=[task_data])

    # Define the DAG
with DAG(
    dag_id='print_task_dag',  # Name of the DAG
    default_args=default_args,
    start_date=datetime(2024, 9, 1),  # The start date for the DAG
    schedule='@daily',  # DAG will run daily
    catchup=False  # Disables backfilling
) as dag:
    
    task1 = PythonOperator(
        task_id='first_task',
        python_callable=celery_task_instance,
        op_args=[1, 'celery_worker.first_task', 'print("Hello from Airflow!")']  # The task name must match the Celery task.
    )

    task2 = PythonOperator(
        task_id='second_task',
        python_callable=celery_task_instance,
        op_args=[2, 'celery_worker.second_task', 'print("Hello Not from Airflow!")']
    )

    # Set task dependencies
    task1 >> task2

# def print_dag():

#     # Task 1: A simple task to print "Hello from task 1"
#     @task
#     def task1():
#         print("Hello from task 1!")

#     # Task 2: A simple task to print "Hello from task 2"
#     @task
#     def task2():
#         print("Hello from task 2!")

#     # Set the order of tasks: task1 >> task2 (task1 runs before task2)
#     task1() >> task2()

# # Instantiate the DAG
# dag = print_dag()
