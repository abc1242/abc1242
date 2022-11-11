from itertools import combinations
from collections import defaultdict
def solution(orders, course):
    answer = []
    
    for cnt in course:
        
        dic = defaultdict(int)

        #최대값
        m = 0
        
        for o in orders:
            
            if len(o) <cnt:
                continue
            
            #조합만들기
            for c in combinations(o,cnt):
                c = sorted(c)
                tmp= ''.join(c)
                dic[tmp] +=1
                
                m = max(m,dic[tmp])

        #최대 메뉴 찾기
        if m == 1:
            continue
        for i in dic:
            if dic[i] == m:

                answer.append(i)
            
            
            
            
    answer.sort()
    return answer