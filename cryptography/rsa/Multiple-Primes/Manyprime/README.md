# [CryptoHack] ManyPrime

Typically, CTF challenges involve multiple primes, which are usually easy to factor. You just need to factor \(n\) and then calculate \(d\) using the appropriate formulas.

Euler's Totient:
`φ(n) = (p₁ - 1)(p₂ - 1) ... (pₖ - 1)`  

d:
`d ≡ e⁻¹ mod φ(n)`  
