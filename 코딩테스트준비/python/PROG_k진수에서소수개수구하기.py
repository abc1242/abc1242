
def isPrime(n):
    
    if n <=1 :
        return False
    
    i = 2
    while i*i <=n:
        if n% i ==0:
            return False
        i+=1
    return True



def solution(n, k):
    answer = 0
    
    tmp = ''
    
    
    while n >= k:
        
        tmp += str(n%k)

        n //= k
    
    tmp +=str(n)
    
    tmp = tmp[::-1]

    arr = list(tmp.split('0'))
    
    

    for i in arr:
        
        if i == '':
            continue

        i = int(i)
        
        if isPrime(i):
            answer+=1
        
        
        
        
    
    
    return answer