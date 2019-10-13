#!/usr/bin/env python3
import os
import csv

with open(os.path.join(os.path.realpath(os.path.dirname(__file__)), 'port_forwards.csv'), 'r') as ports_file:
    output = ""
    port_reader = csv.reader(ports_file)
    for row in port_reader:
        output += "<%s>%s>%s>%s>%s" % (row[0], row[1], row[2], row[3], row[4])

print(output),
