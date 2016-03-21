# -*- coding: utf-8 -*-
# __author__ = 'summer'
def main():
    myMessage = 'We shade in the two boxes in the last row to remind us to ignore them.'
    myKey = 8
    ciphertext = encryptMessage(myKey, myMessage)
    print ciphertext
    print decryptMessage(myKey, ciphertext)

def encryptMessage(key, message):
    o_arr = []
    for i in xrange(key):
        index = 0 + i
        while index < len(message):
            o_arr.append(message[index])
            index += key
    return "".join(o_arr)

def decryptMessage(key, message):
    o_arr = []
    row = len(message) / key + 1
    last_row = len(message) % key
    if last_row == 0:
        last_row = key
    for i in xrange(row):
        index = 0 + i
        flag = 0
        isLastRow = False
        if index == row - 1:
            isLastRow = True
        while index < len(message):
            flag += 1
            if isLastRow and flag > last_row:
                break
            o_arr.append(message[index])
            if flag <= last_row:
                index += row
            else:
                index += (row - 1)
    return "".join(o_arr)

if __name__ == '__main__':
    main()
