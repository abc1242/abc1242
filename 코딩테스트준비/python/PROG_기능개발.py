import math
from collections import deque
def solution(progresses, speeds):
    answer = []
    
    
    for i in range(len(speeds)):
        
        progresses[i] = math.ceil((100 - progresses[i]) /speeds[i])
    
    now = progresses[0]
    tmp = 0
    for i in progresses:
        
        if i <= now:
            tmp+=1
        else:
            answer.append(tmp)
            tmp = 1
            now = i
        
    answer.append(tmp)
        
        
    
    
    return answer