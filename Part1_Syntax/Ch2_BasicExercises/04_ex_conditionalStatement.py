'''
# [연습문제] 조건문
'''

# 1. ----------------------------------------------------------------------------------------------
# 교통 과속 위반 프로그램
# carSpeed = int(input('속도 입력 : '))
# limitSpeed = 50
#
# if carSpeed > limitSpeed:
#     print('안전 속도 위반!! 과태료 50,000원 부과 대상입니다.')
#
# if carSpeed <= limitSpeed:
#     print('안전 속도 준수!!')

velocity = 57 # int(input('속도(km/h) 입력 : '))

if velocity > 50:
    print('안전 속도 위반!! 과태료 50,000원 부과 대상입니다.')
else:
    print('안전 속도 준수!!')
print()


# 2. ----------------------------------------------------------------------------------------------
# 문자 메시지(message) 길이에 따라 문자 요금이 결정되는 프로그램
msg = 'Hello~! Nice to meet you. Today, We will learn Python.' \
      'This programing language is easy to Learn. Let\'s start!' # input(')메시지 입력 : ')
lenMsg = len(msg)
msgPrice = 0

if lenMsg > 50:
    msgPrice = 100
    print('MMS 발송!!')
else:
    msgPrice = 50
    print('SMS 발송!!')

print('메시지 : \'{}\''.format(msg))
print('메시지 길이 : {}'.format(lenMsg))
print('메시지 발요 요금 : {}원'.format(msgPrice))
print()


# 3. ----------------------------------------------------------------------------------------------
# 국어 영어 수학 과학 국사 점수를 입력하면 총점을 비롯한 각종 데이터가 출력되는 프로그램
# - 총점, 평균, 편차를 출력 (과목별 평균은 국어:85, 영어:82, 수학:89, 과학:75, 국사:94)
# - 과목별 평균대비 편차 데이터를 막대그래프로 시각화
korAvg = 85; engAvg = 82; matAvg = 89; sciAvg = 75; hisAvg = 94
totalAvg = korAvg + engAvg + matAvg + sciAvg + hisAvg
average = int(totalAvg / 5)

korScore = 95 # int(input('국어 점수 입력 : '))
engScore = 79 # int(input('영어 점수 입력 : '))
matScore = 100 # int(input('수학 점수 입력 : '))
sciScore = 51 # int(input('과학 점수 입력 : '))
hisScore = 67 # int(input('국사 점수 입력 : '))

totalScore = korScore + engScore + matScore + sciScore + hisScore
avgScore = int(totalScore / 5)

korGap = korScore - korAvg
engGap = engScore - engAvg
matGap = matScore - matAvg
sciGap = sciScore - sciAvg
hisGap = hisScore - hisAvg

totalGap = totalScore - totalAvg
avgDeviation = avgScore - average

print('-' * 75)
print(' 총점: {}({:+}), 평균: {}({:+})'.format(totalScore, totalGap, avgScore, avgDeviation))
print(' 국어: {}({:+}), 영어: {}({:+}), 수학: {}({:+}), 과학: {}({:+}), 국사: {}({:+})'.
      format(korScore, korGap, engScore, engGap, matScore, matGap, sciScore, sciGap, hisScore, hisGap))
print('-' * 75)
str = '+' if korGap > 0 else '-'
print(' 국어 편차: {}({:+})'.format(str * abs(korGap), korGap))
str = '+' if engGap > 0 else '-'
print(' 영어 편차: {}({:+})'.format(str * abs(engGap), engGap))
str = '+' if matGap > 0 else '-'
print(' 수학 편차: {}({:+})'.format(str * abs(matGap), matGap))
str = '+' if sciGap > 0 else '-'
print(' 과학 편차: {}({:+})'.format(str * abs(sciGap), sciGap))
str = '+' if hisGap > 0 else '-'
print(' 국사 편차: {}({:+})'.format(str * abs(hisGap), hisGap))
str = '+' if totalGap > 0 else '-'
print(' 총점 편차: {}({:+})'.format(str * abs(totalGap), totalGap))
str = '+' if avgDeviation > 0 else '-'
print(' 평균 편차: {}({:+})'.format(str * abs(avgDeviation), avgDeviation))

deviations = {'국어 편차':korGap, '영어 편차':engGap, '수학 편차':matGap, '과학 편차':sciGap,
              '국사 편차':hisGap, '총점 편차':totalGap, '평균 편차':avgDeviation}

for str, dev in deviations.items():
    bar = '+' if dev > 0 else '-'
    bar *= abs(dev)
    print(' {}: {}({:+})'.format(str, bar, dev))

print('-' * 75, end='\n\n')


# 4. ----------------------------------------------------------------------------------------------
# 난수를 이용해 홀/짝 게임을 만들기
import random

computerNum = random.randint(1, 2)
userSelect = 2 # int(input('홀/짝 선택 (1.홀  2.짝) : '))

if computerNum == 1 and userSelect == 1:
    print('빙고~^^ 홀수!!')
elif computerNum == 2 and userSelect == 2:
    print('빙고~^^ 짝수!!')
elif computerNum == 1 and userSelect == 2:
    print('실패~ㅜㅜ 홀수!!')
elif computerNum == 2 and userSelect == 1:
    print('실패~ㅜㅜ 짝수!!')
print()

# 난수를 이용해 가위, 바위, 보 게임 만들기
computerNum = random.randint(1, 3)
userNum = 1 # int(input('가위,바위,보 선택 (1.가위 \t 2.바위 \t 3.보) : '))

if (computerNum == 1 and userNum == 2) or \
        (computerNum == 2 and userNum == 3) or \
        (computerNum == 3 and userNum == 1) :
    print('컴퓨터 : 패, 유저 : 승')
elif computerNum == userNum :
    print('무승부')
else:
    print('컴퓨터 : 승, 유저 : 패')

print('컴퓨터 : {}, 유저 : {}'.format(computerNum, userNum))
print()


# 5. ----------------------------------------------------------------------------------------------
# 아래 요금표를 참고해서 상수도 요금 계산기 만들기
# │  업종별  │    사용량     │    단가(원)
# --------------------------------------------
# │  가정용  │       -      │      540
# --------------------------------------------
# │         │     50이하    │      820
# │ 대중탕용 │ 50초과 300이하 │    1,920
# │         │    300초과    │    2,400
# --------------------------------------------
# │  공업용  │    500이하    │      240
# │         │    500초과    │      470
businessType = 1 # int(input('업종 선택 (1.가정용 2.대중탕용 3.공업용) : '))
useAmount = 270 # int(input('사용량 입력 : '))
unitPrice = 0; charge = 0

if businessType == 1:
    unitPrice = 540
elif businessType == 2:
    if useAmount > 300:
        unitPrice = 2400
    elif useAmount > 50 and useAmount <= 300:
        unitPrice = 1920
    elif useAmount <= 50:
        unitPrice = 820
elif businessType == 3:
    if useAmount > 500:
        unitPrice = 470
    else:
        unitPrice = 240

charge = unitPrice * useAmount

print('=' * 30)
print(' 상수도 요금표')
print('-' * 30)
print('   사용량 \t│ \t  요금')
print('    {}\t\t│   {:,}원'.format(useAmount, charge))
print('=' * 30, end='\n\n')


# 6. ----------------------------------------------------------------------------------------------
# 미세먼지 비상저감조치로 차량 운행제한 프로그램
# - 미세먼지 특정 수치가 150이하면 차량 5부제 실시 (
# - 미세먼지 특정 수치가 150초과면 차량 2부제 실시 (홀수/짝수로 운행 제한)
# - 차량 2부제를 실시하더라도 영업용 차량은 5부제 실시
# - 미세먼지 수차, 차량 종류, 차량 번호를 입력하면 운행 가능 여부 출력
import datetime

today = datetime.datetime.today()
day = today.day
limitDust = 150

mdFigure = 170 # int(input('미세먼지 수치 입력 : ')) # microdust
carType = 1 # int(input('차량 종류 선택 (1.승용차  2.영업용차) : '))
carNum = 8524 # int(input('차량 번호 입력 : '))

carEndNum = carNum % 10

print('-' * 30)
print('', today)
print('-' * 30)

if mdFigure > limitDust and carType == 1:
    if (day % 2) == (carNum % 2):
        print(' 차량 2부제 적용')
        print(' 차량 2부제로 금일 운행제한 대상 차량입니다.')
    else:
        print(' 금일 운행 가능합니다!!')

if (mdFigure > limitDust and carType == 2) or (mdFigure <= limitDust):
    if (day % 5) == (carNum % 5):
        print(' 차량 5부제 적용')
        print(' 차량 5부제로 금일 운행제한 대상 차량입니다.')
    else:
        print(' 금일 운행 가능합니다!!')

print('-' * 30, end='\n\n')


# 7. ----------------------------------------------------------------------------------------------
# 컴퓨터가 난수를 발생하면 사용가 맞추는 게임
# - PC가 난수(1~1000)를 생성하고 사용자는 숫자(정수)를 입력한다.
# - 사용자가 난수를 맞추면 게임이 종료된다.
# - 만약, 못 맞추면 난수와 사용자 숫자의 크고 작음을 출력한 후 사용자에게 다시 기회를 준다.
# - 최종적으로 사용자가 시도한 횟수를 출력한다.
rNum = random.randint(1, 1000)
tryCnt = 0
gameFlag = True

while gameFlag:
    tryCnt += 1
    userNum = rNum # int(input('1에서 1,000까지의 정수 입력 : '))

    if rNum == userNum:
        print('빙고!')
        gameFlag = False
    else:
        if rNum > userNum:
            print('난수가 크다. Up~!!')
        else:
            print('난수가 작다. Down!')

print('난수 : {}, 시도 횟수 : {}'.format(rNum, tryCnt))
print()


# 8. ----------------------------------------------------------------------------------------------
# 실내온도를 입력하면 스마트에어컨 상태가 자동으로 설정되는 프로그램
#  실내온도   │  18도 이하   18도초과 22도이하   22 < T <= 24   24 < T <= 26   26 < T <= 28   28도 초과
# 에어컨 상태 │     off          매우 약            약              중             강         매우 강
roomTemp = 29 # int(input('실내온도 입력 : '))

if roomTemp <= 18:
    print('에어컨 상태 : OFF!!')
elif roomTemp > 18 and roomTemp <= 22:
    print('에어컨 상태 : 매우 약!!')
elif roomTemp > 22 and roomTemp <= 24:
    print('에어컨 상태 : 약!!')
elif roomTemp > 24 and roomTemp <= 26:
    print('에어컨 상태 : 중!!')
elif roomTemp > 26 and roomTemp <= 28:
    print('에어컨 상태 : 강!!')
elif roomTemp > 28:
    print('에어컨 상태 : 매우 강!!')


