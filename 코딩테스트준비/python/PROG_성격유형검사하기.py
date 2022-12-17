from collections import defaultdict

def solution(survey, choices):
    answer = ''
    
    dic = defaultdict(int)
    
    for i, s in enumerate(survey):
        
        n = choices[i]
        
        s1,s2 = s[0],s[1]
        
        if n == 4:
            continue
        elif n < 4:
            
            dic[s1] += 4-n
        
        elif n > 4:
            
            dic[s2] += n-4
        
    if dic['R'] >= dic['T']:
        answer+='R'
    else:
        answer += 'T'
    
    if dic['C'] >= dic['F']:
        answer+='C'
    else:
        answer += 'F'
    
    if dic['J'] >= dic['M']:
        answer+='J'
    else:
        answer += 'M'
    
    if dic['A'] >= dic['N']:
        answer+='A'
    else:
        answer += 'N'
    
    
    
    
    return answer