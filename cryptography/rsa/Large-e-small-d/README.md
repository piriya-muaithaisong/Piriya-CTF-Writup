# Large e small d

In RSA, a large public exponent 𝑒 can lead to an unusually small private exponent 𝑑. This situation makes RSA vulnerable to certain attacks, such as the Håstad’s attack or Wiener’s attack.

## Wiener’s Attack

- **Wiener's attack** works when the private exponent d is **less than N^(1/4)**. 
- It exploits the mathematical relationship between e, d, and N using **continued fractions** to approximate:

  `d/e`

- The attacker computes successive continued fractions until the correct d is found, breaking the encryption without needing to factor N.

### Conditions for the Attack:

- **Large e** results in a small d due to the modular inverse relationship.
- **Wiener's attack** becomes possible if:

  `d < (1/3) * N^(1/4)`

Code:
```python
def wiener(e, n):
    # Convert e/n into a continued fraction
    cf = continued_fraction(e/n)
    convergents = cf.convergents()
    for kd in convergents:
        k = kd.numerator()
        d = kd.denominator()
        # Check if k and d meet the requirements
        if k == 0 or d%2 == 0 or e*d % k != 1:
            continue
        phi = (e*d - 1)/k
        # Create the polynomial
        x = PolynomialRing(RationalField(), 'x').gen()
        f = x^2 - (n-phi+1)*x + n
        roots = f.roots()
        # Check if polynomial as two roots
        if len(roots) != 2:
            continue
        # Check if roots of the polynomial are p and q
        p,q = int(roots[0][0]), int(roots[1][0])
        if p*q == n:
            return d
    return None
```


## Boneh-Durfee Attack