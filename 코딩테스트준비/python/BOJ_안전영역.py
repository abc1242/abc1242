import sys

sys.setrecursionlimit(999999)

input = sys.stdin.readline

N = int(input())

arr = []

maxh = 0

for _ in range(N):

  tmp = list(map(int, input().split()))
  arr.append(tmp)
  maxh = max(max(tmp),maxh)


result = 0


def dfs(r,c,h):

  visited[r][c] = True

  for dr, dc in [(-1,0) , (1,0) , (0, -1) , (0, 1)]:

    nr = r + dr
    nc = c + dc
    if  0 <= nr < N and 0 <= nc < N and visited[nr][nc] == False and arr[nr][nc] > h:
      dfs(nr, nc,h)


for h in range(0, maxh):

  visited = [[False] * N for _ in range(N)]
  cnt = 0
  
  for r in range(N):
    for c in range(N):
      

      if arr[r][c] > h and visited[r][c] == False:
        cnt +=1
        dfs(r,c,h)

  result = max(result, cnt)

print(result)