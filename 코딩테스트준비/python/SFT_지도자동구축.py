import sys

N = int(input())

arr = [0] * 16
arr[0] = 2

for i in range(1,16):
    arr[i] = arr[i-1]*2 -1

print(arr[N]*arr[N])
