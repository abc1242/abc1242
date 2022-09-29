from itertools import permutations

def solution(k, dungeons):
    answer = -1
    
    
    course = []
    
    for i in range(len(dungeons)+1):
        tmp = permutations(dungeons,i)
        
        for t in tmp:

            course.append(t)
    
    
    for c in course[1:]:
        cnt = 0
        heart = k
        
        for a in c:
            
            if heart >= a[0]:
                heart -= a[1]
                cnt+=1
            else:
                break
                
        answer = max(answer,cnt)
        
    
    
    return answer