from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os



'''

{"option":"sign","message":"41414141414141414141414141414141"}
>{"signature": "807738664c37e686e9cd101201cc9f6f"}
{"option":"get_flag","message":"414141414141414141414141414141411010101010101010101010101010101061646d696e3d54727565","signature":"9f2008f76647548ce5cca09d19318ec3"}
>{"flag": "crypto{l3ngth_3xT3nd3r}"}

idea:
1. send message A*16 to the server
2. got a hash
3. use that hash as an initial state and append the word admin=True in to message
'''

admin_true = "61646d696e3d54727565"

def bxor(a, b):
    return bytes(x ^ y for x, y in zip(a, b))


def hash(data):
    data = pad(data, 16)
    out = bytes.fromhex("807738664c37e686e9cd101201cc9f6f") #init
    for i in range(0, len(data), 16):
        blk = data[i:i+16]
        out = bxor(AES.new(blk, AES.MODE_ECB).encrypt(out), out)
    return out

new_message = pad(b'A'*16,16) + b"admin=True"
new_hash = hash(b"admin=True")
print(new_message.hex())
print(new_hash.hex())

'''
{"option":"get_flag","message":"414141414141414141414141414141411010101010101010101010101010101061646d696e3d54727565","signature":"9f2008f76647548ce5cca09d19318ec3"}
'''