N = int(input())

scary = list(map(int,input().split()))

scary.sort()

result =0
people = 0

for i in scary:
    people +=1

    if people >= i:
        result+=1
        people =0



print(people)