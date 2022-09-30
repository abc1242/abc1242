from collections import deque


def relo(n,m):

    n -= 1
    
    if n == -1:
        n = m-1
    
    return n
    
def solution(priorities, location):
    answer = 0
    
    Q = deque(priorities)
    cnt = 0
    while Q:
        
        max_value = max(Q)
        
        tmp = Q.popleft()
        
        #나간경우
        if tmp == max_value:
            cnt +=1
            
            if location == 0:
                answer = cnt
                break

        else:
            Q.append(tmp)
            
        location = relo(location, len(Q))

    
    
    return answer