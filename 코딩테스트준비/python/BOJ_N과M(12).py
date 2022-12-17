from itertools import combinations_with_replacement

N,M = map(int, input().split())

arr = list(set(map(int, input().split())))
arr.sort()

ar= list(combinations_with_replacement(arr,M))

for a in ar:

  print(*a)