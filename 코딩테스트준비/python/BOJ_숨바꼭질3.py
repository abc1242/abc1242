import heapq

N, K = map(int, input().split())

if N==K:
  print(0)
else:

  INF = int(1e9)
  distance = [INF for _ in range(100001)]

  Q = []

  heapq.heappush(Q, [0, N])


  while Q:

    day, now = heapq.heappop(Q)

    if distance[now]  < day:

      continue



    if 0<= now-1 < 100001 and distance[now-1] > day+1:

      distance[now-1] = day+1

      heapq.heappush(Q,[day+1, now-1])

    if 0<= now+1 < 100001 and distance[now+1] > day+1:

      distance[now+1] = day+1

      heapq.heappush(Q,[day+1, now+1])

    if 0<= now*2 < 100001 and distance[now*2] > day:

      distance[now*2] = day

      heapq.heappush(Q,[day, now*2])

  print(distance[K])