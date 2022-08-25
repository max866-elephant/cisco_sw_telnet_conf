# -*- coding:utf-8 -*-

from netmiko import ConnectHandler
cmds = []
ip_lists = []

def main():
    global cmds, ip_lists
    with open('ip_lists.txt','r') as ip_lists_f:
        ip_lists = [line.rstrip() for line in ip_lists_f]
    
    with open('cmds.txt', 'r') as cmds_f:
        cmds = [line.rstrip() for line in cmds_f]  

    for ip in ip_lists:
        cisco_switch = {
            'device_type': 'cisco_ios_telnet',
            'host':   ip,
            'username': 'cisco',
            'password': 'cisco',
        }
        net_connect = ConnectHandler(**cisco_switch)

    
        for cmd in cmds:
            try:
                result = net_connect.send_config_set(cmd)
                print(f'Device {ip} config done!')
            except:
                print(f'Device {ip} config error!')
        # output = net_connect.send_command('show run')    
        # print(output)

if __name__ == '__main__':
    main()