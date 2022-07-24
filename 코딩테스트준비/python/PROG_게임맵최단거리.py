from collections import deque

def solution(maps):
    answer = 0
    
    q = deque()
    
    q.append([0,0])

    dx = [0, 1, -1, 0]
    dy = [1, 0 , 0, -1]
    while True:
        
        if len(q) == 0:
            break
        
        tmp = q.popleft()
    
        for i in range(4):
            nx = tmp[0] + dx[i]
            ny = tmp[1] + dy[i]
            
            if nx >=0 and ny >= 0 and nx < len(maps) and  ny < len(maps[0]):
                
                if maps[nx][ny] == 1:
                    maps[nx][ny] += maps[tmp[0]][tmp[1]]
                    q.append([nx,ny])
                    
                    if nx == len(maps)-1 and ny == len(maps[0])-1:
                        break
    
    if maps[-1][-1] == 1:
        answer = -1
    else:
        answer = maps[-1][-1]
        
    
    print(maps)
    return answer