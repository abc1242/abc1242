import heapq

def solution(scoville, K):
    answer = 0
    
    Q = []
    
    for i in scoville:
        heapq.heappush(Q,i)
    tmp1 =0
    while Q:
        
        tmp1 = heapq.heappop(Q)
        if tmp1 >= K:
            break
        if not Q:
            break
        tmp2 = heapq.heappop(Q)
        
        if tmp1 < K:
            tmp3 = tmp1+tmp2*2
            heapq.heappush(Q,tmp3)
            
            answer+=1
    if tmp1 <K:
        answer = -1
    return answer