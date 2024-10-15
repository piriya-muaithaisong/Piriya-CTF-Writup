from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
from Crypto.Util.number import inverse

p = 9739
a = 497
O = (0,0)

def addition(P,Q) :
    x1,y1 = P
    x2,y2 = Q
    if Q == O:
        return P
    # If Q = O, then P + Q = P
    if P == O:
        return Q

    if x1 == x2 and y1 == -y2:
        return O
    
    if P != Q:
        lam = ((y2 - y1) * inverse(x2 - x1, p)) % p
    # If P = Q: λ = (3 * x1**2 + a) / 2 * y1
    else:
        lam = ((3 * x1**2 + a) * inverse(2 * y1, p)) % p

    # x3 = λ**2 - x1 - x2, y3 = λ *( x1 - x3) - y1
    x3 = (lam**2 - x1 - x2) % p
    y3 = (lam * (x1 - x3) - y1) % p
    return (x3,y3)

def multification(x,n):
    Q=x
    R=(0,0)
    while n > 0:
        if n % 2 == 1 :
            R = addition(R,Q)
        Q = addition(Q,Q)
        n= n//2
    return R


def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')

q_x = 4726
nB = 6534

q_y = (q_x**3 + 497*q_x + 1768) % p #Y^2 = X^3 + 497X + 1768
# there are 2 possible sqrt - both number is okay
q_y1 = pow(q_y,(p+1)//4,p)
q_y2 = -pow(q_y,(p+1)//4,p) % p
print(q_y1)
print(q_y2)
QA = (q_x, q_y2)

shared_secret = multification(QA,nB)[0]
iv = 'cd9da9f1c60925922377ea952afc212c'
ciphertext = 'febcbe3a3414a730b125931dccf912d2239f3e969c4334d95ed0ec86f6449ad8'

print(decrypt_flag(shared_secret, iv, ciphertext))
