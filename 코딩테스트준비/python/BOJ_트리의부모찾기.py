import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(N-1):

  s, e = map(int, input().split())

  graph[s].append(e)
  graph[e].append(s)

res = [0]* (N+1)

Q = deque()

Q.append(1)

while Q:

  tmp = Q.popleft()

  for n in graph[tmp]:

    if res[n] != 0:
      continue
    Q.append(n)

    res[n] = tmp


for i in range(2,N+1):
  print(res[i])