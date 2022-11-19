# https://sohee-dev.tistory.com/123
def solution(n, times):
    answer = 0
    
    
    
    left,right = 1,max(times) * n
    
    
    while left <= right:
        
        mid = (left + right) //2
        
        people = 0
        
        for t in times:
            
            people += mid //t
            
            if people >=n:
                break
        
        if people >=n:
            answer =mid
            
            right = mid -1 
            
        else:
            left = mid +1
            
        
        
        
    
    
    
    
    return answer