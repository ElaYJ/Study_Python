'''
# [연습문제] 데이터와 변수
'''

# 1. ----------------------------------------------------------------------------------------------
# Variable

# '주문확인서' 템플릿을 만들고, 변경되는 정보만 입력하면 '주문확인서'가 완성되는 프로그램
import datetime
today = datetime.datetime.today()
date = datetime.datetime.date(today)
time = datetime.datetime.time(today)

name = '홍길동'
product = '야구글러브'
productPrice = 110000
orderNo = 2568956
payMethod = '신용카드'
payPrice = 100000
usePoint = 10000
payDate = date.strftime('%y/%m/%d') + ' ' + time.strftime('%H:%M:%S')
payDiv = 6
payDivCategory = '무'
phone = '02-1234-5678'

print(name, '고객님 안녕하세요.')
print(name, '고객님의 주문이 완료되었습니다.')
print('다음은 주문건에 대한 상세 내역입니다.')
print('-' * 50)
print(' 상품명\t\t: ', product)
print(' 주문번호\t: ', orderNo)
print(' 결재방법\t: ', payMethod)
print(' 상품금액\t: ', format(productPrice, ','))
print(' 결제금액\t: ', format(payPrice, ','))
print(' 사용포인트\t:  {}p'.format(usePoint))
print(' 결제일시\t: ', payDate)
print(' 할부\t\t:  {}개월'.format(payDiv))
print(' 할부유형\t: ', payDivCategory)
print(' 문의\t\t: ', phone)
print('-' * 50)
print('저희 사이트를 이용해 주셔서 감사합니다.', end='\n\n')


# 2. ----------------------------------------------------------------------------------------------
# 'len()' 함수 : 문자열의 길이를 반환
# 'find()' 함수 : 특정 문자열의 위치를 찾아 Index 위치를 반환

# 사용자가 입력한 데이터의 길이를 출력하는 프로그램 만들기
userMsg = 'Hello, python~' # input('메시지 입력 : ')
print('메시지 문자열 길이 :', len(userMsg))

# 다음 문장에서 '객체지향' 문자열 찾기
# article = '파이썬[2](영어: Python)은 1991년[3] 프로그래머인 귀도 반 로섬[4]이 발표한 고급 프로그래밍 언어로, '\
#           '플랫폼에 독립적이며 인터프리터식, 객체지향적 , 동적 타이핑(dynamically typed) 대화형 언어이다. '\
#           '파이썬이라는 이름은 귀도가 좋아하는 코미디〈Monty Python\'s Flying Circus〉에서 따온 것이다.'
article = '파이썬(영어: Python)은 1991년 프로그래머인 귀도 반 로섬이 발표한 '\
		  '고급 프로그래밍 언어로, 플랫폼에 독립적이며 인터프리터식, 객체지향적, '\
          '동적 타이핑(dynamically typed) 대화형 언어이다. 파이썬이라는 이름은 '\
          '귀도 반 로섬이 좋아하는 코미디〈Monty Python\'s Flying Circus〉에서 따온 것이다.'

strIdx = article.find('객체지향')
print('\'객채지향\' 문자열 위치 :', strIdx)
print()


# 3. ----------------------------------------------------------------------------------------------
# Data Type Casting

# 사용자가 입력한 데이터를 모두 실수로 변경한 후 사각형, 삼각형의 넓이를 출력
width = 7 # float(input('가로 길이 입력 : '))
height = 5 # float(input('세로 길이 입력 : '))

squareArea = width * height
triangleArea = squareArea / 2

print('-' * 12, 'Result', '-' * 12)
print(' 사각형 넓이 : %f' % squareArea)
print(' 삼각형 넓이 : %f' % triangleArea)
print(' 사각형 넓이 : %.2f' % squareArea)
print(' 삼각형 넓이 : %.2f' % triangleArea)
print('-' * 30, end='\n\n')

# 원의 반지름을 입력하면 원의 넓이와 둘레 길이를 [정수, 소수점 한자리, 소수점 셋째자리] 형식으로 출력
radius = 3 # float(input('반지름(cm) 입력 : '))
pi = 3.141592

circleArea = pi * radius * radius
circleLength = 2 * pi * radius

print('원의 넓이 \t : %dcm' % circleArea)
print('원 둘레길이 \t : %dcm' % circleLength)
print('원의 넓이 \t : %.1fcm' % circleArea)
print('원 둘레길이 \t : %.1fcm' % circleLength)
print('원의 넓이 \t : %.3fcm' % circleArea)
print('원 둘레길이 \t : %.3fcm' % circleLength)
print()


# 4. ----------------------------------------------------------------------------------------------
# 'str[0]' : str에 저장된 문자열에서 첫 번재 문자값이다.

# 사용자로부터 입력받은 개인정보를 포맷문자열을 이용해 출력. 단, 비밀번호와 주민번호 뒷자리는 별표로 처리
name = 'hong gil dong' # input('이름 입력 : ')
mail = 'gildong@gmail.com' # input('메일 입력 : ')
userID = 'hongID' # input('아이디 입력 : ')
userPW = '1234567890' # input('비밀번호 입력 : ')
privateNum1 = '840921' # input('주민번호 앞자리 입력 : ')
privateNum2 = '2018543' # input('주민번호 뒷자리 입력 : ')
address = 'korea seoul' # input('주소 입력 : ')

print('-' * 30)
print(f' 이름 : {name}')
print(f' 메일 : {mail}')
print(f' 아이디 : {userID}')
pwStar = '*' * len(userPW)
print(f' 비밀번호 : {pwStar}')
privateNumStar = privateNum2[0] + ('*' * (len(privateNum2) - 1))
print(f' 주민번호 : {privateNum1} - {privateNumStar}')
print(f' 주소 : {address}')
print('-' * 30, end='\n\n')


# 5. ----------------------------------------------------------------------------------------------
# 'isdigit()' 함수 : 숫자인지 확인하여 숫자면 True, 아니면 False를 반환

# 체중(g)과 신장(cm)을 입력하면 BMI지수가 출력되는 프로그램 - BMI = 몸무게(kg) / (신장(m) * 신장(m))
weight = '855' # input('체중 입력(g) : ')
height = '187' # input('신장 입력(cm) : ')

if weight.isdigit():
    weight = int(weight) / 10

if height.isdigit():
    height = int(height) / 100

print('체중 : {}kg'.format(weight))
print('신장 : {}m'.format(height))

bmi = weight / (height * height)
result = ''
if bmi <= 18.5:
    result = '저체중'
elif bmi > 18.5 and bmi <= 23.0:
    result = '정상체중'
elif bmi > 23.0 and bmi <= 25.0:
    result = '과체중'
elif bmi > 25.0 and bmi <= 40.0:
    result = '비만'
elif bmi > 40.0:
    result = '심각한비만'

print('BMI : %.2f -> %s입니다.' % (bmi, result))
print()

# 중간, 기말고사 점수를 입력하면 총점과 평균이 출력되는 프로그램
midScore = '89' # input('중간 고사 점수 : ')
finalScore = '94' # input('기말 고사 점수 : ')

if midScore.isdigit() and finalScore.isdigit():
    midScore = int(midScore)
    finalScore = int(finalScore)

    totalScore = midScore + finalScore
    avgScore = totalScore / 2
    print('총점 : {}, 평균 : {}'.format(totalScore, avgScore))
else:
    print('잘못 입력했습니다.')
print()

# 내 나이가 100살이 되는 해의 연도를 구하는 프로그램
myAge = '43' # input('나이 입력 : ')
curYear = today.year # today = datetime.datetime.today()

print('Today: {}'.format(today.strftime('%y/%m/%d %h:%m:%S')))
print(f'Today: {today.strftime('%y/%m/%d %H:%M:%S')}')

if myAge.isdigit():
    deltaAge = 100 - int(myAge)
    resultYear = curYear + deltaAge
    print('{}년({}년후)에 100살!!'.format(resultYear, deltaAge))
else:
    print('잘못 입력했습니다.')
print()

# 키오스크에서 사용하는 언어를 선택하는 프로그램
langOption = '2' # input('언어 선택(Choose your language : 1.한국어  2.English) : ')

if langOption == '1':
    menu = '1.샌드위치 \t 2.햄버거 \t 3.쥬스 \t 4.커피 \t 5.아이스크림'
elif langOption == '2':
    menu = '1.Sandwich \t 2.Hamburger \t 3.Juice \t 4.Coffee \t 5.Ice cream'

print(menu)

