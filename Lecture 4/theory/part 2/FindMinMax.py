from numpy.random import randint
import random
import matplotlib.pyplot as mp
from time import process_time

def maxElement(a, left, right):
	if left == right:
		return a[left]
	middle = (left + right) // 2
	u = maxElement(a, left, middle)
	v = maxElement(a, middle + 1, right)
	return max(u, v)

def minElement(a, left, right):
	if left == right:
		return a[right]
	middle = (left + right) // 2;
	u = minElement(a, left, middle)
	v = minElement(a, middle + 1, right)
	return min(u, v)

def diagram():
	sizeOfInputs = []
	time = []
	for n in range(2, 1000, 10):
		start = process_time()
		a = randint(1000, size=(n))
		print(a)
		print("max of array =", maxElement(a, 0, n - 1), ", min of array =", minElement(a, 0, n - 1))
		end = process_time()
		print("Find max element and min element of array in", end - start)
		print()
		sizeOfInputs.append(n)
		time.append(end - start)

	mp.xlabel('Size of input')
	mp.ylabel('Time complexity')
	mp.plot(sizeOfInputs, time, label = "Max element and min element of array")
	mp.grid()
	mp.legend()
	mp.show()

diagram()