from Crypto.Util.number import isPrime, bytes_to_long, long_to_bytes, GCD
import hashlib
from sympy.ntheory import factorint

#Using md5 property if md5(x) == md5(y) then md5(x+z) == md5(y+z)

x = "4dc968ff0ee35c209572d4777b721587d36fa7b21bdc56b74a3dc0783e7b9518afbfa200a8284bf36e8e4b55b35f427593d849676da0d1555d8360fb5f07fea2"
y = "4dc968ff0ee35c209572d4777b721587d36fa7b21bdc56b74a3dc0783e7b9518afbfa202a8284bf36e8e4b55b35f427593d849676da0d1d55d8360fb5f07fea2"

print("x : ", bytes_to_long(bytes.fromhex(x)))

print("md5(x) : ", hashlib.md5(bytes.fromhex(x)).hexdigest())
print("md5(y) : ", hashlib.md5(bytes.fromhex(y)).hexdigest())

z = 1
i = len("crypto{?????????????????????????}")

xx = 0
yy = 0

while True:
    # append 1s till prime
    xx = bytes_to_long(bytes.fromhex(x) + long_to_bytes(z))
    yy = bytes_to_long(bytes.fromhex(y) + long_to_bytes(z))
    if isPrime(xx) and not isPrime(yy):
        while True:
            if isPrime(i):
                a = GCD(i, int(yy))
                if a > 1:
                    break
            i+=1
            
        break
    z += 2

print("x+z :", xx)
print("y+z :", yy)

print("md5(x+z) : ", hashlib.md5(long_to_bytes(xx)).hexdigest())
print("md5(y+z) : ", hashlib.md5(long_to_bytes(yy)).hexdigest())
print("a = ", a)


'''
{"option":"sign","prime":"1042949915673747639548394979539773519387432406920217853474982925582324441002369106807062644005773384014539089496972340217284225886262811961269251256830829063"}
> {"signature": "d12ee089b93e5ca48de83558fa99e31468ea4cc50a6aed176d77d76f63c29901fab2dfb370950dbcc669ee94d4dea970200e6c04c596da2ac40d71eb1fdbe8199bfbb506a275390f85fd606c0d5112329e6df93f4dd80aa07cba94772332dfe1d863b1d87e593ebd18881fc1246670f0dd0dd7662654fedbd3009f7b5d27931f07fd8a172c2f33c5312b644ab8c34b0cbb9a96dfd6ac57dfea89c589d1491186527e77820754814b493950efe8763ca51bf50771607a6f49237fb51c590c2310548806a12e1a2dbfe068d654840944d5589f64004bd614098782b21f91bfd7f8341cf91d5c30d69c18b92bb9ffcb3ae95d41990545413485f029dc78ba0d911a"}
{"option":"check","a":"71","prime":"1042949915673747639548394979539773519387432406920217853474982925582324441002369106807076447498466965142113959008696894268189128104207757197289383619865780743","signature":"d12ee089b93e5ca48de83558fa99e31468ea4cc50a6aed176d77d76f63c29901fab2dfb370950dbcc669ee94d4dea970200e6c04c596da2ac40d71eb1fdbe8199bfbb506a275390f85fd606c0d5112329e6df93f4dd80aa07cba94772332dfe1d863b1d87e593ebd18881fc1246670f0dd0dd7662654fedbd3009f7b5d27931f07fd8a172c2f33c5312b644ab8c34b0cbb9a96dfd6ac57dfea89c589d1491186527e77820754814b493950efe8763ca51bf50771607a6f49237fb51c590c2310548806a12e1a2dbfe068d654840944d5589f64004bd614098782b21f91bfd7f8341cf91d5c30d69c18b92bb9ffcb3ae95d41990545413485f029dc78ba0d911a"}
> {"msg": "Valid signature. First byte of flag: crypto{MD5_5uck5_p4rt_tw0}"}
'''