S = input()

result = int(S[0])

for i in range(1,len(S)):
    if(int(S[i-1])==0 or int(S[i]) ==0):
        result += int(S[i])
    else:
        result *=  int(S[i])

print(result)
