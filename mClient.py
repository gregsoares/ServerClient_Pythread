from socket import *
from threading import Thread
import time

data_size = 1020  # number of bytes per transmission being sent
con_num = 10  # number of connections to the host
counter = 1000  # number of messages to send of size: data_size
sleep_time = .2

def m_client(host, port, data):
    print('Executing m_client')
    client = socket()
    client.connect((host, port))
    for i in range(counter):
        client.send(data)
    client.close()
    print(' closing connection with ' + str(host))


def data_attack(self):
    pass


def all_in(self):
    pass


if __name__ == "__main__":
#    port = input("Port: ")
#    port = int(port)
    port = 8000
    host = '127.0.0.1'
    # host = (str(input('Host: ')))
    message = 'asddddddsdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd'
    message = message.encode()
    for x in range(10):
        n = Thread(target=m_client(host, port, message),)
        print('Initiating thread ' + str(x))
        time.sleep(.2)
