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


# P = (493, 5564)
# Q = (1539, 4742)
# R = (4403,5202)
# S1 = addition(P,P)
# S2 = addition(Q,R)
# S3 = addition(S1,S2)
# print(S3)
# P =(2339, 2213)
# print(multification(P,7863))
QA = (815, 3190)
print(multification(QA,1829))