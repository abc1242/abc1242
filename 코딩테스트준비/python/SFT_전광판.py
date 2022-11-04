import sys
#0~9
num = [
    [1,1,1,0,1,1,1],
    [0,0,1,0,0,1,0],
    [1,0,1,1,1,0,1],
    [1,0,1,1,0,1,1],
    [0,1,1,1,0,1,0],
    [1,1,0,1,0,1,1],
    [1,1,0,1,1,1,1],
    [1,1,1,0,0,1,0],
    [1,1,1,1,1,1,1],
    [1,1,1,1,0,1,1],
]


T = int(input())

for _ in range(T):
    res = 0
    a,b =  input().split()

    a = a[::-1]
    b = b[::-1]

    if len(a) > len(b):
        a,b = b,a

    for i in range(len(b)):
        
        if i > len(a)-1:
            
            res += sum(num[int(b[i])])

        else:

            aa = num[int(a[i])]
            bb = num[int(b[i])]

            for i in range(7):
                if aa[i] != bb[i]:
                    res +=1




    print(res)