def solution(arr):
    answer = []
    before = -1
    for i in arr:
        
        if i == before:
            continue
        else:
            answer.append(i)
            before = i
    
    
    
    return answer