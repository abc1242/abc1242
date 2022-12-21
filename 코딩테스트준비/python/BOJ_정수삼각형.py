import sys
input = sys.stdin.readline
n = int(input())
#7
bef = list(map(int, input().split()))

for _ in range(n-1):
  #3 8
  now = list(map(int, input().split()))

  for i in range(len(now)):

    if i == 0:
      now[i] += bef[i]
    
    elif 0 < i < len(now)-1 :

      now[i] += max(bef[i-1],bef[i])

    else:
      now[i] += bef[i-1]

  bef = now

print(max(bef))

