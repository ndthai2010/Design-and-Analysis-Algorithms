def printBinary(arr, n):
    for i in range(0, n):
        print(arr[i], end=" ")
    print()

def generateBinaryStrings(n, arr, i):
    if i == n:
        printBinary(arr, n)
        return

    arr[i] = 0
    generateBinaryStrings(n, arr, i + 1)

    arr[i] = 1
    generateBinaryStrings(n, arr, i + 1)


if __name__ == "__main__":

    print("Enter binary length:")
    n = int(input())
    arr = [None] * n
    generateBinaryStrings(n, arr, 0)
