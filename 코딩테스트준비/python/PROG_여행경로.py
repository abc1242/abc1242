# https://gurumee92.tistory.com/165
# https://school.programmers.co.kr/questions/29334
from collections import defaultdict

def solution(tickets):
    answer = []
    
    routes = defaultdict(list)
    
    
    for start, end in tickets:

        routes[start].append(end)
    
    for r in routes.keys():
        routes[r].sort(reverse=True)
    st = ['ICN']
    path = []
    
    while st:
        
        top = st[-1]
        
        if top not in routes or len(routes[top]) == 0:
            path.append(st.pop())
        else:
            st.append(routes[top][-1])
            routes[top] = routes[top][:-1]
    
    
    
    answer = path[::-1]

    
    
    
    
    return answer