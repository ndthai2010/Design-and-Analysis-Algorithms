# 3. Liệt kê n số nguyên tố đầu tiên
import math


def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True


def listNPrimes(num, firstPrime=2, prime=[]):
    if len(prime) == num:
        return prime
    else:
        if isPrime(firstPrime):
            prime.append(firstPrime)
        return listNPrimes(num, firstPrime + 1, prime)


num = int(input("Upperbound:"))
print(listNPrimes(num))
