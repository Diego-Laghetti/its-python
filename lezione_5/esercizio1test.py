def prime_factors(n: int) -> list[int]:
    factors = []  
    divisore = 2

    while n > 1:

        if n % 2 == 0:
            factors.append(divisore)
            n //= divisore

        else:
            divisore += 1

    return factors


print(prime_factors(4)) 
print(prime_factors(60))
print(prime_factors(627))
print(prime_factors(4622919))
print(prime_factors(99999999999999999999))

