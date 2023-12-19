'''
 # [계차수열(difference sequence)]
'''

# an = {3, 7, 13, 21, 31, 43, 57}
# bn =  {4   6   8   10  12  14}

# inputAN1 = int(input('a1 입력: '))
# inputAN = int(input('an 입력: '))
#
# inputBN1 = int(input('b1 입력: '))
# inputBD = int(input('bn 공차 입력: '))
inputAN1 = 3
inputAN = 7
inputBN1 = 4
inputBD = 2

valueAN = 0
valueBN = 0
n = 1
while n <= inputAN:

    if n == 1:
        valueAN = inputAN1
        valueBN = inputBN1
        print('an의 {}번째 항의 값: {}'.format(n, valueAN))
        print('bn의 {}번째 항의 값: {}'.format(n, valueBN))
        n += 1
        continue

    valueAN = valueAN + valueBN
    valueBN = valueBN + inputBD
    print('an의 {}번째 항의 값: {}'.format(n, valueAN))
    print('bn의 {}번째 항의 값: {}'.format(n-1, valueAN))
    n += 1

print('an의 {}번째 항의 값: {}'.format(inputAN, valueAN))
print('bn의 {}번째 항의 값: {}'.format(inputAN, valueBN))


#n^2 + n + 1 = an
valueAN = inputAN ** 2 + inputAN + 1
print('an의 {}번째 항의 값: {}'.format(inputAN, valueAN))
