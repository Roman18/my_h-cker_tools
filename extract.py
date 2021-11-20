import zipfile
import os


def extract(name: str, passwords: str):
    zFile = zipfile.ZipFile(name)

    with open(passwords, 'r') as f:
        while True:
            password = f.readline().strip()
            if not password:
                print('[-] Password not found')
                break
            try:
                zFile.extractall(pwd=password.encode())
                print(f'[+] Password: {password}')
                break
            except:
                pass


def start_ex():
    while True:
        name = input('Name: ')
        passwords = input('List of passwords: ')
        if os.path.exists(name) and os.path.exists(passwords):
            extract(name, passwords)
            break
        else:
            print('[-] Incorrect path')
