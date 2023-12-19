'''
 # [조합(combination)]
'''

#8C3
# numN = int(input('numN 입력: '))
# numR = int(input('numR 입력: '))
numN = 5
numR = 2

resultP = 1
resultR = 1
resultC = 1
#nPr
for n in range(numN, (numN-numR), -1):
    print('n : {}'.format(n))
    resultP *= n

print('resultP: {}'.format(resultP))
#r!
for n in range(numR, 0, -1):
    print('n : {}'.format(n))
    resultR *= n

print('resultR: {}'.format(resultR))
# nCr = nPr/r!
resultC = int(resultP / resultR)
print('resultC: {}'.format(resultC))

result = (1/resultC)*100
print('{}%'.format(round(result, 2)))
