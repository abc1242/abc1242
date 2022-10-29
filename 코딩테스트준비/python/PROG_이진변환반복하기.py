def bi(n):
    
    t= ''
    
    while n >0:
        
        if n %2 == 1:
            t+='1'
            n //=2
        else:
            t+='0'
            n//=2
            
    return t[::-1]


def solution(s):
    answer = []
    
    a,b = 0,0
    
    while s != '1':
        tmp = ''
        #0지우기
        for i in s:
            
            if i !='0':
                tmp+=(i)
            else :
                b+=1
        
        c = len(tmp)


        s = bi(c)
        a+=1

    answer = [a,b]

    return answer