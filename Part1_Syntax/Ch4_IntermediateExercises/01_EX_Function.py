'''
 # [연습문제] 함수
'''

ex_num = int (input('ex_num: '))

if ex_num == 1:
# <Q> --------------------------------------------------------------------------------------------
# 산술연산 계산기를 함수를 이용해 만들어 보기

    def add(n1, n2):        return n1 + n2

    def sub(n1, n2):        return n1 - n2

    def mul(n1, n2):        return n1 * n2

    def div(n1, n2):        return n1 / n2

    def mod(n1, n2):        return n1 % n2

    def flo(n1, n2):        return n1 // n2

    def exp(n1, n2):        return n1 ** n2


    while True:

        print('-' * 60)
        selectNum = int(input('1.덧셈, 2.뺄셈, 3.곱셈, 4.나눗셈, 5.나머지, 6.몫, 7.제곱승, 8.종료 '))
        if selectNum == 8:
            print('Bye~')
            break

        num1 = float(input('첫 번째 숫자 입력: '))
        num2 = float(input('두 번째 숫자 입력: '))

        if selectNum == 1:
            print(f'{num1} + {num2} = {add(num1, num2)}')

        elif selectNum == 2:
            print(f'{num1} - {num2} = {sub(num1, num2)}')

        elif selectNum == 3:
            print(f'{num1} * {num2} = {mul(num1, num2)}')

        elif selectNum == 4:
            print(f'{num1} / {num2} = {div(num1, num2)}')

        elif selectNum == 5:
            print(f'{num1} % {num2} = {mod(num1, num2)}')

        elif selectNum == 6:
            print(f'{num1} // {num2} = {flo(num1, num2)}')

        elif selectNum == 7:
            print(f'{num1} ** {num2} = {exp(num1, num2)}')

        else:
            print('잘못 입력했습니다. 다시 입력하세요.')

        print('-' * 60)


elif ex_num == 2:
# <Q> --------------------------------------------------------------------------------------------
# 이동거리와 이동시간을 반환하는 함수 만드릭
# 거리(km) = 속도(km/h) * 시간(h)

    # 이동 거리 반환
    def getDistance(speed, hour, minute):
        distance = speed * (hour + (minute / 60))
        return distance

    def convertFloatToMinute(f):
        # 100 : 75 = 60 : x  -->  x = 75 * 60 / 100
        return int(f  * 100 * 60 / 100)

    # 이동 시간 반환
    def getTime(speed, distance):
        time = distance / speed
        print(f'time: {time}')
        h = int(time)
        m = int((time - h) * 60)
        # m = convertFloatToMinute(time - h)

        return [h, m]


    print('-' * 60)
    s = float(input('속도(km/h) 입력: '))
    h = float(input('시간(h) 입력: '))
    m = float(input('시간(m) 입력: '))
    d = getDistance(s, h, m)
    print(f'{s}(km/h)속도로 {h}(h)시간 {m}(m)분 동안 이동한 거리: {d}(km)')
    print('-' * 60)

    print('-' * 60)
    s = float(input('속도(km/h) 입력: '))
    d = float(input('거리(km) 입력: '))
    t = getTime(s, d)
    print(f'{s}(km/h) 속도로 {d}(km) 이동한 시간: {t[0]}(h)시간 {t[1]}(m)분')
    print('-' * 60)


elif ex_num == 3:
# <Q> --------------------------------------------------------------------------------------------
# 비행기 티켓 영수증 출력 함수

    childPrice = 18000
    infantPrice = 25000
    adultPrice = 50000
    specialDC = 50

    def formatedNumber(n):
        return format(n, ',')

    def printAriPlaneReceipt(c1, c2, i1, i2, a1, a2):
        print('=' * 40)
        cp = c1 * childPrice
        cp_dc = int(c2 * childPrice * 0.5)
        print(f' 유아 {c1}명 요금: {formatedNumber(cp)}원')
        print(f' 유아 할인 대상 {c2}명 요금: {formatedNumber(cp_dc)}원')

        ip = i1 * infantPrice
        ip_dc = int(i2 * infantPrice * 0.5)
        print(f' 소아 {i1}명 요금: {formatedNumber(ip)}원')
        print(f' 소아 할인 대상 {i2}명 요금: {formatedNumber(ip_dc)}원')

        ap = a1 * adultPrice
        ap_dc = int(a2 * adultPrice * 0.5)
        print(f' 성인 {a1}명 요금: {formatedNumber(ap)}원')
        print(f' 성인 할인 대상 {a2}명 요금: {formatedNumber(ap_dc)}원')

        print('=' * 40)
        print(f' Total: {formatedNumber(c1 + c2 + i1 + i2 + a1 + a2)}명')
        print(f' TotalPrice : {formatedNumber(cp + cp_dc + ip + ip_dc + ap + ap_dc)}원')
        print('=' * 40)


    print(f'childPrice(24개월 미만)\t\t: {formatedNumber(childPrice)}원')
    print(f'infantPrice(만12세 미만)\t\t: {formatedNumber(infantPrice)}원')
    print(f'adultPrice(만12세 이후)\t\t: {formatedNumber(adultPrice)}원')
    print(f'국가 유공자 및 장애우 할인\t\t: {specialDC}%')
    print()

    childCnt = int(input('유아 입력: '))
    specialDCChildCnt = int(input(f'할인대상 유아 입력: '))

    infantCnt = int(input('소아 입력: '))
    specialDCInfantCnt = int(input(f'할인대상 소아 입력: '))

    adultCnt = int(input('성인 입력: '))
    specialDCAdultCnt = int(input(f'할인대상 성인 입력: '))

    printAriPlaneReceipt(childCnt, specialDCChildCnt,
                         infantCnt, specialDCInfantCnt,
                         adultCnt, specialDCAdultCnt)


elif ex_num == 4:
# <Q> --------------------------------------------------------------------------------------------
# 재귀함수를 이용한 팩토리얼 함수

    def formatedNumber(n):
        return format(n, ',')

    def recursionFun(n):
        if n == 1:
            return n
        return n * recursionFun(n - 1)


    inputNumber = int(input('input number: '))
    inputNumberFormated = formatedNumber(recursionFun(inputNumber))
    print(inputNumberFormated)


elif ex_num == 5:
# <Q> --------------------------------------------------------------------------------------------
# 단리/월복리 계산기 함수

    # 단리 계산기
    def singleRateCalculator(m, t, r):
        totalMoney = 0
        totalRateMoney = 0

        for i in range(t):
            totalRateMoney += m * (r * 0.01)

        totalMoney = m + totalRateMoney
        return int(totalMoney)


    # 월복리 계산기
    def multiRateCalculator(m, t, r):
        t = t * 12 # 연을 월로 환산
        rpm = (r / 12) * 0.01 # rate per month: 연이자를 월이자로 환산
        totalMoney = m

        for i in range(t):
            totalMoney += totalMoney * rpm

        return int(totalMoney)

    def formatedNumber(n):
        return format(n, ',')


    money = int(input('예치금(원): '))
    term = int(input('기간(년): '))
    rate = int(input('연 이율(%): '))

    print()
    print('[단리 계산기]')
    print('=' * 30)
    print(f' 예치금\t: {formatedNumber(money)}원')
    print(f' 예치기간\t: {term}년')
    print(f' 연 이율\t: {rate}%')
    print('-' * 30)
    amount = formatedNumber(singleRateCalculator(money, term, rate))
    print(f' {term}년 후 총 수령액: {amount}원')
    print('=' * 30)

    print()
    print('[월복리 계산기]')
    print('=' * 30)
    print(f' 예치금\t: {formatedNumber(money)}원')
    print(f' 예치기간\t: {term}년')
    print(f' 연 이율\t: {rate}%')
    print('-' * 30)
    amount = formatedNumber(multiRateCalculator(money, term, rate))
    print(f' {term}년 후 총 수령액: {amount}원')
    print('=' * 30)


elif ex_num == 6:
# <Q> --------------------------------------------------------------------------------------------
# 등차 수열(Arithmetic Sequence/Progression)의 n번째 값과 합을 출력하는 함수

    def sequenceCal(n1, d, n):
        valueN = 0
        sumN = 0
        i = 1
        while i <= n:

            if i == 1: # 첫 번째 항의 값 설정
                valueN = n1
                sumN += valueN
                print('{}번째 항의 값: {}'.format(i, valueN))
                print('{}번째 항까지의 합: {}'.format(i, sumN))
                i += 1
                continue

            valueN += d
            sumN += valueN
            print('{}번째 항의 값: {}'.format(i, valueN))
            print('{}번째 항까지의 합: {}'.format(i, sumN))
            i += 1

    # 등차 수열 공식을 이용한 함수
    def sequenceFormula(n1, d, n):
        # 등차 수열(일반항) 공식: an = a1 + (n-1) * d
        valueN = n1 + (n - 1) * d
        print('{}번째 항의 값: {}'.format(n, valueN))

        # 등차 수열(합) 공식: sn = n(a1 + an) / 2
        sumN = n * (n1 + valueN) / 2
        print('{}번째 항까지의 합: {}'.format(n, int(sumN)))


    inputN1 = int(input('a1 입력: '))
    inputD = int(input('공차 입력: ')) # 공차: common difference
    inputN = int(input('n 입력: '))

    sequenceCal(inputN1, inputD, inputN)
    print('-' * 30)
    sequenceFormula(inputN1, inputD, inputN)


elif ex_num == 7:
# <Q> --------------------------------------------------------------------------------------------
# 등비 수열의 n번째 값과 합을 출력하는 함수

    def sequenceCal(n1, r, n):
        valueN = 0
        sumN = 0
        i = 1

        while i <= inputN:

            if i == 1:
                valueN = n1
                sumN += valueN
                print('{}번째 항의 값: {}'.format(i, valueN))
                print('{}번째 항까지의 합: {}'.format(i, sumN))
                i += 1
                continue

            valueN *= r
            sumN += valueN
            print('{}번째 항의 값: {}'.format(i, valueN))
            print('{}번째 항까지의 합: {}'.format(i, sumN))
            i += 1


    def sequenceFormula(n1, r, n):
        # 등비 수열(일반항) 공식: an = a1 * r^(n-1)
        valueN = n1 * (r ** (n - 1))
        print('{}번째 항의 값: {}'.format(n, valueN))

        # 등비 수열(합) 공식: sn = a1 * (1 - r^n) / (1-r)
        sumN = n1 * (1 - (r ** n)) / (1 - r)
        print('{}번째 항까지의 합: {}'.format(n, int(sumN)))


    inputN1 = int(input('a1 입력: '))
    inputR = int(input('공비 입력: ')) # common/geometric ratio
    inputN = int(input('n 입력: '))

    sequenceCal(inputN1, inputR, inputN)
    print('-' * 25)
    sequenceFormula(inputN1, inputR, inputN)




