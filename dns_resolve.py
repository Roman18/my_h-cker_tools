import dns
import dns.resolver
import socket
from threading import *

subdomains = [
    'www', 'mail', 'vpn', 'ns', 'dns', 'remote', 'do',
    'server', 'smtp', 'pop', 'imap', 'admin', 'secure',
    'ftp', 'test', 'portal', 'host', 'mx', 'web', 'api',
    'mysql', 'cloud', 'email', 'ir', 'eaf'
]

screenLock = Semaphore(value=1)


def ReverseDNS(ip: str) -> list:
    try:
        # TODO! the function gets too much time
        result = socket.gethostbyaddr(ip)
    except:
        return []
    return [result[0]]


def DNSRequest(name: str):
    try:
        result = dns.resolver.resolve(name, 'A')
        if result:
            screenLock.acquire()
            for answer in result:
                print(f'{name} -> {answer} => Domain name: {ReverseDNS(answer)}')

    except dns.exception.DNSException:
        pass
    screenLock.release()


def start_dns():
    name = input("Enter name: ")
    global subdomains
    for el in subdomains:
        for i in range(0, 10):
            delim = '.' if i == 0 else str(i) + '.'
            t = Thread(target=DNSRequest, args=(el + delim + name,))
            t.start()
            t.join()
