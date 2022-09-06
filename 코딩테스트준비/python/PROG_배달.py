import heapq

def solution(N, road, K):
    answer = 0

    graph = [[] for _ in range(N+1)]
    
    for r in road:
        
        s, e, t = r
        
        graph[s].append([e,t])
        graph[e].append([s,t])
    
    
    
    distance = [int(1e9) for _ in range(N + 1)]
    
    distance[1] = 0
    
    Q = []
    
    heapq.heappush(Q, [0,1])
    
    while Q:
        
        dist, now = heapq.heappop(Q)
        
        if distance[now] < dist:
            continue
        #다음 위치 확인
        for index , cost in graph[now]:
            
            total = dist + cost
            
            if total < distance[index]:
                
                distance[index] = total
                heapq.heappush(Q,[total,index])
                
                
    for i in distance:
        
        if i <= K:
            answer +=1
    

    return answer

