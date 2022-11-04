import sys
#회의실 수, 예약회의 수
N, M = map(int, input().split())

table = [[0] * 9 for _ in range(N)]
name = []

for _ in range(N):
    name.append(input())
name.sort()

#회의실 체크
for _ in range(M):
    r, s, t = input().split()

    s = int(s)-9
    t = int(t)-9

    idx = name.index(r)
    
    for i in range(s,t):
        table[idx][i] = 1

for i in range(N):

    s = 'Room ' + name[i]+':'
    print(s)

    ava_time = []


    start = ''
    end = ''
    for j in range(9):


        if table[i][j] == 0 and start == '':

            if j == 0:
                start = '09-'
            else:

                start += str(j+9)+'-'
        
        
        if table[i][j] == 1 and start !='' and end == '':

            
            s = start + str(j+9)

            ava_time.append(s)
            start = ''
            end = ''

        if j == 8 and start !='':
            s = start + '18'
            ava_time.append(s)

    if len(ava_time) == 0 :
        print('Not available')
    else:
        print(str(len(ava_time))+' available:')
        for q in ava_time:
            print(q)
    if i < N-1:
        print('-----')