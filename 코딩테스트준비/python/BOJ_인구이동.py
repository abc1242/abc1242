import sys

sys.setrecursionlimit(10**5)

input = sys.stdin.readline

N, L, R = map(int, input().split())

arr = []

for _ in range(N):

    arr.append(list(map(int, input().split())))

delta = [(1,0) , (-1,0) , (0,1) , (0,-1)]

v = [[False] * N for _ in range(N)]

tmp = []
total = 0

def move(r,c):

    global total


    v[r][c] = True

    total += arr[r][c]
    tmp.append([r,c])

    for dr, dc in delta:

        nr = r + dr
        nc = c + dc

        if 0 <= nr < N and 0<= nc < N and v[nr][nc] == False and L <= abs(arr[r][c] - arr[nr][nc]) <= R:

            move(nr, nc)




for cnt in range(N*N):

    check = False
    
    for r in range(N):
        
        for c in range(N):
            
            if v[r][c] == False:

                move(r,c)

                Average = total // len(tmp)

                for i, j in tmp:

                    arr[i][j] = Average

                if len(tmp) >=2:
                    check = True

                total = 0
                tmp = []


    v = [[False] * N for _ in range(N)]




    if check == False:
        print(cnt)

        break
    else:
        check = False
    
