import random
import binascii

from sqlalchemy import true

def egcd(a, b):
	if a == 0:
		return (b, 0, 1)
	else:
		g, y, x = egcd(b % a, a)
		return (g, x - (b // a) * y, y)

def gcd(a, b): 
	if a == 0: 
		return b 
	return gcd(b % a, a) 


def modinv(a, m):
	g, x, y = egcd(a, m)
	if g != 1:
		raise Exception('modular inverse does not exist')
	else:
		return x % m

# Output:
# Public Key = [7352, 2356, 7579, 19235, 1944, 14029, 1084]
# Private Key = ([184, 332, 713, 1255, 2688, 5243, 10448], 20910)
# Ciphertext = [8436, 22465, 30044, 22465, 51635, 10380, 11879, 50551, 35250, 51223, 14931, 25048, 7352, 50551, 37606, 39550]

W = [184, 332, 713, 1255, 2688, 5243, 10448]
ct = [8436, 22465, 30044, 22465, 51635, 10380, 11879, 50551, 35250, 51223, 14931, 25048, 7352, 50551, 37606, 39550]
q= 20910



for r in range(100,q):
    if gcd(r,q) != 1:
        continue
    r_ = modinv(r, q)


    print("r = ",r)
    #print("r_ = ",r_)
    flag=""
    for c in ct: 
        #c = 52825
        c_ = (c*r_)%q

        #print("C_ = ",c_)
        #while True:
        
        decom_list = []
        for i in range(len(W)-1,-1,-1) :
            if W[i] <= c_:
                newc_ = c_ - W[i]
                #print("%d = %d - %d"%(newc_,c_,W[i]))
                c_ = newc_
                decom_list.append(i+1)

        #print(decom_list)
        sum_char = 0
        for i in decom_list:
            sum_char += 2**(8-(i+1))
        #print(sum_char)
        flag += chr(sum_char)
    
    print(flag[0:4])
    if flag[0:4] == 'ACSC':
        print(r)
        print(flag)
        break

