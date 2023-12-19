'''
# [연습문제] 연산자
'''

# 1. ----------------------------------------------------------------------------------------------
# 상품 가격과 지불 금액을 입력하면 거스름 돈을 계산하는 프로그램
# 단, 거스름 돈은 지폐와 동전의 개수를 최소로 하고, 1원 단위는 절사한다.
# 지폐 : 50,000원/ 10,000원/ 5,000원/ 1,000원
# 동전 : 500원/ 100원/ 10원
money50000 = 50000; money10000 = 10000; money5000 = 5000; money1000 = 1000
money500 = 500; money100 = 100; money10 = 10

money50000Cnt = 0; money10000Cnt = 0; money5000Cnt = 0; money1000Cnt = 0
money500Cnt = 0; money100Cnt = 0; money10Cnt = 0

productPrice = 35862 # int(input('상품 가격 입력 : '))
payPrice = 100000 # int(input('지불 금액 : '))
print('상품 가격 입력 : {} \n지불 금액 : {}'.format(productPrice, payPrice))

if payPrice >productPrice:
    change = payPrice - productPrice
    change = (change // 10) * 10
    print('거스름 돈 : {}(원단위 절사)'.format(change, ','))

if change > money50000:
    money50000Cnt = change // money50000
    change %= money50000
if change > money10000:
    money10000Cnt = change // money10000
    change %= money10000
if change > money5000:
    money5000Cnt = change // money5000
    change %= money5000
if change > money1000:
    money1000Cnt = change // money1000
    change %= money1000
if change > money500:
    money500Cnt = change // money500
    change %= money500
if change > money100:
    money100Cnt = change // money100
    change %= money100
if change > money10:
    money10Cnt = change // money10
    change %= money10

print('-' * 30)
print(' 50,000원  {}장'.format(money50000Cnt))
print(' 10,000원  {}장'.format(money10000Cnt))
print('  5,000원  {}장'.format(money5000Cnt))
print('  1,000원  {}장'.format(money1000Cnt))
print('    500원  {}개'.format(money500Cnt))
print('    100원  {}개'.format(money100Cnt))
print('     10원  {}개'.format(money10Cnt))
print('-' * 30, end='\n\n')


# 2. ----------------------------------------------------------------------------------------------
# 국어, 영어, 수학 점수 입력 후 총점, 평균, 최고점수와 과목, 최저점수와 과목,
# 그리고 최고 점수와 최저 점수의 차이를 각각 출력
korScore = 84 # int(input('국어 점수 입력 : '))
engScore = 67 # int(input('영어 점수 입력 : '))
mathScore = 91 # int(input('수학 점수 입력 : '))

totalScore = korScore + engScore + mathScore
avgScore = totalScore / 3
print('총점 : {} \n평균 : {:.2f}'.format(totalScore, avgScore))

# maxScore = korScore; maxSubject = '국어'
# if engScore > maxScore:
#     maxScore = engScore
#     maxSubject = '영어'
# if mathScore > maxScore:
#     maxScore = mathScore
#     maxSubject = '수학'
#
# minScore = korScore; minSugject = '국어'
# if engScore < minScore:
#     minScore = engScore
#     minSubject = '영어'
# if mathScore < minScore:
#     minScore = mathScore
#     minSubject = '수학'
'''
# 'if'문을 사용하면 조건문이 총 4번 수행되데,
# 'if ~ else'문을 사용하면 조건문이 총 2번 수행되도록 할 수 있다.
'''
maxScore = korScore; maxSubject = '국어'
minScore = korScore; minSubject = '국어'

if engScore > maxScore:
    maxScore = engScore
    maxSubject = '영어'
else:
    minScore = engScore
    minSubject = '영어'

if mathScore > maxScore:
    maxScore = mathScore
    maxSubject = '수학'
elif mathScore < minScore:
    minScore = mathScore
    minSubject = '수학'

difScore = maxScore - minScore

print('-' * 30)
print(' 최고 점수 과목(점수) : {}({})'.format(maxSubject, maxScore))
print(' 최저 점수 과목(점수) : {}({})'.format(minSubject, minScore))
print(' 최고, 최저 점수 차이 : {}'.format(difScore))
print('-' * 30, end='\n\n')


# 3. ----------------------------------------------------------------------------------------------
# 시, 분, 초를 입력하면 초로 환산하는 프로그램
hour = 9 # int(input('시간 입력 : '))
minute = 27 # int(input('분 입력 : '))
second = 51 # int(input('초 입력 : '))

print('{}초'.format(format(hour * 60 * 60 + minute * 60 + second, ',')))
print()


# 4. ----------------------------------------------------------------------------------------------
# 금액, 이율, 거치 기간을 입력하면 복리계산하는 복리 계산기 프로그램
depositMoney = 2000000 # int(input('예금 금액 입력(원) : '))
depositRate = 5.1 # float(input('예금 이율 입력(%) : '))
depositTerm = 6 # int(input('예금 기간 입력(년) : '))

resultMoney = depositMoney
for i in range(depositTerm):
    resultMoney += resultMoney * depositRate * 0.01

resultfMoney = format(int(resultMoney), ',') # 3자리마다 콤마를 찍어주는 포맷함수
print('-' * 30)
print(' 이율 : {}%'.format(depositRate))
print(' 원금 : {0:,}원'.format(depositMoney)) # 3자리마다 콤마를 찍어주는 포맷문자
print(' {}년 후 금액 : {}원'.format(depositTerm, resultfMoney))
print('-' * 30, end='\n\n')


# 5. ----------------------------------------------------------------------------------------------
# 고도가 60m 올라갈 때마다 기온이 0.8도 내려 간다는 조건 하에서 (지면 온도 : 29도)
# 고도를 입력했을 때 기온이 출력되는 프로그램 민들기
groundTemp = 29
altStep = 60
stepTemp = 0.8

altitude = 790 # int(input('고도 입력 : '))

# targetAltTemp = groundTemp - ((altitude // altStep) * 0.8)
# if altitude % altStep != 0:
#     targetAltTemp -= stepTemp

# 'divmod()'함수는 결과를 tuple형으로 반환해 주고, 'steps, restAlt ='에서 다음과 같은 형태로 할당해 준다.
# steps: int = (divmod(altitude, altStep))[0], restAlt: int = (divmod(altitude, altStep))[1]
steps, restAlt = divmod(altitude, altStep)
targetAltTemp = groundTemp - (steps * 0.8)
if restAlt != 0:
    targetAltTemp -= stepTemp

print('지면 온도 : {} ℃'.format(groundTemp))
print('고도 {}m의 기온 : {} ℃'.format(altitude, targetAltTemp))
print()


# 6. ----------------------------------------------------------------------------------------------
# 197개의 빵과 152개의 우유를 17명의 학생들한테 동일하게 나눠 준다고 할 때,
# 한 명의 학생이 갖게 되는 빵과 우유의 개수를 구하고 남는 빵과 우유의 개수를 출력
bread = 197
milk = 152
studentCnt = 17

milkResult = divmod(milk, studentCnt)

print('학생 한명이 갖게되는 빵 개수 : {}'.format(bread // studentCnt))
print('학생 한명이 갖게되는 우유 개수 : {}'.format(milkResult[0]))
print('남은 빵의 개수 : {}'.format(bread % studentCnt))
print('남은 우유의 개수 : {}'.format(milkResult[1]))
print()


# 7. ----------------------------------------------------------------------------------------------
# 다음 내용을 참고해서 백신 접종 대상자를 구분하기 위한 프로그램 만들기
# 의사코드(프로그래밍 코드를 일상에서 쓰는 자연어로 표현한 것)
# >>   19세 이하 또는 65세 이상 이면
#           출생 연도 끝자리에 따른 접종
#      그렇지 않으면
#           하반기 일정 확인
age = 13 # int(input('나이 입력 : '))

if age <= 19 or age >= 65:
    birthYear = 0 # int(input('출생 연도 끝자리 입력 : '))

    if birthYear == 1 or birthYear == 6:
        print('월요일 접종 가능!!')
    elif birthYear == 2 or birthYear == 7:
        print('화요일 접종 가능!!')
    elif birthYear == 3 or birthYear == 8:
        print('수요일 접종 가능!!')
    elif birthYear == 4 or birthYear == 9:
        print('목요일 접종 가능!!')
    elif birthYear == 5 or birthYear == 0:
        print('금요일 접종 가능!!')

else:
    print('하반기 일정을 확인하세요.')
print()


# 8. ----------------------------------------------------------------------------------------------
# 길이(mm)를 입력하면 inch로 환산하는 프로그램 만들기 (1mm = 0.039)
byInch = 0.039
lengthMM = 580 # int(input('길이(mm) 입력 : '))
lengthInch = lengthMM * byInch

print('{}mm -> {}inch'.format(lengthMM, lengthInch))

