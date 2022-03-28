N = int(input())

coin = 0
#시작
#500
coin += N//500
N = N%500
#100
coin += N//100
N = N%100
#50
coin += N//50
N = N%50
#10
coin += N//10
N = N%10

print(coin)