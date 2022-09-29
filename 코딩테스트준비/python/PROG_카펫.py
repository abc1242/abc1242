def solution(brown, yellow):
    answer = []
    

    
    total = brown + yellow
    
    for i in range(2,brown//2+1):

        if total % i ==0:
            
            w = total // i
            
            outline = 2*(w+i)-4
            inline = total - outline
            
            if brown == outline and yellow ==inline :
                answer=[i,w]
    
    return answer