from socket import *
from threading import Thread


exit_code = '!@'.encode()
t_error = 'ERROR'.encode()
port = input("Port: ")
port = int(port)
message = ''
s = socket()
s.connect(('', port))
code = input('Auth code: ')
code = code.encode()

s.send(code)
ack = s.recv(10)
print('Ack received: ' + (str(ack.decode())))

while (message != exit_code) and (ack != exit_code):
    if(ack != t_error):
        print('Authentication Successful.\n')
        message = (input('Message: ')).encode()
        s.send(message)
        ack = s.recv(1024)
        print('Received: ' + (str(ack.decode())))
    else:
        print('NOT AUTHENTICATED')
        code = (input('Auth code: ')).encode()
        s.send(code)
        ack = s.recv(1024)
        print('Received: ' + (str(ack.decode())))

s.close()
