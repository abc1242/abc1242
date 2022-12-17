from itertools import permutations

N,M = map(int, input().split())

arr = list(map(int, input().split()))


ar= list(set(permutations(arr,M)))
ar.sort()
for a in ar:

  print(*a)