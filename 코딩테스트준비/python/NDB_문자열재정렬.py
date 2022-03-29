s = input()
#K1KA5CB7
print(s)

alpha = list()
num = 0

for i in s:
    if i.isalpha():
        alpha.append(i)
    else:
        num +=int(i)


alpha.sort()

if num != 0:
    alpha.append(str(num))

print(''.join(alpha))