def solution(board, skill):
    answer = 0
    
    
    #누적합으로 풀어보자
    
    N = len(board)
    M = len(board[0])
    
    arr = [[0 for _ in range(M+1)] for _ in range(N+1)]
    
    for t,r1,c1,r2,c2,d in skill:
        
        if t == 1:
            d *= -1
        
        r2 +=1
        c2 +=1
        
        arr[r1][c1] += d
        arr[r2][c2] += d
        
        arr[r2][c1] += -d
        arr[r1][c2] += -d
    
    
    #오른쪽으로 더하기
    
    for r in range(N+1):
        
        for c in range(1, M+1):
            
            arr[r][c] += arr[r][c-1]
    
    #아래로 더하기
    
    for c in range(M+1):
        
        for r in range(1, N+1):
            
            arr[r][c] += arr[r-1][c]
    

    
    for r in range(N):
        
        for c in range(M):
            
            board[r][c] += arr[r][c]
            
            if board[r][c]>0:
                answer+=1
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#     for i in skill:
        
#         t, r1,c1,r2,c2,d = i
        
#         if t==1:
#             d *= -1
        
#         for r in range(r1,r2+1):
            
#             for c in range(c1, c2+1):
                
#                 board[r][c] +=d
        
    
    
#     for boa in board:
        
#         for b in boa:
            
#             if b > 0:
#                 answer+=1
    
    
    
    
    
    return answer