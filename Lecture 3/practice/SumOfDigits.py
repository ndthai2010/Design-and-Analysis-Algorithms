#1. Tổng các chữ số của 1 số

def sumOfDigits(num):
    if num == 0:
        return 0
    else:
        return num % 10 + sumOfDigits(num // 10)

num = int(input("Number:"))
print("Sum of digits of", num, "is", sumOfDigits(num))