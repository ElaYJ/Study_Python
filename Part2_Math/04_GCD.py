'''
 # [공약수(common divisor] 두 개 이상의 수에서 공통된 약수
 # [최대공약수(the Greatest Common Denominator] 공약수 중 가장 큰 수
'''

# 수 두개의 공약수
input_nums = [12, 36]
min_num = min(input_nums)

for i in range(1, (min_num + 1)):
    if input_nums[0] % i == 0 and input_nums[1] % i == 0:
        print('공약수: {}'.format(i))
print()


# 수 두개의 최대공약수
gcd = 0

for i in range(1, (min_num + 1)):
    if input_nums[0] % i == 0 and input_nums[1] % i == 0:
        gcd = i

print('최대공약수: {}'.format(gcd))
print()



# 수 세개의 공약수
num1 = 12
num2 = 54
num3 = 72
min_num = min(num1, num2, num3)

for i in range(1, (min_num + 1)):
    if num1 % i == 0 and num2 % i == 0 and num3 % i == 0:
        print('공약수: {}'.format(i))
print()


# 수 세개의 최대공약수
gcd = 0

for i in range(1, (min_num + 1)):
    if num1 % i == 0 and num2 % i == 0 and num3 % i == 0:
        gcd = i

print('최대공약수: {}'.format(gcd))
print()


# 유클리드 호제법
num1 = 12; num2 = 36

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


# 유클리드 호제법이란?
# 두 정수 a, b의 최대공약수를 G(a, b)라고한다.
# 정수 a, b, Q(몫), R(나머지) (b != 0, a > b)에 대하여
# a = bQ + R이면 G(a, b) = G(b, r)이 성립한다.

def Euclidean(a, b):
    if b == 0: return a

    return Euclidean(b, (a % b))

print('유클리드 호제법({}, {} GCD) : {}'.format(num1, num2, Euclidean(num1, num2)))
