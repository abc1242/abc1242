from collections import deque

s,e = map(int, input().split())

Q = deque()
Q.append([s,1])
res = -1
while Q:

  now,cnt = Q.popleft()

  cnt +=1
  if now*2 <= int(1e9):

    if now*2 == e:
      res = cnt
      break
    else:
      Q.append([now*2,cnt])
  if now*10+1 <= int(1e9):
    if now*10+1== e:
      res = cnt
      break
    else:
      Q.append([now*10+1,cnt])

print(res)
