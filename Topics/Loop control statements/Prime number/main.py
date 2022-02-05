from math import sqrt


def is_prime(num):
    if num <= 1:
        return "This number is not prime"

    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return "This number is not prime"
    return "This number is prime"


number = int(input())
print(is_prime(number))
