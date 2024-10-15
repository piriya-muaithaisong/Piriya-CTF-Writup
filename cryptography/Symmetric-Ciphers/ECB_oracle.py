#flag = 24
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.number import long_to_bytes,bytes_to_long
from time import sleep
import requests
import json
import string

def split_text_by_len(text, lenght):
    return [ text[i:i+lenght] for i in range(0, len(text), lenght) ]

BLOCK_SIZE = 16

flag_size = 26

flag = b""
compare_size = BLOCK_SIZE*2

for i in range(1,flag_size+1):
    for j in string.printable:
       
        
        b1 = b'\x00'*(compare_size-i) + flag + j.encode('ascii')
        b2 = b'\x00'*(compare_size-i)
        #b2 = pad(b''+i.encode('ascii'),block_size=BLOCK_SIZE)
        #b3 = b'\x00'*(33-flag_size)

        #print(b3)
        payload = b1+b2
        payload = payload.hex()

        print(payload)

        r = requests.get("https://aes.cryptohack.org/ecb_oracle/encrypt/" + payload)

        r = json.loads(r.text)["ciphertext"]
        r = split_text_by_len(r,compare_size*2)
        print(r)
        if r[0] == r[1]:
            flag += j.encode('ascii')
            print(flag)
            break

print(flag)