from Crypto.Util.number import long_to_bytes, inverse
import random
import math

N = 57003853477618592533708139357440215706141092564456154826439718767682290353899
e = 65537
c = 16088604257693894556768626620517616259596646357071343869173417352209986726562

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def pollards_rho(n):
    if n % 2 == 0:
        return 2
    x = random.randint(2, n-1)
    y = x
    c = random.randint(1, n-1)
    d = 1
    while d == 1:
        x = (x*x + c) % n
        y = (y*y + c) % n
        y = (y*y + c) % n
        d = gcd(abs(x - y), n)
        if d == n:
            return pollards_rho(n)  # retry with different parameters
    return d

factor = pollards_rho(N)
if factor is None or factor == N:
    print("Failed to factor N with Pollard's Rho.")
else:
    p = factor
    q = N // p
    print(f"Found factors p={p} and q={q}")
    phi = (p - 1)*(q - 1)
    d = inverse(e, phi)
    m = pow(c, d, N)
    print("Decrypted message:", long_to_bytes(m).decode())
