# if E.order != prime --> it's vulnerable
# tip if you know n you can cut out some factor 
# for example
# 2^2 * 3^7 * 139 * 165229 * 31850531 * 270778799 * 179317983307
# if n is small enough you can cut the last oe off
# or if you know n < something
# you can try multiply every factor until it approach 'something'
# then use only that factor
# for example n < 5
# you can just use factor = 2^2

p = 310717010502520989590157367261876774703
a = 2
b = 3
F = FiniteField(p)
E = EllipticCurve(F,[a,b])


g_x = 179210853392303317793440285562762725654
g_y = 105268671499942631758568591033409611165
G = (g_x,g_y)
nG = (280810182131414898730378982766101210916,291506490768054478159835604632710368904)

P = E.point(G)
Q = E.point(nG)
factors, exponents = zip(*factor(E.order()))
primes = [factors[i] ^ exponents[i] for i in range(len(factors))][:-2]
dlogs = []
for fac in primes:
    t = int(P.order()) / int(fac)
    dlog = discrete_log(t*Q,t*P,operation="+")
    dlogs += [dlog]
    print("factor: "+str(fac)+", Discrete Log: "+str(dlog)) #calculates discrete logarithm for each prime order

l = crt(dlogs,primes)
print(l)
