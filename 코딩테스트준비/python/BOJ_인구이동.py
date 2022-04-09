
N, L, R = map(int, input().split())

# arr =[ list(map(int,input().split())) for _ in range(N)]

arr = []
for _ in range(N):
    arr.append(list(map(int,input().split())))

# print(arr)

visited = [ [False] * N for _ in range(N)]

print(visited)

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(i, j):
    queue = [(i, j)]

    while queue:
        r, c = queue.pop(0)
        for dr, dc in delta:
            nr = r + dr
            nc = c + dc
            print(nr, nc)


bfs(2, 3)

# while True:
#     for i in range(N):
#         for j in range(N):
#             bfs(i,j)
#