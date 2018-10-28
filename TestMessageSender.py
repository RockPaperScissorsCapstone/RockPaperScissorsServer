'''
TestMessageSender.py
Message sender for message passing program between client and sever
Based on: ActiveState Code Recipe 578802 by FB36
Simple script to act as serverto chat between computers in the same network.
Both computers must be running both of these scripts and target ip addresses must be set correctly.
(IP address of a computer can be found using ipconfig command.)
'''
import os
from socket import *
host = "127.0.0.1" # set to IP address of target computer
port = 65432
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
while True:
    data = bytes(input("Enter message to send or type 'exit': "), 'utf-8')
    UDPSock.sendto(data, addr)
    if data == "exit":
        break
UDPSock.close()
os._exit(0)
