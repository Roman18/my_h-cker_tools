import socket
from threading import *

screenLock = Semaphore(value=1)
closed_ports = 0


def start_scan_port():
    global closed_ports

    str_ip = input('Enter ip or a multiple ip (192.168.1.1,157.172.10.80): ')
    str_port = input('Enter a port or port range (20-100,110,143-443): ')

    try:
        ports = make_port_list(str_port)
        ips = [socket.gethostbyname(ip) for ip in str_ip.split(',')]
    except socket.gaierror:
        print(f'[-] Unknown domain name')
        return
    except:
        print('[-] Incorrect data!')
        return

    socket.setdefaulttimeout(1)
    for ip in ips:
        print(f'_=_=Start scanning host {ip}=_=_\n')
        for port in ports:
            t = Thread(target=scan, args=(ip, int(port)))
            t.start()
            t.join()
        print(f'[!!!] Closed ports -> {closed_ports}\n')
        closed_ports = 0
        print(f'_=_=Stop scanning host {ip}=_=_\n')


def scan(ip: str, port: int):
    sock = None
    global closed_ports
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip, port))
        sock.send(b'hello')  # msg for grabbing banner
        banner = sock.recv(2048)
        screenLock.acquire()
        print(f'[+] Port {port} is open')
        print(f'\t[+] Banner: {str(banner)}\n')
    except:
        screenLock.acquire()
        closed_ports += 1
    finally:
        screenLock.release()
        sock.close()


def make_port_list(str_port: str) -> list:
    list_port = []
    for port in str_port.split(','):
        if '-' in port:
            first, last = port.split('-')
            for p in range(int(first), int(last) + 1):
                list_port.append(p)
        else:
            list_port.append(int(port))
    return list_port
