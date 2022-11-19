def binary(n):

    cnt = 0

    while n > 0:
        
        if n%2 == 1:
            cnt+=1
        
        n //=2

    return cnt


def solution(n):
    answer = 0
    
    t = binary(n)

    i = n+1
    while True:

        if binary(i) == t:
            
            answer = i
            break
        else:
            i+=1
    
    
    return answer