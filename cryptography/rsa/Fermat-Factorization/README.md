# Fermat's Factorization Method

Fermat's factorization method is an algorithm to factor a composite number `n` into two non-trivial factors. The method is based on the difference of squares and is **particularly effective for numbers that are the product of two close primes (|p-q| is small)**. Here’s how it works step by step:

## Steps for Fermat's Factorization

1. **Choose a Number `n`**:
   - Start with the composite number `n` that you want to factor.

2. **Find the Starting Point**:
   - Compute the ceiling of the square root of `n`:
     ```
     a = ⌈√n⌉
     ```

3. **Calculate `b^2`**:
   - Compute `b^2 = a^2 - n`.
   - If `b^2` is a perfect square, then you can factor `n` as:
     ```
     n = (a - b)(a + b)
     ```
   - If `b^2` is not a perfect square, increase `a` by 1 and repeat this step.

4. **Iterate**:
   - Continue incrementing `a` until `b^2` becomes a perfect square.

5. **Result**:
   - Once you find `b` such that `b^2 = a^2 - n` is a perfect square, you can compute the factors of `n` using:
     ```
     p = a - b
     q = a + b
     ```

## Example

Let's factor `n = 5959`:

1. Compute `a = ⌈√5959⌉ = 78`.
2. Calculate `b^2 = 78^2 - 5959 = 6084 - 5959 = 125` (not a perfect square).
3. Increment `a` to 79:
   - `b^2 = 79^2 - 5959 = 6241 - 5959 = 282` (not a perfect square).
4. Increment `a` to 80:
   - `b^2 = 80^2 - 5959 = 6400 - 5959 = 441` (perfect square, since `441 = 21^2`).
5. Now, factor:
   - `p = 80 - 21 = 59`
   - `q = 80 + 21 = 101`

Thus, `5959 = 59 * 101`.

## Code

```python
def isqrt(n):
	x=n
	y=(x+n//x)//2
	while(y<x):
		x=y
		y=(x+n//x)//2
	return x

def fermat(n):
	t0=isqrt(n)+1
	counter=0
	t=t0+counter
	temp=isqrt((t*t)-n)
	while((temp*temp)!=((t*t)-n)):
		counter+=1
		t=t0+counter
		temp=isqrt((t*t)-n)
	s=temp
	p=t+s
	q=t-s
	return p,q

```