# CNS Assignment-1
# Written By PURVA GOYDANI
# BT17CSE072

import socket

def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5000  
    server_socket = socket.socket()  # get instance
    print ("Socket successfully created")
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        print("\nMessage from Client: " + str(data))
        data = input('\nType Message for client-> ')
        conn.send(data.encode())  # send data to the client

    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()
