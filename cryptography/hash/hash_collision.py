from pwn import *
import time

m1 = b"4dc968ff0ee35c209572d4777b721587d36fa7b21bdc56b74a3dc0783e7b9518afbfa200a8284bf36e8e4b55b35f427593d849676da0d1555d8360fb5f07fea2"
m2 = b"4dc968ff0ee35c209572d4777b721587d36fa7b21bdc56b74a3dc0783e7b9518afbfa202a8284bf36e8e4b55b35f427593d849676da0d1d55d8360fb5f07fea2"

target = remote("socket.cryptohack.org",13389)
time.sleep(1)

payload = b'{"document":"'+ m1 +b'"}'

target.send(payload)

time.sleep(1)
payload = b'{"document":"'+ m2 +b'"}'

target.send(payload)
target.interactive()