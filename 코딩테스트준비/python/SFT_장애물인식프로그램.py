import sys

N = int(input())

arr = []

for _ in range(N):
    tmp = list(map(int,list(input())))
    arr.append(tmp)

res = []
cnt = 0

def dfs(i,j):
    
    global cnt
    for di, dj in [[1,0],[-1,0],[0,1],[0,-1]]:

        ni = i+di
        nj = j+dj

        if 0<=ni<N and 0<=nj<N and arr[ni][nj] == 1:

            arr[ni][nj] = 2
            cnt+=1
            dfs(ni,nj)

for i in range(N):
    for j in range(N):

        if arr[i][j] == 1:
            arr[i][j] =2
            cnt+=1
            dfs(i,j)
            res.append(cnt)
        cnt = 0

res.sort()
print(len(res))
for i in res:
    print(i)
