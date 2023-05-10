from numpy.random import randint
import random
import matplotlib.pyplot as mp
from time import process_time


def binarySearch(a, x):
    start = 0
    end = len(a) - 1
    a.sort()
    while start <= end:
        middle = start + (end - start) // 2
        if a[middle] == x: 
            return middle
        elif a[middle] < x:
            start = middle + 1
        else:
            end = middle - 1
    return -1


def diagram():
    sizeOfInputs = []
    time = []
    for n in range(1, 1000):
        start = process_time()
        a = randint(1000, size=(n))
        print(a)
        x = random.choice(a)
        print(binarySearch(a, x))
        end = process_time()
        print("Search element", x, "by binary search in", end-start)
        print()
        sizeOfInputs.append(n)
        time.append(end - start)

    mp.xlabel('Size of input')
    mp.ylabel('Time complexity')
    mp.plot(sizeOfInputs, time, label="Binary Search")
    mp.grid()
    mp.legend()
    mp.show()

diagram()
