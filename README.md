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
