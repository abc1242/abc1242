def solution(number, k):
    answer = []
    
    for n in number:
        
        while k>0 and answer and answer[-1] < n:
            
            answer.pop()
            k-=1
        answer.append(n)
        
    res = ''
    for a in answer[:len(number)-k]:
        res +=a
        
        
    return res