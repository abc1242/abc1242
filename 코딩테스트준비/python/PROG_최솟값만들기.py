def solution(A,B):
    answer = 0

    A.sort()
    B.sort()
    
    l = len(A)
    
    for i in range(l):
        
        tmp1 = A[i]
        tmp2 = B[l-i-1]
        
        answer += tmp1*tmp2
        
        
    return answer