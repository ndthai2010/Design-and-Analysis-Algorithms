from time import process_time
import random

def changeMoney(denomination, money):
    result = []
    for i in range(len(denomination)):
        result.append(0)
    i = len(denomination) - 1
    while i <= len(denomination) and money > 0:
        result[i] = money // denomination[i]
        money -= result[i] * denomination[i]
        i = i - 1
    if money > 0:
        return -1
    else:
        return result

def main():
    denomination = [1, 5, 10, 50]
    start = process_time()
    
    money = random.randint(100, 1000000)
    result = changeMoney(denomination, money)
    print("Changes", money)
    print(denomination[0], ":", result[0])
    print(denomination[1], ":", result[1])
    print(denomination[2], ":", result[2])
    print(denomination[3], ":", result[3])
    
    end = process_time()
    print("Time complexity for finding minimum coin is ", end - start, "(seconds)")
    
if __name__ == '__main__':
    main()
