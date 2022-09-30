from itertools import combinations
from collections import deque

def solution(n, wires):
    answer = 100
    
    li = list(combinations(wires, len(wires)-1))
    
    for l in li:
        
        graph = [[] for _ in range(n+1)]
        
        for s,e in l:
            
            graph[s].append(e)
            graph[e].append(s)
        
        ##입력끝
        result = [-1 for _ in range(n+1)]
        
        result[0] = 0
        
        Q = deque()
        
        Q.append(1)
        while Q:
            
            tmp = Q.popleft()
            
            result[tmp] = 1
            
            for t in graph[tmp]:
                
                if result[t] == -1:
                    Q.append(t)
                
        answer = min(answer, abs(sum(result)))
        
        
        
    
    return answer