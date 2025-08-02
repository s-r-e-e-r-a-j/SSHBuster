
import os
import sys

if os.geteuid() != 0:
    print("please run as root or with sudo")
    sys.exit(1)
choice = input('[+] to install press (Y) to uninstall press (N) >> ')
run = os.system
if str(choice) =='Y' or str(choice)=='y':

    run('chmod 755 sshbuster.py')
    run('mkdir /usr/share/sshbuster')
    run('cp sshbuster.py /usr/share/sshbuster/sshbuster.py')

    cmnd=(' #! /bin/sh \n exec python3 /usr/share/sshbuster/sshbuster.py "$@"')
    with open('/usr/bin/sshbuster','w')as file:
        file.write(cmnd)
    run('chmod +x /usr/bin/sshbuster & chmod +x /usr/share/sshbuster/sshbuster.py')
    print('''\n\ncongratulation SSHBuster is installed successfully \nfrom now just type \x1b[6;30;42msshbuster\x1b[0m in terminal ''')
if str(choice)=='N' or str(choice)=='n':
    run('rm -r /usr/share/sshbuster ')
    run('rm /usr/bin/sshbuster ')
    print('[!] now SSHBuster has been removed successfully')
