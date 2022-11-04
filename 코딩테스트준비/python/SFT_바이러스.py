import sys

k, p, n = map(int, input().split())

# 총 시간동안 바이러스를 증가시킨다.
for i in range(n):
    k = (k * p) % 1000000007

print(k)