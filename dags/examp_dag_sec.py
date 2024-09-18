from airflow.decorators import dag, task
from datetime import datetime, timedelta
from airflow.providers.ssh.operators.ssh import SSHOperator
import importlib
# import ssh_connection
# importlib.reload(ssh_connection)
# # from ssh_connection.custom_ssh_hook import customSSHHOOK
# from ssh_connection.custom_ssh_hook import custom_ssh_hook
import os
# from ssh_connection.custom_client import customSSHConnect


# ssh_conn = customSSHConnect().client_conn()

# if ssh_conn: 
#     custom_ssh_hook = customSSHHOOK(ssh_client=ssh_conn)

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
    schedule='@daily',  # Run daily
    catchup=False  # Disable catching up on missed runs
)
def my_dag():

    # Task 1: Simple print statement using Python task
    ssh_task1 = SSHOperator(task_id="ssh_task1", 
                            ssh_conn_id=None, 
                            environment ={'SSH_AUTH_SOCK': os.getenv('SSH_AUTH_SOCK')},
                            command="ls -la")

    # Task 2: Another simple print statement
    ssh_task2 = SSHOperator(task_id = "ssh_task2", 
                            ssh_conn_id=None, 
                            environment ={'SSH_AUTH_SOCK': os.getenv('SSH_AUTH_SOCK')}, 
                         command = 'echo "Task 2 received message"')

    # Task 3: Use Bash command with Bash task decorator
    ssh_task3 = SSHOperator(task_id = "ssh_task3", ssh_conn_id=None, 
                            environment ={'SSH_AUTH_SOCK': os.getenv('SSH_AUTH_SOCK')}, 
                         command="echo 'This is task 3 running a bash command'")

    ssh_task1 >> ssh_task2
    ssh_task3




# Creating an instance of the DAG
dag_instance = my_dag()
