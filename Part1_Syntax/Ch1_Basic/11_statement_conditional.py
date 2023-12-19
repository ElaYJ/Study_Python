'''
# [조건식] : 'A if 조건식 else B' - 조건식의 결과가 True이면 A를 실행하고, 그렇지 않으면 B를 실행한다.
# [조건문] : 'if문' - 단일조건 / 'if ~ else문' - 양자택일 / 'if ~ elif문' - 다중조건, 다중택일
'''

# 조건식(삼항연산자) : 'A if 조건식 else B' ---------------------------------------------------------------
num1 = 10; num2 = 21
print(f'num1 = {num1}, num2 = {num2}')

result = True if num1 > num2 else False
print('num1 > num2 : {}'.format(result))
print('num1은 num2보다 크다.') if num1 > num2 else print('num1은 num2보다 크지 않다.')

# 입력받은 적설량이 30mm 이상이면 대설 경보를 발령하고 그렇지 않으면 대설 경보를 해제하는 코드 작성
limitSnowAmount = 30
snowAmount = 27 # int(input('적설량 입력(mm) : '))

print('적설량 : {}mm, {}'.format(snowAmount, '대설 경보 발령!!')) if snowAmount >= limitSnowAmount \
    else print('적설량 : {}mm, {}'.format(snowAmount, '대설 경보 해제~'))

alert = '대설 경보 발령!!' if snowAmount >= limitSnowAmount else '대설 경보 해제!!'
print('적설량 : {}mm, {}'.format(snowAmount, alert))

# 국어, 영어, 수학 점수를 입력 받아 과락을 검사하고 평균이 합격인지 검사하는 코드 작성
import operator

subjectPassScore = 60 # 과목별 합격 점수 : 60점
averagePassScore = 70 # 전체 평균 합격 점수 : 70점

korScore = 65 # int(input('국어 점수 : '))
engScore = 80 # int(input('영어 점수 : '))
matScore = 55 # int(input('수학 점수 : '))

totalScore = korScore + engScore + matScore
scoreAvg = totalScore / 3

print('국어 : PASS') if operator.ge(korScore, subjectPassScore) else print('국어 : FAIL')
print('영어 : PASS') if operator.ge(engScore, subjectPassScore) else print('영어 : FAIL')
print('수학 : PASS') if operator.ge(matScore, subjectPassScore) else print('수학 : FAIL')
print('총점 : %d, 평균 : %.2f' % (totalScore, scoreAvg))
print('시험 : PASS') if operator.ge(scoreAvg, averagePassScore) else print('시험 : FAIL')

# 조건식(삼항연산자)의 결과를 변수에 할당하는 경우
min_ablePoint = 100
userPoint = 4500 # int(input('사용자 포인트 입력 : ))
result = '가능' if userPoint >= min_ablePoint else '불가능'
print(f'포인트 사용 가능 여부 : {result}')


# 단일 조건문 : if 조건식: \ >실행문(코드블록) -------------------------------------------------------------
# 코드블럭을 쓸때는 들여쓰기(>)를 해야한다!

# 국어, 영어, 수학 점수를 입력 받고 평균이 90점 이상이면 '참 잘했어요.'를 출력하는 코드
korScore = 95 # int(input('국어 점수 : '))
engScore = 90 # int(input('영어 점수 : '))
matScore = 92 # int(input('수학 점수 : '))

avgScore = (korScore + engScore + matScore) / 3
print('평균 : %f' % avgScore)

if avgScore >= 90:
    print('참 잘했어요~^^')


# 양자택일 조건문 : if 조건식: \ >실행문 \ else: \ >실행문 -------------------------------------------------
passScore = 80
myScore = 99 # int(input('점수 입력 : '))

if myScore >= passScore:
    print('PASS!!')
else:
    print('FAIL!!')

# 'pass' 키워드 - 실행문을 나중에 코딩하겠다!
msgStr = '오늘 어디서 볼래?' # input('문자 메시지 입력 : ')
print('msgString : {}, msgLength : {}'.format(msgStr, len(msgStr)))

if len(msgStr) >= 500:
    pass
else:
    pass

# 소수점 첫 번째 자리에서 반올림하는 프로그램 만들기
fNum = 3.14 # float(input('소수 입력 : '))

if fNum - int(fNum) >= 0.5:
    print('올림 : {}'.format(int(fNum) + 1))
else:
    print('버림 : {}'.format(int(fNum)))

# 모든 조건식(삼항연산자)는 if ~ else문으로 변경 가능!
# BUT, 모든 if ~ else문을 조건식(삼항연산자)로 변경할 수 있는 것은 아니다! 실행문이 2가지 이상일 때 불가능!!

# print('포인트 사용 가능') if userPoint >= min_ablePoint else print('포인트 사용 불가능')
if userPoint >= min_ablePoint:
    print('포인트 사용 가능')
else:
    print('포인트 사용 불가능')

# result = '가능' if userPoint >= min_ablePoint else '불가능'
if userPoint >= min_ablePoint:
    result = '가능'
else:
    result = '불가능'
print('포인트 사용 가능 여부 : {}'.format(result))

# 조건식(삼항연산자)로 변경 불가능한 if ~ else문
min_ablePoint = 1000
userPoint = 850 # int(input('사용자 포인트 입력 : ))
if userPoint >= min_ablePoint:
    result = '가능'
else:
    result = '불가능'
    lackPoint = min_ablePoint - userPoint
    print(f'포인트가 {lackPoint}p 부족합니다.')
print('포인트 사용 가능 여부 : {}'.format(result))


# 다자택일 조건문 : if 조건식: \ >실행문 \ elif 조건식: \ > 실행문 ... --------------------------------------
examScore = 82 # int(input('시험 성적 입력 : '))
grades = ''

if examScore >= 90:
    grades = 'A'
elif examScore >= 80:
    grades = 'B'
elif examScore >= 70:
    grades = 'C'
elif examScore >= 60:
    grades = 'D'
else:
    grades = 'F'

print('성적 : {} \t 학점 : {}'.format(examScore, grades))

# 다자택일을 사용할 때 조건식의 순서가 중요하다.
# 위에서 차례대로 조건을 검사하고 참이면 아래 조건이 Skip되므로 70점 이상은 항상 C학점이 된다.
if examScore >= 70:
    grades = 'C'
elif examScore >= 90:
    grades = 'A'
elif examScore >= 80:
    grades = 'B'
elif examScore >= 60:
    grades = 'D'
else:
    grades = 'F'

print('성적 : {} \t 학점 : {}'.format(examScore, grades))

# 다자택일을 사용할 경우 조건의 범위를 정확하게 명시하는 것이 좋다.
if examScore >= 70 and examScore < 80:
    grades = 'C'
elif examScore >= 90:
    grades = 'A'
elif examScore >= 80 and examScore < 90:
    grades = 'B'
elif examScore >= 60 and examScore < 70:
    grades = 'D'
else:
    grades = 'F'

print('성적 : {} \t 학점 : {}'.format(examScore, grades))

# 키오스크에서 메뉴를 선택하면 영수증이 출력되는 프로그램 만들기
print('1. 카페라떼(3.5) \t 2. 에스프레소(3.0) \t 3. 아메리카노(2.0) \t 4. 곡물라떼(4.0) \t 5. 밀크티(4.3)')
userSelectNum = 3 # int(input('메뉴 선택 : '))

selectMenu = ''
price = 0

if userSelectNum == 1:
    selectMenu = '카페라떼'
    price = 3500
elif userSelectNum == 2:
    selectMenu = '에스프레소'
    price = 3000
elif userSelectNum == 3:
    selectMenu = '아메리카노'
    price = 2000
elif userSelectNum == 4:
    selectMenu = '곡물라떼'
    price = 4000
elif userSelectNum == 5:
    selectMenu = '밀크티'
    price = 4300
else:
    print('메뉴에 없는 번호입니다.')

print('--------------------')
print(' 메뉴 : {} \n 가격 : {}원'.format(selectMenu, format(price, ',')))
print('--------------------')

print('-' * 20)
if userSelectNum == 1:
    print(' 메뉴 : 카페라떼 \n 가격 : 3,500')
elif userSelectNum == 2:
    print(' 메뉴 : 에스프레소 \n 가격 : 3,000')
elif userSelectNum == 3:
    print(' 메뉴 : 아메리카노 \n 가격 : 2,000')
elif userSelectNum == 4:
    print(' 메뉴 : 곡물라떼 \n 가격 : 4,000')
elif userSelectNum == 5:
    print(' 메뉴 : 밀크티 \n 가격 : 4,300')
print('-' * 20)

# 중첩 조건문 -------------------------------------------------------------------------------------------
if examScore < 60:
    print('재시험 대상자입니다.')
else:
    if examScore >= 90:
        print('A')
    elif examScore >= 80:
        print('B')
    elif examScore >= 70:
        print('C')
    elif examScore >= 60:
        print('D')

# 출퇴근 시 이용하는 교통 수단에 따라 세금을 감면해 주는 정책에 맞는 프로그램 만들기
userSelectNum = int(input('출퇴근 대상자 인가요? \n 1.Yes \t 2.No\n'))

if userSelectNum == 1:
    print('교통수단을 선택하세요')
    trans = int(input('1.도보,자전거  2.버스,지하철,  3.자가용\n'))

    if trans == 1:
        print('세금 감면 5%')
    elif trans == 2:
        print('세금 감면 3%')
    elif trans == 3:
        print('추가 세금 1%')

elif userSelectNum == 2:
    print('세금 변동이 없습니다.')
else:
    print('잘못 입력했습니다.')
