from Crypto.Cipher import AES
import requests
import json

s = requests.Session()

def decrypt(cipher):
    plain = s.get("https://aes.cryptohack.org/ecbcbcwtf/decrypt/" + cipher).text
    return json.loads(plain)["plaintext"]

def encrypt():
    enc = s.get("https://aes.cryptohack.org/ecbcbcwtf/encrypt_flag/").text
    return json.loads(enc)

def split_text_by_len(text, lenght):
    return [ text[i:i+lenght] for i in range(0, len(text), lenght) ]

def xor_strings(a, b):
    a = bytes.fromhex(a)
    b = bytes.fromhex(b)
    return bytes([a1 ^ b1 for a1, b1 in zip(a, b)]).hex()

enc = encrypt()["ciphertext"]
enc = split_text_by_len(enc,32)
plain = ""

for i in range(len(enc)-1):
    c = enc[i+1]
    iv = enc[i]
    p1 = decrypt(c)
    plain += xor_strings(p1,iv)


print(plain)

