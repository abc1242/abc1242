def solution(n, words):
    answer = [0,0]

    
    turn = 1
    now = 0
    
    used = set()
    endword = words[0][0]
    
    a = words[-1]
    for w in words:
        
        if w[0] != endword:
            break
        else:
            endword = w[-1]
        
        if w in used:
            print(w)
            break
        else:
            used.add(w)
            
            
        now +=1
        
        if now == n:
            now =0
            turn +=1
        
        if w == a:
            answer = [0,0]
        else:
            answer =[now+1,turn]
        
        
    return answer