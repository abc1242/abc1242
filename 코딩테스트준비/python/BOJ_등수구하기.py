import sys

input = sys.stdin.readline

N, score, P = map(int, input().split())

if N ==0:
  print(1)
  
else:
  arr = list(map(int, input().split()))
  arr.append(score)
  arr.sort(reverse=True)

  rank = 0

  before_num = -1

  cnt = 1

  tmp = []

  for i in arr:

    if i < score:
      break

    if before_num == i:

      cnt+=1
    

    else:

      rank+=cnt
      cnt = 1

      before_num = i

    tmp.append(i)


  if len(tmp) >  P:
    print(-1)
  else:
    print(rank)