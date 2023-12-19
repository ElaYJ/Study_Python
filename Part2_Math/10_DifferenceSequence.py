'''
 # [계차수열(difference sequence)]
'''

# an = {3, 7, 13, 21, 31, 43, 57}
# bn =  {4   6   8   10  12  14}

inputA1 = 3 # an의 첫번째 항
inputAN = 7 # an의 7번째 항의 값 출력
inputB1 = 4 # bn의 첫번째 항
inputBD = 2 # bn의 공차 d

valueAN = 0
valueBN = 0
n = 1
while n <= inputAN:

    if n == 1:
        valueAN = inputA1
        valueBN = inputB1
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
print()

valueAN = inputA1
valueBN = inputB1
an = {1:inputA1}
bn = {1:inputB1}
print('an의 첫번째 항의 값: {}'.format(valueAN))

for n in range(2, inputAN + 1):
    valueAN += valueBN
    valueBN += inputBD
    an[n] = valueAN
    bn[n] = valueBN
    print('an의 {}번째 항의 값: {}'.format(n, valueAN))

print('an의 {}번째 항의 값: {}'.format(inputAN, valueAN))

print(f'an = {list(an.values())}')

del bn[inputAN]
print(f'bn =   {list(bn.values())}')
print()


#n^2 + n + 1 = an
valueAN = inputAN ** 2 + inputAN + 1
print('an의 {}번째 항의 값: {}'.format(inputAN, valueAN))
