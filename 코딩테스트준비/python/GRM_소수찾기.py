import math

n = int(input())
arr = [0] + list(map(int,input().split()))
res = 0

for i in range(2,len(arr)):
	c= True
	
	for j in range(2,int(math.sqrt(i) + 1)):
		
		if i%j==0:
			c = False
			break
	
	if c:
		res +=arr[i]
		
print(res)