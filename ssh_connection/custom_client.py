import paramiko
import getpass
import paramiko.ssh_exception
from load_env import username, password, pkey_path


class customSSHConnect:
    def __init__(self) -> None:
        self.rsa_file = pkey_path
        self.username = username
        self.password = password
        self.hostname = "login-icelake.hpc.cam.ac.uk"

        pass

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
            
    