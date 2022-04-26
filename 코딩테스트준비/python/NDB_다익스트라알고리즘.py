import sys
input = sys.stdin.readline
INF = int(1e9) #무한을 의미 10억 설정

n, m = map(int, input().split())

start = int(input())

graph = [[] for i in range(n+1)]

visited = [False] * (n+1)

distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())

    graph[a].append((b,c))

def get_samllest_node():
    min_value = INF
    index =0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    #시작노드에서 뻗은 곳 까지 거리 계산
    for j in graph[start]:
        distance[j[0]] = j[1]

    for i in range(n - 1):
        now =get_samllest_node()
        visited[now] = True

        for j in graph[now]:
            #현재 위치까지의 거리값 + 목표지 까지의 값   vs  기존 출발지에서 목표지까지의 값
            cost = distance[now] + j[1]

            if cost < distance[j[0]]:
                distance[j[0]] = cost
dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
