#Author: Greg Soares
#!/usr/bin/env python

import socket
import time
import timeit
import threading


#def clientHandler():
#    conn, addr = s.accept()
#    print(addr, "is Connected")
#
#    while 1:
#        data = conn.recv(1024)
#        if not data:
#            break
#        print("Received Message", repr(data))

def Main():
    exit_code = '!@'
    host = '127.0.0.1'
    port = 5000
    s = socket.socket()
    s.connect((host, port))
    # Initiating connection
    login = input("Login: ")
    message = input("Message: ")
    login = (login.encode())

    print("Sending Login")
    s.send(login)
    data = s.recv(10)
    auth_recv = (str(data))
    login.decode()
    login = (str(login))
    # Debugging messages
    # print('Checking Login')
    # print(auth_recv + ' : ' + login)
    # Add a timer to the if statement to disconnect if no auth received
    if auth_recv == login:  # If we get out auth back then send message
        print('Sending message')  # Let client know we got auth and message is being sent
        message = (message.encode())
        s.send(message)
        # message = message.decode()
        # message = (str(message))
        keep_alive = True
        data = s.recv(1024)
        data = (str(data))
        message = (str(message))
        print('Checking: ' + data + '= ' + message)
        if data == message:

            print(exit_code)
            while keep_alive:
                data = s.recv(1024)
                print(data)
                new_message = (input("Send: ")).encode()
                s.send(new_message)
                data = s.recv(1024)
                data = (str(data))
                new_message = (str(new_message))
                # Debugging messages
                # print(data)
                # print(new_message)
                if new_message == exit_code:  # Check for exit code and close connection
                    print('DISCONNECTING')
                    keep_alive = False

#                if data != new_message:
#                    print('\t\t-- Message error -- \n Sent: {} \n Received: {} '.format(new_message, data))
#                    keep_alive = False

    s.close()


if __name__ == '__main__':
    Main()


