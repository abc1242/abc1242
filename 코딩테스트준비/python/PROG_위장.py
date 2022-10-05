from collections import defaultdict

def solution(clothes):
    answer = 1
    
    closet = defaultdict(list)
    
    for c in clothes:
        
        closet[c[1]].append(c[0])
    
    for c in closet:
        answer *= len(closet[c])+1
    
    return answer-1