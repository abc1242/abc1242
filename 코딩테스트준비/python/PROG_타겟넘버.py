
def solution(numbers, target):
    global answer
    answer = 0
    
    
    
    def dfs(now_num, idx):
        global answer
        if idx == len(numbers):
            if now_num == target:
                answer+=1
            return
        
        dfs(now_num + numbers[idx], idx+1)
        dfs(now_num - numbers[idx], idx+1)
        
    
    dfs(0,0)
        
    
    return answer