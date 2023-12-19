'''
 # [등차수열(arithmetic sequence, arithmetical progression)]
'''

# n번째 항의 값을 출력하는 프로그램
# inputN1 = int(input('a1 입력: '))
# inputD = int(input('공차 입력: '))
# inputN = int(input('n 입력: '))
inputN1 = 2
inputD = 3
inputN = 7

valueN = 0
n = 1
while n <= inputN:

    # 첫 번째 항 등록
    if n == 1:
        valueN = inputN1
        print('{}번째 항의 값: {}'.format(n, valueN))
        n += 1
        continue
    # 두 번째 항부터 n항까지
    valueN += inputD
    print('{}번째 항의 값: {}'.format(n, valueN))
    n += 1

print('{}번째 항의 값: {}'.format(inputN, valueN))


# 등차 수열(일반항) 공식: an = a1 + (n-1) * d
valueN = inputN1 + (inputN-1) * inputD
print('{}번째 항의 값: {}'.format(inputN, valueN))


# n번째 항까지의 합을 출력하는 프로그램
# inputN1 = int(input('a1 입력: '))
# inputD = int(input('공차 입력: '))
# inputN = int(input('n 입력: '))
inputN1 = 5
inputD = 4
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

    valueN += inputD
    sumN += valueN
    print('{}번째 항까지의 합: {}'.format(n, sumN))
    n += 1

print('{}번째 항까지의 합: {}'.format(inputN, sumN))


# 등차 수열(합) 공식: sn = n(a1 + an) / 2
valueN = inputN1 + (inputN-1) * inputD
sumN = inputN * (inputN1 + valueN) / 2
print('{}번째 항까지의 합: {}'.format(inputN, int(sumN)))


