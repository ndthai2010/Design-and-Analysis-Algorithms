# a) Brute-force algorithm
# Complexity: O(n^2)   

def BruteForcePolynominal(A, x):
    pol = 0
    n = len(A)
    for i in range(0, n):
        pol += A[i] * (x**i)
    return pol

# b) Linear algorithm
# Complexity: O(n)

def LinearPolynominal(A, x):
    n = len(A)
    result = A[n - 1]
    for i in range(n - 2, -1, -1):
        result = result * x + A[i]
    return result

# c) Can not design an algorithm better than O(n).

A = [-1, 4, 6]
print(BruteForcePolynominal(A, 2)) #Result is 31
print(LinearPolynominal(A, 2)) #Result is 31