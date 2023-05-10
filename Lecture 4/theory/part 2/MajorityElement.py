from numpy.random import randint
import random
import matplotlib.pyplot as mp
from time import process_time

def hasMajorityElement(arr):
    n = len(arr)
    for i in range(n // 2):
        if arr[i] == arr[i + n // 2]:
            return True
    return False

def diagram():
	sizeOfInputs = []
	time = []
	for n in range(2, 1000, 10):
		start = process_time()
		a = randint(1000, size=(n))
		print(a)
		print("Majority element =", hasMajorityElement(a))
		end = process_time()
		print("Find majority element in", end - start)
		print()
		sizeOfInputs.append(n)
		time.append(end - start)

	mp.xlabel('Size of input')
	mp.ylabel('Time complexity')
	mp.plot(sizeOfInputs, time, label = "Majority element")
	mp.grid()
	mp.legend()
	mp.show()

diagram()