def solution(citations):
    answer = 0
    n = len(citations)
    
    m = max(citations)
    #인용횟수배열
    arr = [0] * (m+1)
    
    for i in citations:
        arr[i] +=1

    for h in range(m+1):
        
        tmp1 = sum(arr[:h+1])
        tmp2 = sum(arr[h:])
        
        if tmp2 >= h >=tmp1:
            answer = h
        
    return answer