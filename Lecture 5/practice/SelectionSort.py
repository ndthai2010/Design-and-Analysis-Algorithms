def selectionSort(array):
    r = array
    for i in range(0, len(r)):
        for j in range(i + 1, len(r)):
            min = r[i]
            if min > r[j]:
                temp = r[i]
                r[i] = r[j]
                r[j] = temp
    return r

def printArray(r):
    print(*r)


array = ["H", "O", "M", "E", "W", "R", "K"]
print("Alphabetical order of 'H', 'O', 'M', 'E', 'W', 'R','K' is:")
r = selectionSort(array)
printArray(r)

#Result is "E H K M O R W"