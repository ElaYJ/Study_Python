'''
# [산술 연산자] : +, -, *, /, %, //, **
    ▶ 숫자와 문자는 더할 수 없다.
    ▶ 문자(열)은 뺄셈 연산 불가능!!
    ▶ 0으로 나누는 것은 불가능!!
    ▶ 0을 나누면 결과는 항상 0.0!
    ▶ 나눗셈의 결과는 항상 float!
    ▶ divmode() 함수로 몫[0]과 나머지[1]를 한번에 연산 가능
'''
fnum1 = 3.14
fnum2 = 0.12
result = fnum1 + fnum2
# print(fnum1 + fnum2)
# print(result)
print(f'result : {result}')
print('result : %.2f' % result)

inum1 = 10
result = inum1 + fnum1
print(f'{inum1} + {fnum1} result : {result}')
print(f'type of result : {type(result)}')
result = inum1 - fnum1
print(f'{inum1} - {fnum1} result : {result}')
print('type of result : {}'.format(type(result)))
result = inum1 * fnum1
print(f'{inum1} * {fnum1} result : {result}')
print('type of result : {}'.format(type(result)))

inum2 = 3
result = inum1 / inum2
print('num1 : {}, num2 : {}'.format(inum1, inum2))
print('result : {}'.format(result))
print('result : %.2f' % result)

# 0으로 나눌 수 없다! 0을 나눗셈하는 경우 결과는 항상 0.0!
num = 0
result = num / inum1
print(f'{num} / {inum1} result : {result}')
# 나눗셈 결과는 항상 float!
inum1 = 20
inum2 = 10
result = inum1 / inum2
print(f'{inum1} / {inum2} result : {result}')
print('type of result : {}'.format(type(result)))

inum1 = 17
inum2 = 4
result = inum1 % inum2 # 나머지
print(f'{inum1} % {inum2} result : {result}')
print('type of result : {}'.format(type(result)))
result = inum1 // inum2 # 몫
print(f'{inum1} // {inum2} result : {result}')
print('type of result : {}'.format(type(result)))

# divmode() 함수는 몫과 나머지를 tuple로 반환한다.
result = divmod(inum1, inum2)
print(type(result))
print('result : {}'.format(result))
print('몫 : {}'.format(result[0]))
print('나머지 : {}'.format(result[1]))

# '**' 거듭제곱 연산자
num1 = 2
num2 = 3
result = num1 ** num2
print(f'num1({num1}) ** num2({num2}) result : {result}')

# '** (1/m)' m제곱근
result = 2 ** (1/2)
print('2의 제곱근 ', result)
result = 2 ** (1/3)
print(f'2의 3제곱근 {result}')
result = 2 ** (1/4)
print('2의 4제곱근 {}'.format(result))

# math 모듈 - pow() / squt()함수는 제곱근만 구할 수 있다.
import math

print('2의 3제곱 %.2f' % math.pow(2, 3))
print(f'2의 4제곱 {math.pow(2, 4):.2f}')
print('2의 5제곱 {:.2f}'.format(pow(2, 5)))

print('2의 제곱근 %f' % math.sqrt(2))
print(f'3의 제곱근 {math.sqrt(3):f}')
print('4의 제곱근 {:f}'.format(math.sqrt(4)))

# 첫 달 200원을 받고 매월 2배씩 인상했을 때 12개월째에 받게되는 용돈은?
firstPocketMoney = 200
after12Month = ((firstPocketMoney * 0.01) ** 12) * 100
print('12개월 후 용돈 : {:d}원'.format(int(after12Month)))
# print(type(after12Month))
after12Month = firstPocketMoney * pow(2, 11)
# format() 함수 결과 콤마(,)가 들어가 문자열이 되므로 다시 정수로 캐스팅할 수 없다!
strResult = format(after12Month, ',')
print('12개월 후 용돈 : %s원' % strResult)


# 문자열 산술 연산 ---------------------------------------------------------------------------------------
# 문자열 덧셈은 가능하나 뺄쎔음 불가능하다!
str1 = 'Good'
str2 = ' '
str3 = 'Morning'
result = str1 + str2 + str3
print(f'result : {result}')
# 문자열 곱셈은 반복 횟수를 의미한다!
str = 'Hello '
result = str * 7
print(f'result : {result}')


