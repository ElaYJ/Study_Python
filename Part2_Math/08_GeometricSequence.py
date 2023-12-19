'''
 # [등비수열(geometric sequence/progression)]
'''

# n번째 항의 값을 출력하는 프로그램
# inputN1 = int(input('a1 입력: '))
# inputR = int(input('공비 입력: '))
# inputN = int(input('n 입력: '))
inputN1 = 2
inputR = 2
inputN = 7

valueN = 0
n = 1
while n <= inputN:

    if n == 1:
        valueN = inputN1
        print('{}번째 항의 값: {}'.format(n, valueN))
        n += 1
        continue

    valueN *= inputR
    print('{}번째 항의 값: {}'.format(n, valueN))
    n += 1

print('{}번째 항의 값: {}'.format(inputN, valueN))


# 등비 수열(일반항) 공식: an = a1 * r^(n-1)
valueN = inputN1 * (inputR ** (inputN-1))
print('{}번째 항의 값: {}'.format(inputN, valueN))



# n번째 항까지의 합을 출력하는 프로그램
# inputN1 = int(input('a1 입력: '))
# inputR = int(input('공비 입력: '))
# inputN = int(input('n 입력: '))
inputN1 = 5
inputR = 3
inputN = 7

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