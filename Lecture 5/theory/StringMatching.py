def strMatching(string, pattern):
    n = len(string)
    m = len(pattern)
    if m > n:
        print("No Match Found")
    else:
        found = False
        for i in range(0, n - m + 1):
            j = 0
            while j < m and string[i] == pattern[j] :
                i = i + 1
                j = j + 1
            if j == m:
                found = True
                print("Matching Found At " + str(i - m + 1))
        if not found:		
            print("No Matching Found")

if __name__ == "__main__": 
    print("String 1:")
    string = input()
    print("String 2:")
    pattern = input()
    strMatching(string, pattern)