import sys

M, N, K = map(int, input().split())

secret = "".join(input().split())

cmd = "".join(input().split())

if secret in cmd:
    print('secret')
else:
    print('normal')