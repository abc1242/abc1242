cmd = input()

x = int(ord(cmd[0])) - int(ord('a')) +1
y = int(cmd[1])

steps = [(-2,-1),(-2,1),(2,-1),(2,1),(1,2),(1,-2),(-1,-2),(-1,2)]

result =0
for step in steps:
    dx = x + step[0]
    dy = y + step[1]

    if(dx >= 1 and dx <= 8 and dy >=1 and dy <=8):
        result +=1
print(result)