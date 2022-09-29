from itertools import permutations

def isprime(n):
    
    if n == 1 or n == 0:
        return False
    else:
        i =2
        while i*i <= n:
            
            if n% i  == 0:
                return False
            i+=1
        return True
            


def solution(numbers):
    answer  = 0
    result = []
    
    for i in range(len(numbers)+1):
        result = result+list(permutations(numbers,i))  

    checked = []
    for r in result[1:]:
        
        tmp = ''
        
        for a in r:
            tmp +=a
        
        tmp = int(tmp)
        
        if tmp in checked:
            continue
        else:
            checked.append(tmp)
            
            if isprime(tmp):
                answer+=1
                print(tmp)
    
    return answer