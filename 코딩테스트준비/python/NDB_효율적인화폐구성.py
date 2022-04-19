N, M = map(int, input().split())

arr = list()
for i in range(N):
    arr.append(int(input()))

dp = [-1] * (M+1)

for i in arr:
    dp[i] = 1

for i in range(arr[0], M+1):

    for j in range(N):
        if dp[i - arr[j]] > 0 :
            if dp[i] <= dp[i - arr[j]] + 1 :
                dp[i] = dp[i - arr[j]] + 1

# print(dp[M])
print(dp)