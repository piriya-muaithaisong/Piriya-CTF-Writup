# Muliple Primes

## Calculating Euler's Totient and d in RSA with Multiple Primes

In RSA, the Euler's Totient function φ(n) and the private key exponent d are calculated based on the prime factors of n. When you have multiple primes, the calculations are adjusted accordingly.

## Steps to Calculate φ(n) and d

1. **Choose Primes**:  
   Select k distinct prime numbers p₁, p₂, ..., pₖ. The modulus n is computed as:  
   `n = p₁ * p₂ * ... * pₖ`

2. **Calculate φ(n)**:  
   The Euler's Totient function for multiple primes is calculated using:  
   `φ(n) = (p₁ - 1)(p₂ - 1) ... (pₖ - 1)`  
   This formula works because each factor contributes to the count of integers that are coprime to n.

3. **Choose Public Exponent e**:  
   Select a public exponent e that is coprime to φ(n). Common choices for e include 3, 17, and 65537.

4. **Calculate the Private Exponent d**:  
   The private exponent d is computed as the modular multiplicative inverse of e modulo φ(n):  
   `d ≡ e⁻¹ mod φ(n)`  
   This means you need to find d such that:  
   `d * e ≡ 1 mod φ(n)`  
   You can use the Extended Euclidean Algorithm to compute d.

## Example

Suppose you have three primes p₁ = 61, p₂ = 53, and p₃ = 47:

1. Calculate n:  
   `n = 61 * 53 * 47 = 161,081`

2. Calculate φ(n):  
   `φ(n) = (61 - 1)(53 - 1)(47 - 1) = 60 * 52 * 46 = 152,520`

3. Choose e (let's say e = 65537) and verify it is coprime to φ(n).

4. Calculate d:  
   Using the Extended Euclidean Algorithm to find d:  
   `d ≡ 65537⁻¹ mod 152520`
