N, K = map(int, input().split())

arr1 = list(map(int, input().split()))

arr2 = list(map(int, input().split()))

arr1.sort(reverse=True)
arr2.sort(reverse=True)

i = 0
while K > 0:

    #값비교
    if arr1[N-i-1] < arr2[i]:
        arr1[N-i-1] = arr2[i]
        K -=1
        i +=1

print(sum(arr1))