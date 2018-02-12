#Author: Greg Soares
#!/usr/bin/env python


import time
import timeit
import socket
import threading
#import Queue
      
L2I = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",range(26)))
I2L = dict(zip(range(26),"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

key = 7

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
def Main():
    encoded = ""
    # encoded = encrypt(plaintext)
    #print '\nCiphertext to be Sent:'
    #for eachElement in message: print eachElement

    #print '\nPrinting each letter as array of chars(casted to byte)'
    #print encoded

# Initiating Socket

#----Initiate a loop to encode each char in string and send it    
    #message = raw_input("-> ")

    # i = 0
    # while i != len(encoded):
    #    message = encoded[i]
    #    #print('Sending NOW: %s'%(message))
    #    s.send('%s'%(message))
    #    #data = s.recv(1024)
    #    #print 'Received from server: ' + str(data)
    # ser.write('\nTransmitted Ciphertext Message: \n%s'%(encoded))
    #    i = i + 1
    #    time.sleep(.1)

    host = '127.0.0.1'
    port = 5000
    login = input("Login: ")
    message = input("Message: ")
    s = socket.socket()
    s.connect((host, port))
    print("Sending Message")
    s.send((login.encode()))
    data = s.recv(10)
    if(data == (login.encode())):
        s.send((message.encode()))
        keep_alive = True
        data = s.recv(1024)
        if(data == ( message.encode())):
            while keep_alive:
                new_message = input("Send: ")
                s.send(new_message)
                data = s.recv(1024)
                if (data != new_message):
                    print('\t\t-- Message error -- \n Sent: {} \n Received: {} '.format((str(new_message)), (str(data))))
                    keep_alive = False
                else:
                    pass
    s.close()


if __name__ == '__main__':
    Main()


