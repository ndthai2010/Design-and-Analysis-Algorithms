def permute(a, left, right):
    if left == right:
        for i in range(0, len(a)):
            print(a[i], end=" ")
        print()
    else:
        for i in range(left, right + 1):
            a[left], a[i] = a[i], a[left]
            permute(a, left + 1, right)
            a[left], a[i] = a[i], a[left]

def main():
    arr = []
    print("Nhập số phần tử: n = ", end="")
    n = int(input())
    for i in range(0, n):
        print("Nhập phần tử thứ", i + 1, ":")
        arr.append(input())
    print("Các hoán vị của", len(arr), "phần tử trên là:")
    permute(arr, 0, n - 1)
    
if __name__ == '__main__':
    main()