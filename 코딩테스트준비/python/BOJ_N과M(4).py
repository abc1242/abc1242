from itertools import combinations_with_replacement

N,M = map(int, input().split())


arr = combinations_with_replacement(range(1,N+1),M)

for a in arr:

  print(*a)