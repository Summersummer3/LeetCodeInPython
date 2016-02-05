# -*- coding: utf-8 -*-
# __author__ = 'summer'
dictionary = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


def ceaserEncrypt(i_str, key):
    o_str = ""
    i_str = i_str.lower()
    for i in xrange(len(i_str)):
        if i_str[i] in dictionary:
            index = (dictionary.index(i_str[i]) + key) % 26
            o_str += dictionary[index]
        else:
            o_str += i_str[i]
    return o_str

def encryptFromText(filepath, filename, key=0):
    bufferstr = b''
    with open(filepath + filename, 'rb') as f:
        for line in f.readlines():
            bufferstr += line
    o_str = ceaserEncrypt(bufferstr, key)
    with open(filepath + "encrypted " + filename, 'w') as f_out:
        f_out.writelines(o_str)

encryptFromText("/Users/summer/Documents/", "unEncrypt.txt", 5)