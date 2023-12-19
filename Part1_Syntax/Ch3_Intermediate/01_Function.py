'''
# [함수] : 수학의 함수와 동일한 역할을 한다. 함수는 곧 '기능'
    ▶ 함수 사용 목적은 특정 기능을 계속 반복적으로 재사용하기 위해함이다. -> 함수의 목적 : 기능 재사용
    ▶ 내장 함수 : python 내부에 기본적으로 정의되어 있는 함수,
                 파이썬을 설치하면 기본적으로 사용 가능한 함수들
    ▶ 사용자 정의 함수
    ▶ 외부 함수(Module)
'''

# 내장 함수 =====================================================================================
# print(), input(), List method, ...

numbers = [2, 5, 1, 4, 3]
print(f'numbers : {numbers}')

numbers.sort()
print(f'numbers : {numbers}')
numbers.reverse()
print(f'numbers : {numbers}')
numbers.clear()
print(f'numbers : {numbers}')
print()


# 사용자 정의 함수 ===============================================================================
# 함수 선언(정의) : 함수는 'def' Keyword, 함수명, ':', 들여쓰기를 이용해 선언한다.
# 'pass' Keyword를 사용해 실행문을 생략할 수 있다.
def PrintUserName(name):
    print(f'{name}고객님, 안녕하세요.')

# 함수 호출 : 함수명과 '()'를 이용해 함수를 호출한다.
PrintUserName('홍길동')
print()

# <Q> ----------------------------------------------------------------------------------------
# 정수 두 개를 입력하면 곱셈과 나눗셈 연산 결과를 출력하는 함수를 만들고 호출
# def CalFunc():
#     n1 = int(input('n1 입력 : '))
#     n2 = int(input('n2 입력 : '))
#
#     print(f'n1 * n2 = {n1 * n2}')
#     print(f'n1 / n2 = {round(n1 / n2, 2)}')
#     # round() 함수로 반올림하여 소수점 둘째 자리까지만 표현
#
# CalFunc() # 1, 3
# CalFunc() # 10, 5
# CalFunc() # 3, 8
# print()

# 함수 내에서 또 다른 함수 호출 -----------------------------------------------------------------
def Func1():
    print('Func1 호출!')
    Func2()
    print('Func2 호출 후에 실행!')
def Func2():
    print('Func2 호출!')
    Func3()
def Func3():
    print('Func3 호출!')

Func1()
print()

# <Q> ----------------------------------------------------------------------------------------
# 구구단(multiplication table) 출력 함수가 연쇄적으로 호출되도록 함수를 선언
def MultiTable2():
    for i in range(1, 10):
        print('2 * {} = {: >2}'.format(i, 2 * i))

    MultiTable3()

def MultiTable3():
    for i in range(1, 10):
        print('3 * {} = {: >2}'.format(i, 3 * i))

    MultiTable4()

def MultiTable4():
    for i in range(1, 10):
        print('4 * {} = {: >2}'.format(i, 4 * i))

    MultiTable5()

def MultiTable5():
    for i in range(1, 10):
        print('5 * {} = {: >2}'.format(i, 5 * i))

    MultiTable6()

def MultiTable6():
    for i in range(1, 10):
        print('6 * {} = {: >2}'.format(i, 6 * i))

    MultiTable7()

def MultiTable7():
    for i in range(1, 10):
        print('7 * {} = {: >2}'.format(i, 7 * i))

    MultiTable8()

def MultiTable8():
    for i in range(1, 10):
        print('8 * {} = {: >2}'.format(i, 8 * i))

    MultiTable9()

def MultiTable9():
    for i in range(1, 10):
        print('9 * {} = {: >2}'.format(i, 9 * i))

# MultiTable2()
print()


# 인수, 매개변수 =================================================================================
# 인수(Argument) : 함수 호출 시 함수로 넘겨주는 데이터
# 매개변수(Parameter) : 함수 선언 시 정의하는 넘겨받을 데이터
# 인수와 매개변수는 함수가 주고 받는 값으로 쌍을 이루어야 하므로 개수 항상 일치해야 한다.
def AddCalculate(x, y): # 매개변수
    print(f'{x} + {y} = {x + y}')

AddCalculate(3, 4) # 인수

# 매개변수의 개수가 정해지지 않은 경우 '*'(asterisk)를 이용한다.
def PrintNumber(*numbers):
    # print(type(numbers)) # <class 'tuple'>
    for num in numbers:
        print(num, end=' ')
    print()

PrintNumber()
PrintNumber(1)
PrintNumber(1, 2)
PrintNumber(1, 2, 3)
PrintNumber(1, 2, 3, 4)
PrintNumber(1, 2, 3, 4, 5)
print()

# <Q> ----------------------------------------------------------------------------------------
# 국어, 영어, 수학 점수를 입력받고, 입력받은 점수를 이용하여 총점과 평균을 출력하는 함수
def PrintScore(kor, eng, math):
    sum = kor + eng + math
    avg = sum / 3

    print(f'총점: {sum}')
    print(f'평균: {round(avg, 2)}')

korScore = 85 # int(input('국어 점수 입력: '))
engScore = 92 # int(input('영어 점수 입력: '))
matScore = 79 # int(input('수학 점수 입력: '))
PrintScore(korScore, engScore, matScore)
print()


# 실행 결과 반환 =================================================================================
# 'return' Keyword를 사용해 함수 실행 결과를 호출부로 반환할 수 있다.
# 함수 실행문 내에서 'return'을 만나면 함수 실행이 종료된다. 함수가 'return'을 만나면 실행을 종료한다.
def AddCal(n1, n2):
    return n1 + n2

print(AddCal(3, 9))

returnValue = AddCal(20, 10)
print(f'returnValue: {returnValue}')

# 'return' - 함수 실행 종료 후 실행 결과 반환
def DivideNumber(n):
    if n % 2 == 0:
        return '짝수'
    else:
        return '홀수'

returnValue = DivideNumber(5)
print(f'returnValue: {returnValue}')

# <Q> ----------------------------------------------------------------------------------------
# 사용자가 길이(cm)를 입력하면 mm로 환산한 값을 반환하는 함수
def CmToMm(cm):
    result = cm * 10
    return result

length = 10.5 # float(input('길이(cm) 입력: '))
returnValue = CmToMm(length)
print(f'{length}cm -> {returnValue}mm')

# <Q> ----------------------------------------------------------------------------------------
# 1부터 100까지의 정수 중 홀수인 난수를 반환하는 함수
import random

def GetOddRandomNumber():
    cnt = 0
    while True:
        cnt += 1
        rNum = random.randint(1, 100)
        if rNum % 2 != 0:
            break
    return [rNum, cnt]

print(GetOddRandomNumber())
# print(f'Get Odd Number({GetOddRandomNumber()[1]}): {GetOddRandomNumber()[0]}')
# 함수가 2번 각각 실행되므로 세트 결과값이 아니다.!!
# index 기호를 쓸꺼면... '(GetOddRandomNumber())[1]' 형태로
count, result = GetOddRandomNumber()
# count: Any = (GetOddRandomNumber())[0]
# result: Any = (GetOddRandomNumber())[1]  형태로 수행됨
print(f'Get Odd Number({count}): {result}')
print()


# 전역변수와 지역변수 =============================================================================
# 전역변수 : 함수 밖에 선언된 변수로 어디에서나 사용은 가능하지만 함수 안에서 수정할 수는 없다.
# 'global' Keyword를 사용하면 함수 내에서도 전역변수의 값을 수정할 수 있다.
num_out = 10
def PrintOutNumber():
    # 지역변수(함수 밖에 있는 num_out과 이름은 같지만 전혀 다른 함수 내 지역변수로 새로 선언된 것이다.!)
    num_out = 20
    print(f'num_out: {num_out}')

PrintOutNumber()
print(f'num_out: {num_out}')

def PrintGlobalNumber():
    global num_out # 함수 밖에 있는 전역변수 num_out을 사용하겠다는 선언! 수정할 수 있는 권한이 생긴다.
    #print(f'num_global: {num_out}')
    num_out = 100
    print(f'num_global: {num_out}')

PrintGlobalNumber()
print(f'num_out: {num_out}')

# 지역변수 : 함수 안에 선언된 변수로 함수 내에서만 사용 가능하다.
def PrintInNumber():
    num_in = 20
    print(f'num_in: {num_in}')

PrintInNumber()
#print(f'num_in: {num_in}')
# -> NameError: name 'num_in' is not defined

# <Q> ----------------------------------------------------------------------------------------
# 가로, 세로 길이를 입력 받아 삼각형, 사각형 넓이를 출력하는 함수
def PrintArea():
    # 지역변수
    triangleArea = width * height / 2
    squareArea = width * height

    print(f'삼각형 넓이: {triangleArea}')
    print(f'사각형 넓이: {squareArea}')

# 전역변수를 먼저 정의하고 함수를 실행하므로 OK~!
width = 12 # int(input('가로 길이 입력: '))
height = 11 # int(input('세로 길이 입력: '))
PrintArea()

# <Q> ----------------------------------------------------------------------------------------
# 방문객 수를 카운트하는 함수
totalVisit = 0
def CountTotalVisit():
    global  totalVisit
    totalVisit += 1
    print(f'누적 방문객수: {totalVisit}')

CountTotalVisit()
CountTotalVisit()
CountTotalVisit()
CountTotalVisit()
CountTotalVisit()
print()


# 중첩함수 ======================================================================================
# 함수 안에 또 다른 함수가 있는 형태
# 내부 함수는 함수 내에서만 사용가능! 함수 밖에서는 호출할 수 없다.
def OutFunc():
    print('Out Function Called!!')

    def InnerFunc():
        print('In Function Called~!')

    InnerFunc()

OutFunc()
InnerFunc()
# -> NameError: name 'InFunc' is not defined

# <Q> ----------------------------------------------------------------------------------------
# 사칙연산을 선택할 수 있는 계산기 함수
def Calculator(n1, n2, operator):
    def AddCal():
        print(f'{n1} + {n2} = {round(n1 + n2, 2)}')
    def SubCal():
        print(f'{n1} - {n2} = {round(n1 - n2, 2)}')
    def MulCal():
        print(f'{n1} * {n2} = {round(n1 * n2, 2)}')
    def DivCal():
        print(f'{n1} / {n2} = {round(n1 / n2, 2)}')

    if operator == 1:
        AddCal()
    elif operator == 2:
        SubCal()
    elif operator == 3:
        MulCal()
    elif operator == 4:
        DivCal()

num1 = 3.2 # float(input('실수(n1) 입력: '))
num2 = 2 # float(input('실수(n2) 입력: '))
while True:
    operatorNum = int(input('1.덧셈, 2.뺄셈, 3.곱셈, 4.나눗셈, 5.종료\n실행 Num: '))

    if operatorNum == 5:
        print('Bye~')
        break

    Calculator(num1, num2, operatorNum)

