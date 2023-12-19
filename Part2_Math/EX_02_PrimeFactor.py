import random

rNum = random.randint(100, 1000)
print(f'rNum: {rNum}')

soinsuList = []

# 소인수분해
n = 2
while n <= rNum:
    if rNum % n == 0:
        print(f'소인수: {n}')
        soinsuList.append(n)
        rNum /= n
    else:
        n += 1

print(f'soinsuList: {soinsuList}')

tempNum = 0
for s in soinsuList:
    if tempNum != s:
        print(f'{s}\'s exponent: {soinsuList.count(s)}')
        tempNum = s
