def solution(s):
    answer = ''
    
    s = s.lower()
    
    blank = False
    for i in s:
        answer+=i

        if i ==' ':
            blank = True
            continue
        if blank:
            if i.isalpha():
                answer= answer[:-1]+ i.upper()
            blank = False
    
    
    if answer[0].isalpha():
        answer = answer[0].upper() + answer[1:]
    return answer