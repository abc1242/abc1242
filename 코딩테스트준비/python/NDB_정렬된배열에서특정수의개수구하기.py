from bisect import bisect_left, bisect_right

N, M = map(int, input().split())

arr = list(map(int, input().split()))

start = bisect_left(arr,M)
end = bisect_right(arr,M)

count = end -start

if count == 0 :
    print(-1)
else:
    print(end - start)