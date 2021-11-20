from extract import start_ex
from dns_resolve import start_dns
from port_scanning import start_scan_port

tools_name = ['Crack zip', 'Resolve domain names', 'Network scanner']  # name of tools
tools_point = [start_ex, start_dns, start_scan_port]  # function references


def start():
    while True:
        show_menu()
        choice = input('>>> ')
        active_tool(choice)


def show_menu():
    for index, name in enumerate(tools_name, 1):
        print(f'{index}) {name}')
    print('99) Exit')


def active_tool(choice: str):
    if choice == '99':
        print('Buy!')
        exit(0)
    if not choice.isdigit():
        print('[-] You should use number!')
        return
    choice = int(choice)
    if choice <= 0 or choice > len(tools_name):
        print(f'[-] Range from 1 to {len(tools_name)}')
        return

    tools_point[choice - 1]()
