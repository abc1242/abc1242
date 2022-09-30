from itertools import product


def solution(word):
    answer = 0
    
    li = ['A', 'E', 'I', 'O', 'U']
    di = []
    for i in range(1,6):
        
        tmp = list(product(li,repeat=i))
        
        for tm in tmp:
            
            s = ''
            for t in tm:
                s+=t
            di.append(s)
        
            
        
    di.sort()
    
    
    answer = di.index(word) +1
    
    
    
    
    
    
    
    
    return answer