import matplotlib.pyplot as mp
from time import process_time


def decToBin(x):
    if x >= 1:
        decToBin(x // 2)
    print(x % 2, end='')


def drawDiagram():
    size = []
    time = []

    for i in range(0, 1000):
        start = process_time()
        decToBin(i)
        print()
        end = process_time()

        print("Convert", i, "to binary in", end - start)
        size.append(i)
        time.append(end - start)

    mp.xlabel("Size of input ")
    mp.ylabel("Time complexity")
    mp.plot(size, time, label="Convert decimal to binary")
    mp.grid()
    mp.legend()
    mp.show()


drawDiagram()
