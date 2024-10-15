# Simple Encrypt-Decrypt RSA

This write up show how RSA encryption and decryption work in text book RSA. If the **private key** is known


## 📄 RSA Overview

RSA is based on the mathematical properties of large prime numbers. Below are the key steps and equations involved.


## 🔑 Key Generation

1. **Choose two large prime numbers**:  
   $\( p \)$ and $\( q \)$.  
   Compute their product:

   \[
   n = p \times q
   \]

2. **Calculate Euler’s Totient Function**:  
   \[
   \phi(n) = (p - 1) \times (q - 1)
   \]

3. **Select a public key exponent** \( e \) such that:  
   \[
   1 < e < \phi(n) \quad \text{and} \quad \gcd(e, \phi(n)) = 1
   \]

4. **Compute the private key exponent** \( d \) as the modular inverse of \( e \) modulo \( \phi(n) \):

   \[
   d \times e \equiv 1 \pmod{\phi(n)}
   \]

The **public key** is \( (e, n) \) and the **private key** is \( (d, n) \).


## 🔒 Encryption

Given a plaintext message \( M \) (as an integer), the ciphertext \( C \) is computed as:

\[
C \equiv M^e \pmod{n}
\]



## 🔑 Decryption

To decrypt the ciphertext \( C \), use the private key \( d \):

\[
M \equiv C^d \pmod{n}
\]

This retrieves the original plaintext message \( M \).

