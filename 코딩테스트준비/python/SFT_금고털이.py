import sys

input = sys.stdin.readline

W,N = map(int, input().split())

arr = []

for _ in range(N):

    arr.append(list(map(int, input().split())))

arr.sort(key = lambda x : -x[1])

res = 0

for m,p in arr:
    
    if W >= m:

        res += m*p
        W -=m
    else:


        res += W*p
        break
print(res)