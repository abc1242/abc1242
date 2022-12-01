from collections import deque

def solution(s):
    answer = 1

    st = deque()
    
    for w in s:
        
        if len(st) == 0:
            st.append(w)
            
        else:
            
            if st[-1] == w:
                st.pop()
            else:
                st.append(w)
    
    if len(st) >0:
        answer = 0
    
    
    return answer