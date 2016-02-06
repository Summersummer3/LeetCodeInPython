# -*- coding: utf-8 -*-
# __author__ = 'summer'
def main():
    myMessage = 'Common sense is not so common.'
    myKey = 8
    ciphertext = encryptMessage(myKey, myMessage) + "|"
    print ciphertext

def encryptMessage(key, message):
    o_arr = []
    for i in xrange(key):
        index = 0 + i
        while index < len(message):
            o_arr.append(message[index])
            index += key
    return "".join(o_arr)

if __name__ == '__main__':
    main()