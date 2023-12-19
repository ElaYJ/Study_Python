'''
# [비교 연산자] : >, >=, <, <=, ==, !=
    ▶ ord(), chr() : 문자와 아스키 코드 변환 함수
'''

# 숫자 비교 -------------------------------------------------------------------------------------------
num1 = 10; num2 = 5
print(f'num1 = {num1}, num2 = {num2}')

result = num1 > num2
print(f'num1 > num2 : {result}')
result = num1 >= num2
print(f'num1 >= num2 : {result}')
result = num1 < num2
print(f'num1 < num2 : {result}')
result = num1 <= num2
print(f'num1 <= num2 : {result}')
result = num1 == num2
print(f'num1 == num2 : {result}')
result = num1 != num2
print(f'num1 != num2 : {result}')

userInputNum1 = 11 # int(input('첫 번째 숫자 입력 : '))
userInputNum2 = 27 # int(input('두 번째 숫자 입력 : '))
print('{} > {} : {}'.format(userInputNum1, userInputNum2, (userInputNum1 > userInputNum2)))
print('{} >= {} : {}'.format(userInputNum1, userInputNum2, (userInputNum1 >= userInputNum2)))
print('{} < {} : {}'.format(userInputNum1, userInputNum2, (userInputNum1 < userInputNum2)))
print('{} <= {} : {}'.format(userInputNum1, userInputNum2, (userInputNum1 <= userInputNum2)))
print('{} == {} : {}'.format(userInputNum1, userInputNum2, (userInputNum1 == userInputNum2)))
print('{} != {} : {}'.format(userInputNum1, userInputNum2, (userInputNum1 != userInputNum2)))


# 문자 비교 -------------------------------------------------------------------------------------------
cha1 = 'A' # 65
cha2 = 'S' # 83
print('\'{}\' > \'{}\' : {}'.format(cha1, cha2, (cha1 > cha2)))
print('\'{}\' >= \'{}\' : {}'.format(cha1, cha2, (cha1 >= cha2)))
print('\'{}\' < \'{}\' : {}'.format(cha1, cha2, (cha1 < cha2)))
print('\'{}\' <= \'{}\' : {}'.format(cha1, cha2, (cha1 <= cha2)))
print('\'{}\' == \'{}\' : {}'.format(cha1, cha2, (cha1 == cha2)))
print('\'{}\' != \'{}\' : {}'.format(cha1, cha2, (cha1 != cha2)))

# ord(), chr() : 문자와 아스키 코드 변환 함수
print('\'A\' -> {}'.format(ord('A')))
print('\'S\' -> {}'.format(ord('S')))
print('65 -> {}'.format(chr(65)))
print('83 -> {}'.format(chr(83)))


# 문자열 비교 ------------------------------------------------------------------------------------------
str1 = 'Hello'; str2 = 'hello'
print(f'{str1} == {str2} : {str1 == str2}')
print(f'{str1} != {str2} : {str1 != str2}')
