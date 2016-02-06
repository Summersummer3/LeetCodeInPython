# -*- coding: utf-8 -*-
# __author__ = 'summer'
dictionary = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


def ceaserCipher(i_str, key, mode="encrypt"):
    o_str = ""
    if mode == "decrypt":
        key = 0 - key
    for i in xrange(len(i_str)):
        if i_str[i] in dictionary:
            index = (dictionary.index(i_str[i]) + key) % 26
            o_str += dictionary[index]
        else:
            if i_str[i].isupper():
                index = (dictionary.index(i_str[i].lower()) + key) % 26
                o_str += dictionary[index].upper()
            else:
                o_str += i_str[i]
    return o_str

def encryptFromText(filepath, filename, key=0):
    bufferstr = b''
    with open(filepath + filename, 'rb') as f:
        for line in f.readlines():
            bufferstr += line
    o_str = ceaserCipher(bufferstr, key)
    with open(filepath + "encrypted " + filename, 'w') as f_out:
        f_out.writelines(o_str)

def decryptFromText(filepath, filename, key=0):
    bufferstr = b''
    with open(filepath + filename, 'rb') as f:
        for line in f.readlines():
            bufferstr += line
    o_str = ceaserCipher(bufferstr, key, "decrypt")
    with open(filepath + "decrypted " + filename, 'w') as f_out:
        f_out.writelines(o_str)


decryptFromText("/Users/summer/Documents/", "encrypted unEncrypt.txt", 5)