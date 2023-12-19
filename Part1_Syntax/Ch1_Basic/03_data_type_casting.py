'''
# [자료형 변환] : 데이터 타입을 변환하는 것
    ▶ 파이썬에서 제공하는 함수를 사용 : int(), float(), str(), bool()
'''
num1 = 123
num2 = 456
print(num1 + num2)

num1 = str(num1)
num2 = str(num2)
print(num1 + num2)

var = '100'
print(var, '\t\t', type(var))

var = int(var)
print(var, '\t\t', type(var))

var = '10,000'
# var = int(var)
# 단위 구분 문자가 포함된 숫자 문자열은 정수형으로 캐스팅할 수 없다.

var = '3.14'
print(var, '\t\t', type(var))

var = float(var)
print(var, '\t\t', type(var))

var = True
print(var, '\t\t', type(var))

var = int(var)
print(var, '\t\t\t', type(var))

var = False
var = float(var)
print(var, '\t\t', type(var))

var = ''
print(var, '\t\t\t', type(var))

var = bool(var)
print(var, '\t\t', type(var))

# 공백문자
var = ' '
print(var, '\t\t\t', type(var))

var = bool(var)
print(var, '\t\t', type(var))

# 문자열 -> 논리형 -> 산술연산
var1 = 'True'
var2 = 'False'
print(var1, '\t\t', type(var1))
print(var2, '\t\t', type(var2))

var1 = bool(var1)
var2 = bool(var2) # 빈문자가 아니면 True가 나온다.
print(var1, '\t\t', type(var1))
print(var2, '\t\t', type(var2))

print(var1 + var2, '\t\t\t', type(var1 + var2))

var1 = False
var2 = False
print(var1 + var2, '\t\t\t', type(var1 + var2))
