'''
# [람다함수]
    ▶ 'lambda' Keyword를 사용하면 함수 선언을 보다 간단하게 할 수 있다.
    ▶ 형식 : 함수명 = lambda 매개변수: 실행문 or 결과값 = (lambda 매개변수: 실행문)(인수)
'''
def AddCalculate(x, y): # 매개변수
    return  x + y

returnVal = AddCalculate(3, 4) # 인수
print(f'returnValue: {returnVal}')

Calculator = lambda x, y: x + y
returnVal = Calculator(3, 4)
print(f'returnValue: {returnVal}')

# <Q> ----------------------------------------------------------------------------------------
# 삼격형, 사각형, 원의 넓이를 반환하는 lambda 함수
GetTriangleArea = lambda n1, n2: n1 * n2 / 2
GetSquareArea = lambda n1, n2: n1 * n2
GetCircleArea = lambda r: r * r * 3.14

width = 20 # int(input('가로 길이 입력: '))
height = 30 # int(input('세로 길이 입력: '))
radius = 6 # int(input('반지름 길이 입력: '))

triVal = GetTriangleArea(width, height)
squVal = GetSquareArea(width, height)
cirVal = GetCircleArea(radius)

print(f'삼각형 넓이: {triVal}')
print(f'사각형 넓이: {squVal}')
print(f'원 넓이: {cirVal}')
