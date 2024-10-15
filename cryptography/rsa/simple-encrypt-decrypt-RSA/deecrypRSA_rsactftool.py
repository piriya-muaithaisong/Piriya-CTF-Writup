from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import os 
from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes, GCD

with open('/home/kali/Desktop/ctf/tools/RsaCtfTool/tmp/private_chal2.key') as f:
    private_key = RSA.importKey(f.read())
cipher = PKCS1_OAEP.new(private_key)

ct = 0x249d72cd1d287b1a15a3881f2bff5788bc4bf62c789f2df44d88aae805b54c9a94b8944c0ba798f70062b66160fee312b98879f1dd5d17b33095feb3c5830d28
decrypted = cipher.decrypt(long_to_bytes(ct))
print(decrypted)