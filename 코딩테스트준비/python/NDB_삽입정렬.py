array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        #자기 기준 왼쪽들 것과 비교하여 자기보다 큰 것을 찾고 그 왼쪽에 들어감
        if array[j] < array[j -1]:
            array[j], array[j-1] = array[j-1],array[j]
        else:
            break
print(array)
