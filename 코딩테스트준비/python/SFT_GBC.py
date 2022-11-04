import sys

N, M = map(int, input().split())

gbc = [0]*101

b = 0
for _ in range(N):
    l , speed = map(int, input().split())

    for i in range(b,b+l):
        gbc[i] = speed
    b += l

now = 0
res = 0
for _ in range(M):
    l , speed = map(int, input().split())

    for i in range(now, now+l):

        res = max(speed - gbc[i],res)
    now +=l

print(res)
