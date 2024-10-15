from airflow.providers.ssh.hooks.ssh import SSHHook
from paramiko.client import SSHClient as SSHClient
from ssh_connection.custom_client import customSSHConnect
from dotenv import load_dotenv
import os

class customSSHHOOK(SSHHook): 
    def __init__(self, ssh_client) -> None:
        self.ssh_client = ssh_client

    def get_conn(self) -> SSHClient:
        return self.ssh_client
    


ssh_conn = customSSHConnect().client_conn()

if ssh_conn: 
    custom_ssh_hook = customSSHHOOK(ssh_client=ssh_conn)
    print(custom_ssh_hook.ssh_client)