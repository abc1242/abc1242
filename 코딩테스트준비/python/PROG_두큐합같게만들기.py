# https://a-littlecoding.tistory.com/m/123
from collections import deque

def solution(queue1, queue2):
    answer = 0

    Q1 = deque(queue1)
    Q2 = deque(queue2)
    limit = (len(queue1)) * 3
    s1 = sum(Q1)
    s2 = sum(Q2)
    

    while s1 != s2 :
        
        if s1 > s2:
            tmp = Q1.popleft()
            Q2.append(tmp)
            
            s1 -= tmp
            s2 += tmp
            answer+=1
        
        elif s1 < s2:
            tmp = Q2.popleft()
            Q1.append(tmp)
            
            s2 -= tmp
            s1 += tmp
            answer+=1

        if answer >= limit:
            answer = -1
            break

    
    return answer