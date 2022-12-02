#!/usr/bin/python3
"""
This script allows multiple hosts and ports to be scanned.
Fed by a json file.
"""
import socket
import json
import time
from other import extra

e = extra()
user = e[0]
file_name = e[1]
config_local = '/Users/%s/Desktop/%s' % (user, file_name)

with open(config_local) as config_file:
    config = json.load(config_file)

hosts = config["hosts"]
ports = config["ports"]

def port_scanner(ports, hosts):
    for host in hosts:
        for port in ports:
            # AF_INET -> IPV4, SOCK_STREAM -> TCP
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(5)
            # connect.ex returns error code when error occurs
            if s.connect_ex((host, port)):
                print("Port %s is closed on %s" % (port, host))
            else:
                print("Port %s is open on %s" % (port, host))

port_scanner(ports, hosts)