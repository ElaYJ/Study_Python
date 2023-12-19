'''
# [출력함수] : print() -> 자동 개행(end='\n')된다. 옵션을 바꾸고 싶을 때 end=''를 사용
    ▶ 콤마(,)를 이용한 연속 출력 - 자동으로 '공백'을 구분문자[sep=' ']로 사용
    ▶ 포맷 문자열[f'{}'] 이용 가능
    ▶ 포맷 문자['%d(정수), %f(실수), %s(문자열)'] 이용 가능 - 여러 옵션(소수점 자리수, 오른쪽/왼족 정렬, 콤마 등)으로 사용
    ▶ 포맷 함수['{}'.format()] 이용 가능 - 인덱스 사용
'''

userName = '홍길동'
userAge = 20

# 콤마(,)를 이용한 데이터 연속 출력
print('User name', userName, 'User age', userAge)
print('User name', userName, 'User age', userAge, sep='/')

# 포맷 문자열을 이용한 데이터 출력
print(f'User name : {userName} \nUser age : {userAge}')
print(f'User name\t:\t{userName}\tUser age\t:\t{userAge}')

# 포맷 문자(형식 문자)를 이용한 데이터 출력
print('User nmae : %s' % userName)
print('User age : %d' % userAge)
print('User name : %s, User age : %d' % (userName, userAge))

# format() 함수를 이용한 데이터 출력, index 사용 가능
print('User name : {}, User age : {}'.format(userName, userAge))
print('User age {1}, User name : {0}'.format(userName, userAge))
print('나의 이름은 {0}이고, 나이는 {1}살 입니다. {0} 이름은 아버님께서 지어 주셨습니다.'
      .format(userName, userAge))

pi = 3.1415926535
print("Pi : %f" % pi)
print("Pi : %d" % pi)

print("Pi : %.0f" % pi)
print("Pi : %.2f" % pi)
print("Pi : %.5f" % pi)
print("Pi : %.10f" % pi)

print('3 * 5 = ', end='')
print(3 * 5)

width = 10.5 # float(input('가로 길이 입력 : '))
height = 5.5 # float(input('세로 길이 입력 : '))
triangle = width * height / 2
square = width * height
print(f'width : {width} \nheight : {height}')
print('Triangle : ', triangle, '\nSquare : ', square)

print('width : ', width, ', height : ', height)
print('Triangle : ', triangle, end=', ')
print('Square : ', square)

radius = 3 # float(input('반지름 입력 : '))
pi = 3.141592 # float(input('원주율 입력 : '))
circleArea = pow(radius, 2) * pi

print('반지름 : %.2f' % radius)
print('원주율 : %.2f' % pi)
print('원넓이 : %.2f' % circleArea)