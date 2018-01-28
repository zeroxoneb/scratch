#!/usr/bin/env python3

import ipaddress

starting = '192.168.42.0/24'

for net in ipaddress.ip_network(starting).subnets(new_prefix=27):
    print(net)
    for ip in net.hosts():
        print(f'  {ip}')
