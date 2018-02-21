# Source author of ThreardedServer class
#!/usr/bin/env python


import socket
import threading

# object --> maybe change to a thread type obj
#class ThreadedServer(object):
#    def __init__(self, host, port):  # host/port = actual parameters at creation time
#        self.host = host
#        self.port = port
#        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#        self.sock.bind((self.host, self.port))
#
#    def listen(self):
#        self.sock.listen(5)
#        while True:
#            client, address = self.sock.accept()
#            client.settimeout(60)
#            threading.Thread(target = self.listenToClient,args = (client,address)).start()
#
#    def listenToClient(self, client, address):
#        size = 1024
#        while True:
#            try:
#                data = client.recv(size)
#                if data:
#                    # Set the response to echo back the received data
#                    response = data
#                    client.send(response)
#                else:
#                    raise NameError('{} - Client disconnected'.format(address))
#            except:
#                client.close()
#                return False
#
#
#if __name__ == "__main__":
#    while True:
#        # port_num = input("Port? ")
#        try:
#            # port_num = int(port_num)  # input() above returns a string
#            port_num = 5000
#            break
#        except ValueError:
#            pass
#
#    ThreadedServer('127.0.0.1', port_num).listen()


#def clientHandler():
#    conn, addr = s.accept()
#    print(addr, "is Connected")
#    while 1:
#        data = conn.recv(1024)
#        if not data:
#            break
#        print("Received Message", repr(data))
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
    # auth_recv = auth_recv.decode()
    print('Checking: ' + auth_recv)
    # Debugging of auth and auth_recv variable types and equivalence
    # print(auth + ' is of type ' + str(type(auth)))
    # print(auth_recv + ' is of type ' + str(type(auth_recv)))

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



