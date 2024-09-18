from dotenv import load_dotenv
import os

load_dotenv() # Loading environmental variables from the .env file. 

username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
pkey_path = os.getenv('PKEY_PATH')
hostname = os.getenv('HOSTNAME')