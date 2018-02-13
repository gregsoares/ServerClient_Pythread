#!/usr/bin/env python


import socket
import threading

def Main():
    auth = 'pass'
    host = '127.0.0.1'
    port = 5000
    exit_code = '!@'
    exit_code = exit_code.encode()
    s = socket.socket()
    s.bind((host, port))
    s.listen(0)
    c, addr = s.accept()
    print("Incoming connection from: " + str(addr))

    data = c.recv(10)  # Receive max of 10 bytes
    auth_recv = str((data.decode()))
#    auth_recv = auth_recv.decode()
    print('Checking: ' + auth_recv)
    print(auth + ' is of type ' + str(type(auth)))
    print(auth_recv + ' is of type ' + str(type(auth_recv)))

    if ((str(auth_recv)) == (str(auth))):
        print(auth_recv + ' successfully authenticated')
        print('Exit Code: ' + (str(exit_code)))
        while data != exit_code:  # Exit code
            # Make an is_authorized to check for login again or not
            # ELSE: if is_authorized then just receive message till exit code is given
            c.send(data)  # ack
            data = c.recv(1024)  # Receive max of 10 bytes
            c.send(data)  # ack
            print("Message: " + data.decode())
            if not data:
                break
    else:
        print(auth_recv + ' did not authenticate successfully')

    c.close()


if __name__ == '__main__':
    Main()


