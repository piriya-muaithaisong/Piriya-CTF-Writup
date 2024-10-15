# Simple Encrypt-Decrypt RSA

This write-up shows how RSA encryption and decryption work in textbook RSA. If the **private key** is known.

## 📄 RSA Overview

RSA is based on the mathematical properties of large prime numbers. Below are the key steps and equations involved.

## 🔑 Key Generation

1. **Choose two large prime numbers**:  
   p and q.  
   Compute their product:  
   `n = p × q`

2. **Calculate Euler’s Totient Function**:  
   `φ(n) = (p - 1) × (q - 1)`

3. **Select a public key exponent** e such that:  
   `1 < e < φ(n)` and `gcd(e, φ(n)) = 1`

4. **Compute the private key exponent** d as the modular inverse of e modulo φ(n):  
   `d × e ≡ 1 (mod φ(n))`

The **public key** is **(e, n)** and the **private key** is **(d, n)**.

## 🔒 Encryption

Given a plaintext message M (as an integer), the ciphertext C is computed as:  
`C ≡ M^e (mod n)`

## 🔑 Decryption

To decrypt the ciphertext C, use the private key d:  
`M ≡ C^d (mod n)`

This retrieves the original plaintext message M.