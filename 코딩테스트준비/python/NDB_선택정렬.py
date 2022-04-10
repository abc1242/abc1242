#선택정렬
#가장 작은수를 찾아 맨앞값과 교체
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    #끝까지 비교하고 나서보면 가장 작은 수를 선택한 상황이다.
    array[i], array[min_index] = array[min_index], array[i]

print(array)