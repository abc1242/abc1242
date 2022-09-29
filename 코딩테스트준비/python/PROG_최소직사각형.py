def solution(sizes):
    answer = 0
    
    w = 0
    h = 0
    
    for s in sizes:
        a,b = min(s), max(s)
        
        w = max(w,a)
        h = max(h,b)
    
    answer = w*h
        
    
    return answer