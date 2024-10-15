# Factorize N giving d

This write up is about how to [factorize n giving d](https://www.di-mgt.com.au/rsa_factorize_n.html)

```python
k = d*e -1
x = 0
y = 0

def RSA_dec(p, q):
    print("p = %d, q = %d"%(p,q))
    phi = (p-1)*(q-1)
    d = inverse(new_e, phi)

    pt  = pow(flag,d,N)
    pt = long_to_bytes(pt)
    print(pt)
    exit(0)
    
while True:
    g = randrange(1,N)
    t = k
    while t%2 == 0:
        t = t//2
        x = pow(g,t,N)
        if x > 1:
            y = GCD(x-1,N)
            if y > 1:
                p = y
                q = N//y
                if p*q != N:
                    print("WTF")
                    exit(0)
                RSA_dec(p, q)
```