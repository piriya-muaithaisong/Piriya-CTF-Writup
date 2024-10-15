from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Util.number import *
from hashlib import sha1
import random
import os
from collections import namedtuple
from sage.all import *

Point = namedtuple("Point", "x y")

# check if p ≡ 3(mod4)
p = 173754216895752892448109692432341061254596347285717132408796456167143559
D = 529
G = Point(29394812077144852405795385333766317269085018265469771684226884125940148,
          94108086667844986046802106544375316173742538919949485639896613738390948)
nG = Point(155781055760279718382374741001148850818103179141959728567110540865590463, 73794785561346677848810778233901832813072697504335306937799336126503714)
zero = Point(1,0)
print(p%4 == 3) #True
group_order = p+1
print(group_order) 

factors, exponents = zip(*factor(group_order))
primes = [factors[i] ** exponents[i] for i in range(len(factors))]

    

print(primes)



def point_addition(P, Q):
    Rx = (P.x*Q.x + D*P.y*Q.y) % p
    Ry = (P.x*Q.y + P.y*Q.x) % p
    return Point(Rx, Ry)


def scalar_multiplication(P, n):
    Q = Point(1, 0)
    while n > 0:
        if n % 2 == 1:
            Q = point_addition(Q, P)
        P = point_addition(P, P)
        n = n//2
    return Q


def gen_keypair():
    private = random.randint(1, p-1)
    public = scalar_multiplication(G, private)
    return (public, private)


def gen_shared_secret(P, d):
    return scalar_multiplication(P, d).x


def encrypt_flag(shared_secret: int, flag: bytes):
    # Derive AES key from shared secret
    key = sha1(str(shared_secret).encode('ascii')).digest()[:16]
    # Encrypt flag
    iv = os.urandom(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(flag, 16))
    # Prepare data to send
    data = {}
    data['iv'] = iv.hex()
    data['encrypted_flag'] = ciphertext.hex()
    return data

multiplication_names = ( 'multiplication', 'times', 'product', '*')
addition_names       = ( 'addition', 'plus', 'sum', '+')
def old_discrete_log(a, base, ord=None, operation='*',
                          identity=None, inverse=None, op=None):
     b = base

     from operator import inv, mul, neg, add
     Z = Integers()

     if operation in multiplication_names:
         identity = b.parent()(1)
         inverse  = inv
         op = mul
         if ord==None:
             ord = b.multiplicative_order()
     elif operation in addition_names:
         identity = b.parent()(0)
         inverse  = neg
         op = add
         if ord==None:
             ord = b.order()
     else:
         if ord==None or identity==None or inverse==None or op==None:
             print(ord, identity, inverse, op)

     if ord < 100:
         c = identity
         for i in range(ord):
             if c == a:        # is b^i
                 return Z(i)
             c = op(c,b)

     m = ord.isqrt()+1  # we need sqrt(ord) rounded up
     table = dict()     # will hold pairs (b^j,j) for j in range(m)
     g = identity       # will run through b**j    
     for j in range(m):
         if a==g:
             return Z(j)           
         table[g] = j
         g = op(g,b)

     g = inverse(g)     # this is now b**(-m)
     h = op(a,g)        # will run through a*g**i = a*b**(-i*m)
     for i in range(1,m):
         j = table.get(h)
         if not j==None:  # then a*b**(-i*m) == b**j
             return Z(i*m + j)
         if i < m-1:
             h = op(h,g)
def inverse(A):
    return scalar_multiplication(A,group_order-1) 
        
def pollign_d_log(q,nq): 
    print("dlogging: ", q)
    dlogs = []
    for f in factors[:-1]:
        t = group_order//f
        qt = scalar_multiplication(q,t)
        gent = scalar_multiplication(nq, t)
        dlog = old_discrete_log(qt, gent, ord=f, operation='NONE',
                            op=point_addition, identity=zero, inverse=inverse)
        dlogs.append(dlog)
        print("factor: "+str(f)+", Discrete Log: "+str(dlog))
        if None in dlogs:
            raise ValueError("oh no")
    l = CRT_list(dlogs, factors)
    return l


al = pollign_d_log(G,nG)
print(al)
