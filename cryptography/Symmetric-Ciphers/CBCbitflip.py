from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.number import long_to_bytes,bytes_to_long
from time import sleep
import requests
import json
import string 

def split_text_by_len(text, lenght):
    return [ text[i:i+lenght] for i in range(0, len(text), lenght) ]

cookie = "5f082250ace090427aa0633dbf5c8eca8855acfc1f08e9802409016f7b9c5aa9318b9299e30782c41363a52f6e25f30b"

cipher = split_text_by_len(cookie,32)
iv = cipher[0]
block = cipher[1]
#admin=True;
#admin=False
s1 = b"False"
s2 = b"True;"
c1 = bytes.fromhex("90427aa063")

def new_iv(s1,s2,c1):
    iv = b''
    for i in range(len(s1)):
       iv += (s1[i] ^ s2[i] ^ c1[i]).to_bytes()
    return iv


print(new_iv(s1,s2,c1).hex())
print(c1.hex())
print(iv)
print(cipher[1:])



