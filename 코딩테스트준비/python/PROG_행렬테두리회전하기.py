def solution(rows, columns, queries):
    answer = []
    
   
    
    arr = [[0 for _ in range(columns)] for _ in range(rows)]
    
    tmp = 1
    for i in range(rows):
        for j in range(columns):
            
            arr[i][j] = tmp
            tmp +=1
    
    for x1,y1,x2,y2 in queries:
        
        x1 -=1
        y1 -=1
        x2 -=1
        y2 -=1
        
        small = int(1e9)
        
        #회전 로직
        
        #한칸빼기
        tmp = arr[x1][y1]

        small = min(small,tmp )
        #올리기
        
        for i in range(x1,x2):
            arr[i][y1] = arr[i+1][y1]
            small = min(small,arr[i+1][y1])
            
        #왼쪽으로 밀기
        
        for i in range(y1,y2):
            arr[x2][i] = arr[x2][i+1]
            small = min(small,arr[x2][i+1])
        #내리기
        
        for i in range(x2,x1,-1):
            arr[i][y2] = arr[i-1][y2]
            small = min(small,arr[i-1][y2])
        #오른쪽 밀기
        for i in range(y2,y1,-1):
            arr[x1][i] = arr[x1][i-1]
            small = min(small,arr[x1][i-1])
        #뺀값 넣기
        arr[x1][y1+1] = tmp
        
        answer.append(small)

       
    
    
    return answer