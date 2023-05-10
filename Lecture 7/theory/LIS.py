from time import process_time

def longestIncreasingSubsequence(numbers):
    temp_list = [1 for x in range(0, n)]
    i, j = 1, 0
    while i < len(numbers) and j < len(numbers):
        if numbers[j] < numbers[i]:
            if temp_list[j] + 1 > temp_list[i]:
                temp_list[i] = temp_list[j] + 1
        j = j + 1
        if j == i:
            j, i = 0, i + 1
    return max(temp_list)

if __name__ == '__main__':
    print("Number of elements:") # 3
    n = int(input())
    start = process_time()
    numbers = []
    for i in range (0, n):
        print("Number", i, "is:")# 2 4 5
        numbers.append(int(input()))
    end = process_time()
    print("LIS is", longestIncreasingSubsequence(numbers)) # 3
    print("Time complexity for LIS is ", end - start, "(seconds)")