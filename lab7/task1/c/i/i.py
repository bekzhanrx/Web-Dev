import math

def count_divisors(x):
    divisors = 0
    sqrt_x = int(math.sqrt(x))

    # Перебираем числа от 1 до квадратного корня из x
    for i in range(1, sqrt_x + 1):
        # Если x делится на i без остатка, i - это делитель x
        if x % i == 0:
            divisors += 1

            # Если x / i != i, тогда x / i - это также делитель x
            if i != x / i:
                divisors += 1

    return divisors

x = int(input())
print(count_divisors(x))
