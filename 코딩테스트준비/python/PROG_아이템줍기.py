#https://sangsangss.tistory.com/199

from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    mapp = [[0 for _ in range(101)] for _ in range(101)]
    
    characterX *=2
    characterY *=2
    itemX *=2
    itemY *=2
    for x1, y1, x2, y2 in rectangle:
        for i in range(2*x1, 2*x2+1):
            for j in range(2*y1, 2*y2+1):
                mapp[i][j] = 1
    
    for x1, y1, x2, y2 in rectangle:
        for i in range(2*x1+1, 2*x2):
            for j in range(2*y1+1, 2*y2):
                mapp[i][j] = 0

    Q = deque()
    
    dx = [1,-1,0,0]
    dy = [0,0,-1,1]
    
    Q.append([characterX,characterY])
    
    while Q:
        
        x,y = Q.popleft()
       
        if x == itemX and  y ==itemY:
            break

        for i in range(4):
            
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0  and ny >= 0 and nx < 101 and ny < 101:
                
                if mapp[nx][ny] == 1:
                    Q.append([nx,ny])
                    mapp[nx][ny] = mapp[x][y] +1
 
                   
    for m in mapp:
        print(m)
    answer = (mapp[itemX][itemY] -1 )//2
    return answer