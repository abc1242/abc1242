from collections import deque

def solution(n, computers):
    answer = 0
    
    v = [False] * n
    
    Q = deque()
    
    for i in range(n):
        
        if v[i] == True:
            continue
        answer += 1

        Q.append(i)
        
        while Q:
            
            tmp = Q.popleft()
            
            v[tmp] = True
            print(tmp)
            
            for j in range(n):
                if computers[tmp][j] == 0:
                    continue
                if v[j] == True:
                    continue

                    
                Q.append(j)
                
    
    return answer

    
    
    
    
    
    