import sys

msg = input()
key = input()

s = set()
tmp = []
for k in key:
    if k in s:
        continue
    
    s.add(k)
    tmp.append(k)

alpha = ['A','B','C','D','E','F','G','H','I','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

for a in alpha:

    if a not in tmp:
        tmp.append(a)

arr_key = []

for i in range(5):

    t = [tmp[i*5],tmp[i*5+1], tmp[i*5+2], tmp[i*5+3], tmp[i*5+4]]
    arr_key.append(t)
#키생성 끝



m = []

t = ''
for i in msg:
    
    if t == '':
        t = i
    else:
        if t == i:
            if t == 'X':
                m.append([t,'Q'])
                t = i
            else:
                m.append([t,'X'])
                t = i
        else:
            m.append([t,i])
            t = ''

if t != '':
    m.append([t,'X'])
#두개씩 나누기 끝

#답
res = ''

for a,b in m:
    
    a1,a2,b1,b2 = 0,0,0,0

    #가로 검사
    for i in range(5):
        for j in range(5):

            if arr_key[i][j] == a:
                a1 = i
                a2 = j

            if arr_key[i][j] == b:
                b1 = i
                b2 = j
    
    #같은 가로일경우
    if a1 == b1:
        a2 = (a2+1)%5
        b2 = (b2+1)%5
    #세로검사
    elif a2 == b2:
        a1 = (a1+1)%5
        b1 = (b1+1)%5
    #나머지경우
    else:
        qwe = a2
        a2 = b2
        b2 = qwe
    
    #정답문자열에 추가
    
    res += arr_key[a1][a2] + arr_key[b1][b2]

print(res)