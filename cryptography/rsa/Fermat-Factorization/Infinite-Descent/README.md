# Infinite Descent

This algorithm is vulnerable because it first generates a number \( r \) and then adds random integers to it until it finds a prime number. As a result, the primes \( p \) and \( q \) are both close to \( r \) and to each other. Susceptible to Fermat Factorization attack.
