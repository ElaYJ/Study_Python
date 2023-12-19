'''
 # [등차수열(arithmetic sequence, arithmetical progression)]
'''

# n번째 항의 값을 출력하는 프로그램
inputA1 = 2
inputD = 3
inputN = 7

valueN = 0
n = 1
while n <= inputN:

    # 첫 번째 항 등록
    if n == 1:
        valueN = inputA1
        print('{}번째 항의 값: {}'.format(n, valueN))
        n += 1
        continue
    # 두 번째 항부터 n항까지 공차를 더해간다.
    valueN += inputD
    print('{}번째 항의 값: {}'.format(n, valueN))
    n += 1

print('{}번째 항의 값: {}'.format(inputN, valueN))
print()

for n in range(1, inputN + 1):
    if n == 1:
        valueN = inputA1
        print('{}번째 항의 값: {}'.format(n, valueN))
        continue

    valueN += inputD
    print('{}번째 항의 값: {}'.format(n, valueN))

print('{}번째 항의 값: {}'.format(inputN, valueN))
print()

# 등차 수열(일반항) 공식: an = a1 + (n-1) * d
valueN = inputA1 + (inputN - 1) * inputD
print('{}번째 항의 값: {}'.format(inputN, valueN))
print()


# n번째 항까지의 합을 출력하는 프로그램
inputA1 = 5
inputD = 4
inputN = 7

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

    valueN += inputD
    sumN += valueN
    print('{}번째 항까지의 합: {}'.format(n, sumN))
    n += 1

print('{}번째 항까지의 합: {}'.format(inputN, sumN))
print()


valueN = inputA1
sumN = valueN
print('첫번째 항까지의 합: {}'.format(sumN))

for n in range(2, inputN + 1):
    valueN += inputD
    sumN += valueN
    print('{}번째 항까지의 합: {}'.format(n, sumN))

print('{}번째 항까지의 합: {}'.format(inputN, sumN))
print()


# 등차 수열(합) 공식: sn = n(a1 + an) / 2
valueN = inputA1 + (inputN - 1) * inputD
sumN = inputN * (inputA1 + valueN) / 2
print('{}번째 항까지의 합: {}'.format(inputN, int(sumN)))
print()

