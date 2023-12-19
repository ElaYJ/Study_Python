'''
# [operator 모듈]
'''

import operator

num1 = 8; num2 = 3
print('{} + {} = {}'.format(num1, num2, operator.add(num1, num2)))
print('{} - {} = {}'.format(num1, num2, operator.sub(num1, num2)))
print('{} * {} = {}'.format(num1, num2, operator.mul(num1, num2)))
print('{} / {} = {}'.format(num1, num2, operator.truediv(num1, num2)))
print('{} % {} = {}'.format(num1, num2, operator.mod(num1, num2)))
print('{} // {} = {}'.format(num1, num2, operator.floordiv(num1, num2)))
print('{} ** {} = {}'.format(num1, num2, operator.pow(num1, num2)))

print('{} == {} : {}'.format(num1, num2, operator.eq(num1, num2)))
print('{} != {} : {}'.format(num1, num2, operator.ne(num1, num2)))
print('{} > {} : {}'.format(num1, num2, operator.gt(num1, num2)))
print('{} >= {} : {}'.format(num1, num2, operator.ge(num1, num2)))
print('{} < {} : {}'.format(num1, num2, operator.lt(num1, num2)))
print('{} <= {} : {}'.format(num1, num2, operator.le(num1, num2)))

flag1 = True; flag2 = False
print('{} and {} : {}'.format(flag1, flag2, operator.and_(flag1, flag2)))
print('{} or {} : {}'.format(flag1, flag2, operator.or_(flag1, flag2)))
print('not {} : {}'.format(flag1, operator.not_(flag1)))


# <Q> ----------------------------------------------------------------------------------------------
# 20세 미만 또는 65세 이상자가 백신 접종 대상자가 될 수 있다.
age = 19 # int(input('나이 입력 : '))
isVaccine = (age < 20) or (age >= 65)
print('age : {}, result : {}'.format(age, isVaccine))
isVaccine = operator.or_(operator.lt(age, 20), operator.ge(age, 65))
print('age : {}, result : {}'.format(age, isVaccine))

# <Q> ----------------------------------------------------------------------------------------------
# 10부터 100사이의 난수 중 십의 자리와 일의 자리가 각각 3의 배수인지 판단하는 코드 작성
# random과 operator 모듈을 사용
import random

rInt = random.randint(10, 100)

num10 = operator.floordiv(rInt, 10)
num01 = operator.mod(rInt, 10)

print(f'난수 : {rInt}')
print(f'십의 자리 : {num10}')
print(f'일의 자리 : {num01}')
print('십의 자리는 3의 배수입니까? {}'.format(operator.eq(operator.mod(num10, 3), 0)))
print('일의 자리는 3의 배수입니까? {}'.format(operator.eq(operator.mod(num01, 3), 0)))