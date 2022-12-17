N,M = map(int, input().split())

res =1
for i in range(N,N-M,-1):
  res *= i


for i in range(1,M+1):
  res//=i
print(res)