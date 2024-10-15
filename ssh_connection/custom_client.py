import paramiko
import getpass
import paramiko.ssh_exception
from load_env import username, password, pkey_path, hostname
from dotenv import set_key, load_dotenv
import os
from airflow.models import Variable
import time





class customSSHConnect:
    def __init__(self):
        self.rsa_file = pkey_path
        self.username = username
        self.password = password
        self.hostname = hostname
        pass
    
    def TOTP_handler(title, instruction, prompt_list): 
        print("Please provide OTP via Airflow UI in Variable 'otp_input'.")
        totp = Variable.get(f"{instruction
                               }", default_var=None)

        for _ in prompt_list:
            totp_response = totp
        
        while not totp: 
            time.sleep(20)
            totp = Variable.get("totp_input", default_var=None)

        return totp_response
    


    def client_conn(self):
        transport = paramiko.Transport(self.hostname) 
        try: 
            transport.start_client() 
            
            priv_key = paramiko.Ed25519Key.from_private_key_file(self.rsa_file, self.password)
            if not transport.auth_publickey(self.username, priv_key): 
                raise paramiko.ssh_exception.SSHException("Public key/username authentication failed")
            try: 
                transport.auth_interactive_dumb(self.username)
                client = paramiko.SSHClient()
                # invoking client from transport ssh connection 
                client._transport = transport
                
                return client
            except paramiko.ssh_exception.SSHException as e: 
                raise(f"Error initiation ssh connection {e}")
            except paramiko.ssh_exception.AuthenticationException as e: 
                raise(f"Authentication failed: {e}")
            except paramiko.ssh_exception.BadAuthenticationType as e: 
                raise(f"public key not accepeted for user: {e}")
        except paramiko.ssh_exception.SSHException as e: 
            print(f"Error establising ssh connection with csd3")
            return None


# def export_ssh_client(ssh_client): 
#     load_dotenv()
#     try: 
#         print(f"yes ssh client {ssh_client}")
#         if ssh_client and not os.getenv("SSH_CLIENT"): 
#             set_key(dotenv_path="./.env", key_to_set="SSH_CLIENT", value_to_set=ssh_client)
#             print("SSH_CLIENT value successfully set")
#         else: 
#             print("SSH_CLIENT already set")
#     except Exception as e: 
#         print(f"Error saving SSH_CLIENT as env: {e}")
#         return 


if __name__ == "__main__": 
    # delete env varaible SSH_CLIENT if exist in .env file before initiating SSH connection 
    if os.getenv("SSH_CLIENT"): 
        os.environ.pop("SSH_CLIENT")
    
    # initiate SSH connection and return client object 
    conn = customSSHConnect().client_conn()

    # save initiated client object in .env file
    # export_ssh_client(con)

    print(conn.get_params())