from Crypto.Util.number import long_to_bytes, inverse
from fractions import Fraction

N = 57003853477618592533708139357440215706141092564456154826439718767682290353899
e = 65537
c = 16088604257693894556768626620517616259596646357071343869173417352209986726562

def continued_fraction_expansion(numerator, denominator):
    while denominator:
        a = numerator // denominator
        yield a
        numerator, denominator = denominator, numerator - a * denominator

def convergents(cf):
    numerators = [0, 1]
    denominators = [1, 0]
    for q in cf:
        numerators.append(q * numerators[-1] + numerators[-2])
        denominators.append(q * denominators[-1] + denominators[-2])
        yield (numerators[-1], denominators[-1])

def wiener_attack(e, N):
    cf = continued_fraction_expansion(e, N)
    for k, d in convergents(cf):
        if k == 0:
            continue
        # Check if d is correct
        if (e * d - 1) % k == 0:
            phi = (e * d - 1) // k
            # Solve for roots of x^2 - (N - phi + 1)x + N = 0
            s = N - phi + 1
            discr = s*s - 4*N
            if discr >= 0:
                t = int(discr**0.5)
                if t*t == discr and (s + t) % 2 == 0:
                    # Found correct d
                    return d
    return None

d = wiener_attack(e, N)
if d is None:
    print("Wiener's attack failed.")
else:
    print(f"Found d = {d}")
    m = pow(c, d, N)
    print("Decrypted message:", long_to_bytes(m).decode())
