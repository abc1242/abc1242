from itertools import permutations

N,M = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort()
ar= permutations(arr,M)

for a in ar:

  print(*a)