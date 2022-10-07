import heapq
def solution(jobs):
    answer = []
    
    heapq.heapify(jobs)
    Q = []
    

    time = 0
    while jobs or Q:
        #작업큐에넣기
        while jobs:
            if time >= jobs[0][0]:
                s,d = heapq.heappop(jobs)
                
                heapq.heappush(Q,[d,s])
            else:
                break
        
        
        if Q and time >=Q[0][1]:
            
            dd, ss = heapq.heappop(Q)
            
            answer.append(time + dd - ss)
            time +=dd-1
        
        
        time+=1
    res = sum(answer)//len(answer)
    return res