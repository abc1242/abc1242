import sys
input = sys.stdin.readline

n = int(input())

a,b = map(int,input().split())

m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):

  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

v = [False for _ in range(n+1)]



res = -1

def dfs(start, cnt):

  global res
  if start == b:
    res = cnt
    return


  for i in graph[start]:


    if v[i] == False:
      v[i] = True
      dfs(i, cnt+1)



dfs(a,0)


print(res)