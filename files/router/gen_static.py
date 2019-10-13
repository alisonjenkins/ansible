#!/usr/bin/env python3
import os
import pdb

with open(os.path.join(os.path.realpath(os.path.dirname(__file__)), 'dhcp_static'), 'r') as hosts:
    output = ""
    for line in hosts.readlines():
        mac, ip, name = line.strip().split(' ')
        output += "<%s>%s>%s" % (mac, ip, name)

print(output),
