# SSHBuster

SSHBuster is a powerful command-line SSH brute-forcing tool designed for ethical hacking and penetration testing. It performs dictionary-based attacks to find valid SSH login credentials efficiently.

---

## Features

- Brute-force **SSH servers** using different username and password combinations  
- Supports:
  - **Username + password wordlists**
  - **Single username + password wordlist**
  - **Username wordlist + single password**
  - **Single username + single password**
- **Multithreaded** for better speed (**default: 2 threads, max: 5**)
- Stops immediately after finding valid credentials
- Displays **real-time progress**
- Automatically handles **UTF-8** and **Latin-1** encoded wordlists
- Efficient thread management using `ThreadPoolExecutor` and `threading.Event`

---

## ⚠️ Legal Disclaimer

SSHBuster is intended for **educational purposes** and **authorized penetration testing** only.  
**Unauthorized use is illegal.**  
The author is not responsible for misuse or damages caused by this tool.

---

## Requirements

- Python 3.x
- `paramiko` library

Install it with:
```bash
pip3 install paramiko
```

## Installation
1. **Clone the repository** 
```bash
git clone https://github.com/s-r-e-e-r-a-j/SSHBuster.git
```

2. **Navigate to the SSHBuster directory**
```bash
cd SSHBuster
```
3. **Run Installer**
```bash
sudo python3 install.py
```
**then type `y` for install**

3. **Run the tool**

```bash
sshbuster [arguments]
```

## Command-Line Arguments

| Argument / Option         | Description                                       |
|---------------------------|---------------------------------------------------|
| `target_ip`               | Target SSH IP address                             |
| `target_port`             | Target SSH port (usually 22)                      |
| `-u`, `--username`        | Single username                                   |
| `-U`, `--userlist`        | Path to username wordlist                         |
| `-p`, `--password`        | Single password                                   |
| `-P`, `--passlist`        | Path to password wordlist                         |
| `-t`, `--threads`         | Number of threads (default: 2, max allowed: 5)    |

> ⚠️ You must provide **either a single username or a username wordlist**, and likewise **either a single password or a password wordlist**.


## Examples
1. **Brute-force with username and password wordlists**

```bash
sshbuster 192.168.1.100 22 --userlist users.txt --passlist passwords.txt
```
2. **Brute-force with single username and password wordlist**

```bash
sshbuster 192.168.1.100 22 --username root --passlist passwords.txt
```
3. **Brute-force with username wordlist and single password**

```bash
sshbuster 192.168.1.100 22 --userlist users.txt --password 123456
```
4. **Single username and single password**

```bash
sshbuster 192.168.1.100 22 --username admin --password admin123
```
5. **Brute-force using username and password wordlists with 5 threads**
```bash
sshbuster 192.168.1.100 22 --userlist users.txt --passlist passwords.txt --threads 5
```
