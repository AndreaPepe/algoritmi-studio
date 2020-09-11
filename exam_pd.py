def maxIncreasing(A):
    n=len(A)
    dp=[]
    for i in range(n):
        dp.append(A[i])
        for j in range(i):
            if (A[j] < A[i] and dp[j]+A[i] > dp[i]):
                dp[i] = dp[j] + A[i]

    max=A[0]                                            # return max(dp)!!!
    for i in range(1,n):
        if dp[i]>max:
            max=dp[i]
    return max



A=[1, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11]
print(maxIncreasing(A))
