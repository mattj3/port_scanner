#!/usr/bin/python3
"""
This script allows multiple hosts and ports to be scanned; fed by a json file.
"""
import socket
import json

# View README.md for config_local example file
config_local = input("Please provide full path to config file (Ex. /Users/yourname/Desktop/filename.json): \n")

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