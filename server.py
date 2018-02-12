# Author: Greg Soares
# Server Class and threading from github.com/Torxed
#!/usr/bin/env python


import time
import timeit
import socket
import threading

#import Queue

# {
#
# L2I = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",range(26)))
# I2L = dict(zip(range(26),"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
# key = 7
#class Low_Level_encrypt():
#    def __init__(self):
#        return encrypt(self.plaintext)
#
#    def encrypt(ptext):
#        binVar_i = ''
#        plaintext = ""
#        plaintext = ptext
#
#        # encipher
#        ciphertext = ""
#        for c in plaintext.upper():
#            if c.isalpha(): ciphertext += I2L[ (L2I[c] + key)%26 ]
#            else: ciphertext += c
#
#        # decipher
#        plaintext2 = ""
#        for c in ciphertext.upper():
#            if c.isalpha(): plaintext2 += I2L[ (L2I[c] - key)%26 ]
#            else: plaintext2 += c
#        print ('Decrypted Ciphertext:')
#        print (plaintext2)
#        ciphertext = list(ciphertext) #Turn string to array of chars
#        #print ciphertext
#        binary_ciphertext = []
#
#        for charToBin in ciphertext: #Char -> Int -> bin: then it to binary_ciphertext and return
#            binVar_i = ord(charToBin) #take the char in the string and turn it to integer
#            binVar = bin(binVar_i) #from integer to binary
#            binVar_i = list(str(binVar))
#            print (binVar_i)
#            if len(binVar_i) <= 8:
#                print ('THIS IS LESS THAN 7 ---  ')
#                print (binVar_i)
#                while len(binVar_i) < 9:
#                    binVar_i.insert(0,0)
#                    print ('\n -- ADDED 0 --')
#                    print (binVar_i)
#            for each in binVar_i: #Takes each binary location and checks that its a number, then adds to the message to be
#                #sent
#                if each == '0' or each == '1':
#                    binary_ciphertext.append(each)
#        print ("\n---ENCRYPTED CIPHER ---\n")
#        print (ciphertext)
#        #print "\n-----------------------"
#        #print ('TESTING binary_ciphertext\n -----------------\n')
#        #print (binary_ciphertext)
#        return (binary_ciphertext)
#        
#
#def Main():
#    host = '172.16.201.109'
#    port = 2041 
#    message = ""
#    encoded = ""
#    plaintext = "Twinkle, twinkle, little star\nHow I wonder what you are\nUp above the world so high\nLike a diamond in the sky\nTwinkle, twinkle little star\nHow I wonder what you are"
#    plaintext = plaintext.upper()
#    # encoded = encrypt(plaintext)
#    #print '\nCiphertext to be Sent:'
#    #for eachElement in message: print eachElement
#
#    #print '\nPrinting each letter as array of chars(casted to byte)'
#    #print encoded
#
## Initiating Socket
#    s = socket.socket()
#    s.connect((host, port))
##----Initiate a loop to encode each char in string and send it    
#    #message = raw_input("-> ")
#
#    i = 0
#    #while i != len(encoded):
#    #    message = encoded[i]
#    #    #print('Sending NOW: %s'%(message))
#    #    s.send('%s'%(message))
#    #    #data = s.recv(1024)
#    #    #print 'Received from server: ' + str(data)
#    ##ser.write('\nTransmitted Ciphertext Message: \n%s'%(encoded))
#    #    i = i + 1
#    #    time.sleep(.1)
#    print("Sending Message")
#    messa = 'asd'
#    s.send('a')
#    data = s.recv(1024)
#    s.close()
#
# }
def Main():
    auth = "pass"
    host = '127.0.0.1'
    port = 5000
    s = socket.socket()
    s.bind((host, port))
    s.listen(0)
    c, addr = s.accept()
    print("Incoming connection from: " + str(addr))

    data = c.recv(10)  # Receive max of 10 bytes
    auth_recv = str(data)
    auth_recv = auth_recv.decode()
    print('Checking: ' + auth_recv)

    if (auth_recv == auth):
        print(auth_recv + ' = greg')
    while data != ('!@'.encode()):  # Exit code
        # Make an is_authorized to check for login again or not
        # ELSE: if is_authorized then just receive message till exit code is given
        c.send(data)  # ack
        data = c.recv(1024)  # Receive max of 10 bytes
        c.send(data)  # ack
        print ("Message: " + data.decode('ascii'))
        if not data:
            break



    c.close()


if __name__ == '__main__':
    Main()


