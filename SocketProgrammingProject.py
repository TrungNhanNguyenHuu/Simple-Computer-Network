# This file is considered as server.py
import socket
import sys

# Create a Socket (connect 2 computers)
def create_socket():
    try:
        global host # IP address
        global port 
        global s    # Socket

        host = ""
        port = 9999
        s = socket.socket()

    except socket.error as msg:
        print("Socket creation error: " + str(msg))


