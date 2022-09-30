def solution(numbers):
    answer = ''
    
    snum = []
    
    for n in numbers:
        
        snum.append(str(n))

    snum.sort(key = lambda x: x*3 ,reverse=True)

    for i in snum:
        
        answer+=i
        
    answer = str(int(answer))
    return answer