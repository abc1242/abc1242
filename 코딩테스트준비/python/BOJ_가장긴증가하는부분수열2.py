import bisect

N = int(input())

arr = list(map(int, input().split()))

dp = []

dp.append(arr[0])

for a in arr:

  if dp[-1] > a:

    idx = bisect.bisect_left(dp,a)

    dp[idx] = a

  elif dp[-1] == a:
    continue

  else:

    dp.append(a)

print(len(dp))

