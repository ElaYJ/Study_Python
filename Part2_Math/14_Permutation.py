'''
 # [순열(permutation)]
'''

# 8P3
numN = 8
numR = 3

# nPr = n(n-1)(n-2)...(n-r+1)
result = 1

for n in range(numN, (numN-numR), -1):
    print('n : {}'.format(n))
    result *= n

print('result: {}'.format(result))


# 7P5
numN = 7
numR = 5

# nPr = n!/(n-r)!
resultC = 1
resultP = 1
# n!
for n in range(numN, 0, -1):
    resultC *= n
# (n-r)!
for n in range((numN - numR), 0, -1):
    resultP *= n

print('result: {}'.format(int(resultC/resultP)))



import math

result = int(math.factorial(numN) / math.factorial(numN - numR))
print('result: {}'.format(result))



# 원순열

# n = int(input('친구 수 입력: '))
n = 4

result = 1
for i in range(1, n):
    result *= i

print('result: {}'.format(result))


import math

result = int(math.factorial(n - 1))
print('result: {}'.format(result))
