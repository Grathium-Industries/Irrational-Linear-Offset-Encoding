import random

def randomString(limit: int) -> int:
        random.seed(5)

        return random.getrandbits(limit)

# from stack overflow to test if a number is irrational
import collections, fractions
def get_prime_factors(n) -> list:
    #http://stackoverflow.com/a/22808285/5393381
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors  
def hasIrrationalSquareRoot(num) -> bool:
    #http://stackoverflow.com/questions/42302488/identify-a-irrational-or-complex-number
    frac = fractions.Fraction(str(num))
    top_primes = get_prime_factors(frac.numerator)
    bottom_primes = get_prime_factors(frac.denominator)
    all_even_top = all(num % 2 == 0 for num in collections.Counter(top_primes).values())
    all_even_bottom = all(num % 2 == 0 for num in collections.Counter(bottom_primes).values())
    if all_even_top and all_even_bottom:
        return False
    return True
