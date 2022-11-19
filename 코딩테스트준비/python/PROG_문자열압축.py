def solution(s):
    answer = []
    l = len(s)

    res = '0'*l
    if l == 1:
        return 1
    for i in range(1,l):
        
        # if l%i !=0:
        #     continue
        
        #i길이로 잘라서 줄이기
        
        arr = []
        for j in range(0,l,i):
            
            arr.append(s[j:j+i])

        tmp = ''
        
        before = ''
        cnt = 1
        for a in arr:
            if before == '':
                before = a
                continue
            
            
            if before == a:
                cnt +=1
            else:
                
                if cnt>1:
                    
                    tmp += str(cnt) + before
                    cnt =1
                else:
                    tmp +=before
                
  
            
            before = a
            
            
            
        if cnt == 1:
            tmp = tmp+arr[-1]

        else:
            tmp = tmp+str(cnt)+arr[-1]

        answer.append(len(tmp))
        
        
        
        
        
    
    
    return min(answer)