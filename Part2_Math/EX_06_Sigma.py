# inputA1 = int(input('a1 입력: '))
# inputR = int(input('공비 입력: '))
# inputN = int(input('n 입력: '))
inputA1 = 2
inputR = 2
inputN = 30

valueN = 0
sumN = 0
n = 1
while n <= inputN:

    if n == 1:
        valueN = inputA1
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
sumN = inputA1 * (1 - (inputR ** inputN)) / (1 - inputR)
print('{}일째 되는 날 받게 되는 쌀의 개수는 {:,}개'.format(inputN, int(sumN)))
