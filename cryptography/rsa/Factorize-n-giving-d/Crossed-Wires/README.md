# [CryptoHack] Crossed-Wired - Intentional Solution

This write up you need to [factorize n giving d](https://www.di-mgt.com.au/rsa_factorize_n.html)

Since

```
cipher ≡ flag^(e₁ ⋅ e₂ ⋅ e₃ ⋅ ... ⋅ eₙ) (mod N)
```

The purpose of this challenge is to factorize 𝑁 into its prime factors 𝑝 and 
𝑞, allowing us to calculate the private key exponent 𝑑 using a new public exponent 𝑒 provided by our friend.