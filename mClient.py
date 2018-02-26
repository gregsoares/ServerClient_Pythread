from socket import *
from threading import Thread
from scapy.all import *

data_size = 1020  # number of bytes per transmission being sent
con_num = 10  # number of connections to the host
counter = 1000  # number of messages to send of size: data_size


def m_client(sock, host, port, data):
    sock.connect((host, port))
    sock.send(data)


def data_attack(self):
    pass


def all_in(self):
    pass


if __name__ == "__main__":
#    port = input("Port: ")
#    port = int(port)
    port = 7000
    host = '127.0.0.1'
    # host = (str(input('Host: ')))
    message = 'asdddddd'
    message = message.encode()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    for x in range(10):
        newn = s.dup()
        n = Thread(target=m_client, args=(newn, host, port, message),)
        #ack = s.recv(10)
        #print('Ack received: ' + (str(ack.decode())))

    s.close()
