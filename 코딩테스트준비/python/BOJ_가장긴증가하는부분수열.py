import sys
input = sys.stdin.readline
a = int(input())

arr = list(map(int,input().split()))

dp = [1] * a


for i in range(a):

  for j in range(i):

    if arr[i] > arr[j]:

      dp[i] = max(dp[i], dp[j]+1)

print(max(dp))