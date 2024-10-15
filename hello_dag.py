from airflow.decorators import dag
from datetime import datetime, timedelta
from airflow.providers.ssh.operators.ssh import SSHOperator
import os


default_args = {
    'owner': 'khalid',
    'retries': 3,
    'retry_delay': timedelta(seconds=2)
}


@dag(
    dag_id='hello_world_dag_decorator',
    default_args=default_args,
    start_date=datetime(2024, 9, 23),
    schedule='@daily',  # Run daily
    catchup=False  # Disable catching up on missed runs
)
def my_dag():

    # Task 1: Simple print statement using Python task
    ssh_task1 = SSHOperator(task_id="ssh_task1", 
                            ssh_conn_id=None, 
                            environment ={'SSH_AUTH_SOCK': os.getenv('SSH_AUTH_SOCK')},
                            command="echo 'hello world' > /tmp/hello.log && cat /tmp/hello.log", 
                            get_pty=True)


    ssh_task1

my_dag()
