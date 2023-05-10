def greatestArray(arr, k):
    n = len(arr)
    dp = [0] * k
    max_sum = 0

    for i in range(n):
        for j in range(k - 1, -1, -1):
            if j == 0:
                dp[j] = arr[i]
            else:
                dp[j] += arr[i]
            if j == k - 1 and dp[j] > max_sum:
                max_sum = dp[j]

    return max_sum


arr = [2, 1, 5, 1, 3, 2]
k = 3
print(greatestArray(arr, k))  # output: 14
