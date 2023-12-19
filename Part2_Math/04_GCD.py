'''
 # [공약수(common divisor]
 # [최대공약수(the Greatest Common Denominator]
'''

# 수 두개의 공약수
# num1 = int(input('1보다 큰 정수 입력: '))
# num2 = int(input('1보다 큰 정수 입력: '))
num1 = 12; num2 = 36

for i in range(1, (num1 + 1)):
    if num1 % i == 0 and num2 % i == 0:
        print('공약수: {}'.format(i))
print()


# 수 두개의 최대공약수
# num1 = int(input('1보다 큰 정수 입력: '))
# num2 = int(input('1보다 큰 정수 입력: '))
maxNum = 0

for i in range(1, (num1 + 1)):
    if num1 % i == 0 and num2 % i == 0:
        print('공약수: {}'.format(i))
        maxNum = i

print('최대공약수: {}'.format(maxNum))
print()



# 수 세개의 공약수
# num1 = int(input('1보다 큰 정수 입력: '))
# num2 = int(input('1보다 큰 정수 입력: '))
# num3 = int(input('1보다 큰 정수 입력: '))
num1 = 12
num2 = 54
num3 = 72


for i in range(1, (num1 + 1)):
    if num1 % i == 0 and num2 % i == 0 and num3 % i == 0:
        print('공약수: {}'.format(i))
print()


# 수 세개의 최대공약수
# num1 = int(input('1보다 큰 정수 입력: '))
# num2 = int(input('1보다 큰 정수 입력: '))
# num3 = int(input('1보다 큰 정수 입력: '))
maxNum = 0

for i in range(1, (num1 + 1)):
    if num1 % i == 0 and num2 % i == 0 and num3 % i == 0:
        print('공약수: {}'.format(i))
        maxNum = i

print('최대공약수: {}'.format(maxNum))
print()

# 유클리드 호제법
# num1 = int(input('1보다 큰 정수 입력: '))
# num2 = int(input('1보다 큰 정수 입력: '))
num1 = 12; num2 = 58

temp1 = num1; temp2 = num2
while temp2 > 0:
    temp = temp2
    print(f'{temp1} % {temp2} = ', end='')
    temp2 = temp1 % temp2
    print(f'{temp2}')
    temp1 = temp

print('{}, {}의 최대공약수: {}'.format(num1, num2, temp1))

temp1 = num1; temp2 = num2; rest = 1
while  rest > 0:
    print(f'{temp1} % {temp2} = ', end='')
    rest = temp1 % temp2
    print(f'{rest}')
    temp1 = temp2
    temp2 = rest

print('{}, {}의 최대공약수: {}'.format(num1, num2, temp1))

# 최대공약수에서 공약수를 구할 수 있다.
for n in range(1, (temp1 + 1)):
    if temp1 % n == 0:
        print('{}, {}의 공약수: {}'.format(num1, num2, n))


