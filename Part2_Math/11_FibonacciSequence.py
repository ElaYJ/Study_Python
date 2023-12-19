'''
 # [피보나치 수열(Fibonacci sequence/series)]
'''

inputN = int(input('n 입력: '))

fibonacci = []
valueN = 0
sumN = 0

valuePreN1 = 0
valuePreN2 = 0

n = 1
while n <= inputN:
    if n == 1 or n == 2:
        valueN = 1
        valuePreN1 = valueN
        valuePreN2 = valueN
        fibonacci.append(valueN)
        sumN += valueN
        n += 1

    else:
        valueN = valuePreN1 + valuePreN2
        valuePreN1 = valuePreN2
        valuePreN2 = valueN
        fibonacci.append(valueN)
        sumN += valueN
        n += 1

print('피보나치 수: {}'.format(fibonacci))
print('{}번째 항의 값: {}'.format(inputN, valueN))
print('{}번째 항까지의 합: {}'.format(inputN, sumN))

