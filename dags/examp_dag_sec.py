from airflow.decorators import dag, task
from datetime import datetime, timedelta

# Default arguments for the DAG
default_args = {
    'owner': 'khalid',
    'retries': 3,
    'retry_delay': timedelta(minutes=5)
}

# Defining the DAG with the @dag decorator
@dag(
    dag_id='example_dag_decorator',
    default_args=default_args,
    start_date=datetime(2024, 9, 1),
    schedule_interval='@daily',  # Run daily
    catchup=False  # Disable catching up on missed runs
)
def my_dag():

    # Task 1: Simple print statement using Python task
    @task
    def task_1():
        print("Hello, this is task 1")
        return "task_1 complete"

    # Task 2: Another simple print statement
    @task
    def task_2(message: str):
        print(f"Task 2 received message: {message}")
        return "task_2 complete"

    # Task 3: Use Bash command with Bash task decorator
    @task.bash
    def task_3():
        return "echo 'This is task 3 running a bash command'"

    # Defining the task pipeline
    t1_result = task_1()
    t2_result = task_2(t1_result)  # task_2 depends on the result of task_1
    task_3()  # task_3 runs independently

# Creating an instance of the DAG
dag_instance = my_dag()
