import matplotlib.pyplot as mp
from time import process_time
from numpy.random import randint

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def drawDiagram():
    size = []
    time = []

    for i in range(0, 1000):
        start = process_time()
        fib(i)
        print()
        end = process_time()

        print("Compute the ", i, "-th Fibonacci number in", end - start)
        size.append(i)
        time.append(end - start)

    mp.xlabel("Size of input ")
    mp.ylabel("Time complexity")
    mp.plot(size, time, label="n-th Fibonacci number")
    mp.grid()
    mp.legend()
    mp.show()

drawDiagram()
