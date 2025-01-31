from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import os
import logging

# Set up logging for debugging
logging.basicConfig(level=logging.DEBUG)

# Prompt the user to input the folder path
ftp_folder = input("Enter the full path to the folder for FTP server access: ")

# Check if the provided path is valid
if not os.path.exists(ftp_folder):
    print("The provided path does not exist. Exiting...")
    exit()

# Set up the authorizer
authorizer = DummyAuthorizer()

# Add user permission (username, password, directory, permission)
# Changed password to '2004' for testing, replace with your desired password
authorizer.add_user("user", "1234", ftp_folder, perm="elradfmw")

# Set up the handler
handler = FTPHandler
handler.authorizer = authorizer

# Set up the FTP server
address = ("0.0.0.0", 2121)  # IP and port for the server
server = FTPServer(address, handler)

# Start the FTP server
print(f"FTP server is running and serving folder: {ftp_folder}")
server.serve_forever()
