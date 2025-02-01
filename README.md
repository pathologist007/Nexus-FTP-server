
# FTP Server and Client Setup Guide

## Overview
This guide provides detailed instructions for setting up and configuring an FTP server and client on various platforms, including Windows, Linux, and Termux. It covers necessary firewall configurations, installation of essential software, and commands for both downloading and uploading files via FTP.

## Prerequisites
Before proceeding, ensure you have the following:
- Access to your router settings for network configuration.
- Administrative privileges on your PC (for Windows users).
- Termux installed on your Android device (for mobile access).

## Configuring Your PC and Router

### 1. Configuring Inbound and Outbound Firewall Rules on Windows
- **Inbound Rules:** Set up an inbound rule for FTP traffic on port 2121.
- **Outbound Rules:** Set up an outbound rule for FTP traffic on port 2121.
- **Passive Mode Rules:** Set up inbound and outbound rules for passive FTP mode with ports 50000-50010.

*Note:* To configure these rules, open the Windows Firewall Advanced Settings.

### 2. Disabling SSID Isolation on Your Router
- Access your router settings and disable SSID isolation.
- Navigate to both WLAN Settings and Basic WLAN Settings, and disable isolation if enabled.

### 3. Optional: Enabling Port Triggering
You may choose to enable port triggering from your router settings to enhance FTP performance.

### 4. Installing PyFTPDlib (Python FTP Library)
Before using Nexus, you will need to install pyftpdlib.

- **Windows:**
  ```bash
  pip install pyftpdlib
  ```

- **Linux:**
  Install using either:
  ```bash
  pip install pyftpdlib
  ```
  or:
  ```bash
  pipx install pyftpdlib
  ```

  Alternatively, use the following command if you encounter permission issues:
  ```bash
  pip install pyftpdlib --break-system-packages
  ```

## Setting Up FTP on Termux (Mobile)

### 1. Update Termux and Install Required Packages
Start by updating Termux and installing the necessary FTP tools.
```bash
pkg update && pkg upgrade
pkg install inetutils
```

### 2. Verify FTP Installation
Confirm that the FTP client has been installed correctly by checking its version:
```bash
ftp --version
```

### 3. Grant Storage Access to Termux
Allow Termux to access your device's storage:
```bash
termux-setup-storage
```
Navigate to the directory where you want to download files:
```bash
ls
cd [directory]
```
*Important:* Use `cd` to navigate to the directory where you need to download files from the FTP server to your mobile device.

### 4. Connecting to the FTP Server
Use the following command to connect to the FTP server:
```bash
ftp [IPV4] 2121
```
*Note:* Run `ipconfig` on Windows or `ifconfig` on Linux to determine the IPv4 address of the machine hosting the FTP server.

### 5. Troubleshooting Corrupted Files
If files are corrupted when received via FTP, use the following command to switch to binary mode:
```bash
bin
```

Alternatively, you can install lftp, which is a more robust FTP client:
```bash
pkg install lftp
```

## FTP Command Reference

### Using FTP Commands
Once connected to the FTP server, use the following commands for file management:

- **Download files:**
  ```bash
  get <filename>
  ```

- **Upload files:**
  ```bash
  put <filename>
  ```

- **Navigate directories:**
  ```bash
  cd <directory-name>
  ```

- **Check current directory:**
  ```bash
  pwd
  ```

### Using lftp for Enhanced FTP Functionality

#### 1. Install lftp
To install lftp on Termux, run:
```bash
pkg install lftp
```

#### 2. Connecting to the FTP Server with lftp
Use the following command to connect to the FTP server with your username and password:
```bash
lftp -u user,1234 ftp://<server-ip>:2121
```

#### 3. Downloading Files
To download a file from the server:
```bash
get <filename>
```

#### 4. Uploading Files
To upload a file to the server:
```bash
put <localfile>
```

#### 5. Exiting the FTP Session
To exit the FTP session:
```bash
exit
```

## Conclusion
With this guide, you should now be able to set up and use FTP servers and clients across multiple platforms, ensuring smooth file transfers both locally and remotely. For further assistance or troubleshooting, refer to the respective software documentation.
