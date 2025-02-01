Make sure you do the following:
On your PC and Router:
1- Making inbound and outbound rules: choose port with specific remote port 2121  [ON WINDOWS FIREWALL ADVANCES SETTINGS]
2- Making passive inbound and outbound rules: choose port with specific remote port 50000-50010 [ON WINDOWS FIREWALL ADVANCES SETTINGS]
3- [Mandatory] Go to your router settings and disable the islolation of SSID from WLAN settings then SSID settings and also disable the isoltaion from Basic WLAN settings. [See pictures attached]
4- [Optional] You can enable the the port trigger application from settings. [See pictures attached]
5- Before using Nexus, run your terminal and install pyftpdlib:
Windows:

          pip install pyftpdlib
          
Linux: 

          pip install pyftpdlib

      or: pipx install pyftpdlib

      or: pip install pyftpdlib --break-system-packages
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
On Termux:
Launch Termux, and ensure it is up to date:

pkg update && pkg upgrade

Install the inetutils package, which includes the FTP client:

pkg install inetutils


Confirm the installation by checking the version:

ftp --version

Enable Storage Access for Termux: Run this command to grant access:

termux-setup-storage

ls

cd [directory]

Important NOTE: USE CD TO NATIGATE INTO THE DIRECTORY YOU NEED TO DOWNLOAD NEEDED FILED FROM FTP SERVER INTO YOUR MOBLIE PHONE.

Run the FTP server script and reconnect using the new port:

ftp [IPV4] 2121

Important Note: It is imortant to run ipconfig, for windows or ifconfig, for linux on the terminal of your PC to know the IPV4 of the PC hosting the FTP server.

Important Note: If the files received using ftp are corrupted, type after connection using ftp the command: bin , it will work correctly after enforcing binary mode in the FTP client, or: install lftp instead.

If you want to:
⦁	Download more files: Use the get <filename> command
⦁	Upload files: Use the put <filename> command
⦁	Navigate through directories: Use cd <directory-name>
⦁	Check your current directory or preview your current path: Use pwd

lftp Commands Guide:
1. Install lftp
To install lftp on Termux, use the following command:

pkg install lftp

2. Connect to the FTP Server
To connect to the FTP server with your credentials (replace <server-ip> with the IP address of your
FTP server):

lftp -u user,1234 ftp://<server-ip>:2121

3. Download Files
To download a file, use the get command:

get filename

4. Upload Files
To upload a file to the server, use the put command:

put localfile

5. Exit the FTP Session
Once done, exit lftp with:

exit

