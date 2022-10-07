import heapq

def solution(n, edge):
    answer = 0
    distance = [int(1e9)] * (n + 1)
    graph = [[] for _ in range(n+1)] 
    
    
    for s,e in edge:
        graph[s].append(e)
        graph[e].append(s)
    
    def dijkstra(start):
        Q = []

        heapq.heappush(Q,[0,start])
        distance[start] = 0

        while Q:

            dist, now = heapq.heappop(Q)

            if dist > distance[now]:
                continue

            for i in graph[now]:
                cost = dist + 1

                if cost < distance[i]:
                    distance[i] = cost
                    heapq.heappush(Q,[cost, i])
    
    dijkstra(1)
    maxy = max(distance[1:])
    
    for a in distance:
        if maxy == a:
            answer+=1
    return answer