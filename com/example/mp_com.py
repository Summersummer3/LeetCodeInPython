# -*- coding: utf-8 -*-
# __author__ = 'summer'

from multiprocessing import Process, Pipe, Value
from os import getpid
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

def cert_key_generate():
    key = RSA.generate(1024)
    private_key = key.export_key()
    public_key = key.publickey().export_key()

    file_pri_key = open("ca_private_key.pem", "wb")
    file_pri_key.write(private_key)
    file_pri_key.close()

    file_pub_key = open("ca_public_key.pem", "wb")
    file_pub_key.write(public_key)
    file_pub_key.close()


def cert_sign(pid):
    key = RSA.generate(1024)
    private_key = key.export_key()
    public_key = key.publickey().export_key()

    file_pri_key = open("%s_private_key.pem" % pid, "wb")
    file_pri_key.write(private_key)
    file_pri_key.close()

    file_pub_key = open("%s_public_key.pem" % pid, "wb")
    file_pub_key.write(public_key)
    file_pub_key.close()

    data = pid + public_key
    sign_key = RSA.import_key(open("ca_private_key.pem", "rb").read())
    h = SHA256.new(data)
    cert = pkcs1_15.new(sign_key).sign(h)

    file_cert = open("%s_cert.pem" % pid, "wb")
    file_cert.write(cert)
    file_cert.close()


def alice(pipe):
    """
    send: enc_ms 
    """
    # sender
    pipe.send("1")
    if pipe.recv() == "1":
        ver_key = RSA.import_key(open("ca_public_key.pem", "rb").read())
        b_public_key = pipe.recv()
        pid = pipe.recv()
        data = pid + b_public_key

        cert = pipe.recv()
        h = SHA256.new(data)
        try:
            pkcs1_15.new(ver_key).verify(h, cert)
            ms = Random.get_random_bytes(16)
            print ms
            key = RSA.import_key(b_public_key)
            cipher_rsa = PKCS1_OAEP.new(key)
            enc_ms = cipher_rsa.encrypt(ms)
            pipe.send(enc_ms)

        except:
            print "vertfication failed"

        # key = Random.get_random_bytes(16)
        # pipe.send("%s" % (getpid()))
        # cipher = AES.new(key, AES.MODE_EAX)
        # ct = cipher.encrypt(data)
        # pipe.send(key)
        # pipe.send(cipher.nonce)
        # pipe.send(ct)

def bob(pipe):

    """
    send:
    1.public_key
    2.pid
    3.cert
    recv:
    shared_key
    """
    pid = str(getpid())
    cert_sign(pid)

    if pipe.recv() == "1":
        pipe.send("1")
        public_key = open("%s_public_key.pem" % pid, "rb").read()
        pipe.send(public_key)
        pipe.send(pid)

        cert = open("%s_cert.pem" % pid, "rb").read()
        pipe.send(cert)
        ciphertext = pipe.recv()
        key = RSA.import_key(open("%s_private_key.pem" % pid, "rb").read())
        cipher_rsa = PKCS1_OAEP.new(key)
        ms = cipher_rsa.decrypt(ciphertext)

        # key = pipe.recv()
        # nonce = pipe.recv()
        # cipher = AES.new(key=key, mode=AES.MODE_EAX, nonce=nonce)
        # ct = pipe.recv()
        # print ct
        # pt = cipher.decrypt(ct)
        # print pt.encode("utf-8")

if __name__ == '__main__':

    cert_key_generate()
    pipe = Pipe()
    plaintext = b"hello, Bob"
    p_1 = Process(target=alice, args=(pipe[1], ))
    p_2 = Process(target=bob, args=(pipe[0], ))

    p_1.start()
    p_2.start()
    p_1.join()
    p_2.join(3)

