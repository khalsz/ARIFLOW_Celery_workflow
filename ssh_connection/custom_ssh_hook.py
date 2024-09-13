from airflow.providers.ssh.hooks.ssh import SSHHook
from paramiko.client import SSHClient as SSHClient


class customSSHHOOK(SSHHook): 
    def __init__(self, ssh_client) -> None:
        self.ssh_client = ssh_client

    def get_conn(self) -> SSHClient:
        return self.ssh_client