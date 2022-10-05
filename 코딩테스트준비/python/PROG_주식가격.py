# https://sanghyu.tistory.com/155
def solution(prices):
    answer = [0] * len(prices)
    
    #인덱스 값 = 시간초
    s = [0]
    
    
    for i in range(1,len(prices)):
        
        while s and prices[s[-1]] > prices[i]:
            
            
            answer[s[-1]] = i-s[-1]
            s.pop()
        
        s.append(i)
    while s:
        i = s.pop()
        answer[i] = len(prices)-1-i
    
    return answer