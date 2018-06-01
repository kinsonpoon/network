import sys
import socket
import argparse
from binascii import hexlify

def print_machine_info():
    print("Machine info")
    host_name = socket.gethostname()
    print("Host name: %s" %host_name)
    print("IP address: %s" %socket.gethostbyname(host_name))

def get_remote_machine_info():
    remote_host = 'eip.hk.chinamobile.com'
    try:
        print("IP address: %s" %socket.gethostbyname(remote_host))
    except socket.error as serr:
        print("Error message",serr)

def convert_ip4_address():
    for ip_addr in ['127.0.0.1', '192.168.0.1']:
        packed_ip_addr = socket.inet_aton(ip_addr)
        unpacked_ip_addr = socket.inet_ntoa(packed_ip_addr)
        print("IP Address: %s => Packed: %s, Unpacked: %s"\
        %(ip_addr, hexlify(packed_ip_addr), unpacked_ip_addr))

def find_service_name():
    protocolname = 'tcp'
    for port in [80, 25]:
        print("Port: %s => service name: %s" %(port, socket.
        getservbyport(port, protocolname)))
    print("Port: %s => service name: %s" %(53, socket.
    getservbyport(53, 'udp')))

def convert_integer():
    data = 1234
    # 32-bit
    print("Original: %s => Long host byte order: %s, Network byte order: %s"\
    %(data, socket.ntohl(data), socket.htonl(data)))
    # 16-bit
    print("Original: %s => Short host byte order: %s, Network byte order: %s"\
    %(data, socket.ntohs(data), socket.htons(data)))

def test_socket_timeout():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Default socket timeout: %s" %s.gettimeout())
    s.settimeout(100)
    print("Current socket timeout: %s" %s.gettimeout())


#main
convert_ip4_address()