#2. Liệt kê các số nguyên tố nhỏ hơn n
import math


def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True


def listPrime(num):
    if num <= 2:
        return []
    else:
        prime = listPrime(num - 1)
        if isPrime(num - 1):
            prime.append(num - 1)
        return prime


num = int(input("Upperbound:"))
print(listPrime(num))
