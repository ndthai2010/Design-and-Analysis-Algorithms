from time import process_time
import random

def findMin(valueMoney):

	#can phai sap xem cac menh gia theo thu tu tang dan
	
	denomination = [1000, 2000, 5000, 10000, 20000, 50000,
			100000, 500000]

	n = len(denomination)
	
	result = []

	i = n - 1

	while(i >= 0):
		
		while (valueMoney >= denomination[i]):
			valueMoney = valueMoney -  denomination[i]
			result.append(denomination[i])

		i = i - 1

	for i in range(len(result)):
		print(result[i], end = " ")

if __name__ == '__main__':
	# gioi han can doi so tien tu 1 nghin dong toi 1 trieu dong
	requireMoney = random.randint(1000,10000000)
	print("We need to use this denomination for transfering", requireMoney, ": ", end = "")
	print(" ")
	start = process_time()
	findMin(requireMoney)
	end = process_time()
	print (" ")
	print ("Time complexity for finding minumum coin is ", end - start , "(seconds)")
	

