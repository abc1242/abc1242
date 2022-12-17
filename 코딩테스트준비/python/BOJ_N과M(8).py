from itertools import combinations_with_replacement

N,M = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort()
ar= combinations_with_replacement(arr,M)

for a in ar:

  print(*a)