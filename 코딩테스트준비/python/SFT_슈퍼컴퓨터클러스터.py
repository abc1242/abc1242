import sys
import math

N,B = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort()


left = 0

#최대성능
right = arr[-1] + int(math.sqrt(int(10e18)))

res = 0

while right-left>1:

    mid = (left + right) //2

    cost = 0
    
    overcost = False
    for a in arr:

        if a > mid:
            break

        cost += (mid-a)**2

        if cost >B:
            overcost = True
            break
    
    if overcost:
        right = mid
    else:
        left = mid


print(left)