# Source author of ThreardedServer class
#!/usr/bin/env python


import socket
from threading import Thread

max_con = 500
auth = 'pass'
exit_code = '!@'
exit_code = exit_code.encode()


class ThreadedServer(object):
    def __init__(self, host, port):  # host/port = actual parameters at creation time
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen(500)
        while True:
            client, address = self.sock.accept()
            Thread(target = self.listen_to_client, args=(client, address)).start()

#  Handles authentication of the client.
# Instead of being called each time a client attempts
#  to authenticate Communicates with the client directly
    @staticmethod
    def authenticate_client(code, client, address):
        print('Executing authentication for ' + address[0] + ', code: ' + code)
        counter = 0
        client.settimeout(10)
        auth_recv = code
        print(str(address[0]) + '\'s authentication code: ' + auth_recv)
        while True:
            counter = counter+1
            if counter == 3:
                print('Client ' + address[0] + '\'s AUTH ATTEMPT EXCEEDED')
                return False
            try:
                if auth_recv == auth:
                    print(auth_recv + ' successfully authenticated')
                    print('Exit Code: ' + (str(exit_code)))
                    client.send(code.encode())
                    return True
                else:
                    print('Auth failed, waiting for another auth')
                    client.send('ERROR'.encode())
                    auth_recv = client.recv(10)
                    auth_recv = str(auth_recv.decode())
            except socket.timeout:
                print('TIMED OUT')
                return False

    # Receive connection, Authenticate within 10 secs or DROP
    def listen_to_client(self, client, address): # New connection
        print("Incoming connection from: " + str(address[0]) + ':' + str(address[1]))
        data = client.recv(10)  # receive 10-byte authentication code
        auth_recv = str((data.decode()))
        authorized = self.authenticate_client(auth_recv, client, address)
        print('Auth status: ' + str(authorized))
        while True:
            if authorized is False:
                print(str(address[0]) + '\'s Connection timed out/unauthorized')
                break
            else:
                while data != exit_code:  # Exit code
                    try:
                        client.send(data)  # ack
                        data = client.recv(1024)  # Receive max of 10 bytes
                        print(str(address[0]) + " says: " + data.decode())
                        # has been r # Authentication = True, drop connection if no data
                        # has been received for 10 seconds OR exit code is
                        # entered
                        if not data:
                            break
                            authorized = False

                    except socket.timeout:
                        # print('Client: ' + str(address[0]) + '\'s connection Timed out')
                        data = exit_code
                        authorized = False

        client.send(exit_code)
        # Closing thread
        client.close()


if __name__ == "__main__":
    while True:
        port_num = input("Port? ")  # input() returns a string
        try:
            port_num = int(port_num)
            break
        except ValueError:
            pass
    # Instantiates ThreadedServer obj type listen()
    ThreadedServer('127.0.0.1', port_num).listen()
