from collections import deque

def solution(s):
    answer = True
    
    Q = deque()
    
    for i in s:
        
        if i == '(':
            Q.append(i)
        else:
            
            if not Q:
                answer = False
                break
            else:
                Q.popleft()

        
    if Q:
        answer = False
    if s[0] == ')':
        answer =False

    return answer