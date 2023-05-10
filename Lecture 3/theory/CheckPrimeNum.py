import matplotlib.pyplot as mp
from time import process_time
import math


def checkPrimeNumber(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


def primeFactors(x, n):
    if n <= x:
        if x % n == 0 and checkPrimeNumber(n):
            print(n, end=" ")
        primeFactors(x, n + 1)


def drawDiagram():
    size = []
    time = []

    for i in range(0, 1000):
        start = process_time()
        primeFactors(n, 2)
        print()
        end = process_time()

        print("Show prime factors of ", i, "in", end - start)
        size.append(i)
        time.append(end - start)

    mp.xlabel("Size of input ")
    mp.ylabel("Time complexity")
    mp.plot(size, time, label="Prime factors illustration")
    mp.grid()
    mp.legend()
    mp.show()


drawDiagram()
