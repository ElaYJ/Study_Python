'''
 # [시그마]
'''

# 등차 수열의 합
# inputN1 = int(input('a1 입력: '))
# inputD = int(input('공차 입력: '))
# inputN = int(input('n 입력: '))
inputN1 = 2
inputD = 2
inputN = 10

valueN = 0
sumN = 0
n = 1
while n <= inputN:

    if n == 1:
        valueN = inputN1
        sumN += valueN
        print('{}번째 항까지의 합: {}'.format(n, sumN))
        n += 1
        continue

    valueN += inputD
    sumN += valueN
    print('{}번째 항까지의 합: {}'.format(n, sumN))
    n += 1

print('{}번째 항까지의 합: {}'.format(inputN, sumN))


# 등차 수열(합) 공식: sn = n(a1 + an) / 2
valueN = inputN1 + (inputN-1) * inputD
sumN = inputN * (inputN1 + valueN) / 2
print('{}번째 항까지의 합: {}'.format(inputN, int(sumN)))





# inputN1 = int(input('a1 입력: '))
# inputR = int(input('공비 입력: '))
# inputN = int(input('n 입력: '))
inputN1 = 2
inputR= 3
inputN = 8

valueN = 0
sumN = 0
n = 1
while n <= inputN:

    if n == 1:
        valueN = inputN1
        sumN += valueN
        print('{}번째 항까지의 합: {}'.format(n, sumN))
        n += 1
        continue

    valueN *= inputR
    sumN += valueN
    print('{}번째 항까지의 합: {}'.format(n, sumN))
    n += 1

print('{}번째 항까지의 합: {}'.format(inputN, sumN))


# 등비 수열(합) 공식: sn = a1 * (1 - r^n) / (1-r)
sumN = inputN1 * (1 - (inputR ** inputN)) / (1 - inputR)
print('{}번째 항까지의 합: {}'.format(inputN, int(sumN)))

