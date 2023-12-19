'''
 # [연습문제] 텍스트 파일 입출력
'''

ex_num = int (input('ex_num: '))
uri = 'D:/pythonTxt/EX/'

if ex_num == 1:
# <Q> --------------------------------------------------------------------------------------------
# 회원 계정별 텍스트 파일을 생성한 후 회원 본인 파일에 '한 줄 일기'를 쓰고 읽는 프로그램

    import file_module_Diary as diary

    members = {} # {key(id):value(pw)}


    def printMembers():
        for m_id in members.keys():
            print(f'ID: {m_id} \t PW: {members[m_id]}')


    while True:

        selectNum = int(input('1.회원가입,\t 2.한줄일기쓰기,\t 3.한줄일기보기,\t 4.종료 '))

        if (selectNum == 1):
            mId = input('input ID: ')
            mPw = input('input PW: ')
            members[mId] = mPw
            printMembers()

        elif (selectNum == 2):
            mId = input('input ID: ')
            mPw = input('input PW: ')

            if mId in members and members[mId] == mPw:
                print(f'login success!!')
                fileName = 'myDaiary_' + mId + '.txt'
                data = input('오늘 하루 인상 깊은 일을 기록하세요. ')
                diary.writeDiary(uri, fileName, data)

            else:
                print('login fail!!')
                printMembers()

        elif (selectNum == 3):
            mId = input('input ID: ')
            mPw = input('input PW: ')

            if mId in members and members[mId] == mPw:
                print('login success!!')
                fileName = 'myDaiary_' + mId + '.txt'
                datas = diary.readDiary(uri, fileName)
                for d in datas:
                    print(d, end='') # 이중개행 방지

            else:
                print('login fail!!')
                printMembers()

        elif (selectNum == 4):
            print('Bye~')
            break



elif ex_num == 2:
# <Q> --------------------------------------------------------------------------------------------
# 텍스트 파일에 수입과 지출을 기록하는 가계부 만들기
# 잔액 관리를 위해 수입과 지출의 이력을 관리하는 파일과 별도로 현재 잔고만 따로 기록할 파일을 만든다.
# 수입과 지출의 이력을 관리하는 파일을 읽을 때 한행씩 읽어 오므로 잔액만 가져오기 어렵다.

    import time

    limitSpendMoney = 2000


    def getTime():
        lt = time.localtime()
        st = time.strftime('%Y-%m-%d %H:%M:%S')
        return st

    def fNum(n):    return format(n, ',')

    # 입금 실행시 파일이 없으면 Error!가 나므로 while문 들어가기 전에 파일부터 만들고 시작!
    with open(uri + 'bank_money.txt', 'w') as f:
        f.write('0')
    # Test를 위해 입출금 이력도 초기화가 필요!
    with open(uri + 'pocketMoneyRegister.txt', 'w') as f:
        f.write('')

    while True:

        selectNumber = int(input('1.입금 \t 2.출금 \t 3.로그출력 \t 4.종료 '))

        if selectNumber == 1:
            money = int(input('입금액 입력: '))
            # 현재 잔고를 가져온다.
            with open(uri + 'bank_money.txt', 'r') as f:
                m = f.read()
            # 현재 잔고에 입금액을 더해서 다시 기록한다.
            # 'w'모드로 기존 내용을 갱신해서 기록한다
            with open(uri + 'bank_money.txt', 'w') as f:
                f.write(str(int(m) + money))

            # 입출금 내역은 별도 파일로 관리
            memo = input('입금 내역 입력: ')
            with open(uri + 'pocketMoneyRegister.txt', 'a') as f:
                f.write('--------------------------------\n')
                f.write(f' {getTime()} \n')
                f.write(f' [입금] {memo} : {fNum(money)}원 \n')
                f.write(f' [잔액] {fNum(int(m) + money)}원 \n')

            print('입금 완료!!')
            print('-' * 25)
            print(f' 기존 잔액 : {fNum(int(m))}')
            print(f' 입금 후 잔액 : {fNum(int(m) + money)}')
            print('-' * 25)


        elif selectNumber == 2:
            money = int(input('출금액 입력: '))
            with open(uri + 'bank_money.txt', 'r') as f:
                m = f.read()

            with open(uri + 'bank_money.txt', 'w') as f:
                f.write(str(int(m) - money))

            memo = input('출금 내역 입력: ')
            with open(uri + 'pocketMoneyRegister.txt', 'a') as f:
                f.write('--------------------------------\n')
                f.write(f' {getTime()} \n')
                f.write(f' [출금] {memo} : {fNum(money)}원 \n')
                f.write(f' [잔액] {fNum(int(m) - money)}원 \n')

            print('출금 완료!!')
            print('-' * 25)
            print(f' 기존 잔액 : {fNum(int(m))}')
            print(f' 출금 후 잔액 : {fNum(int(m) - money)}')
            print('-' * 25)

        elif selectNumber == 3:
            with open(uri + 'pocketMoneyRegister.txt', 'r') as f:
                data = f.readlines()
                for d in data:
                    print(d.strip('\n'))
                print('--------------------------------\n')

        elif selectNumber == 4:
            print('Bye~')
            break

        else:
            print('잘못 입력하셨습니다.')



elif ex_num == 3:
# <Q> --------------------------------------------------------------------------------------------
# 사용자가 입력한 숫자의 약수를 텍스트 파일에 기록

    # 약수
    inputNumber = int(input("0보다 큰 정수 입력: "))

    divisor = []
    for number in range(1, (inputNumber + 1)):
        if inputNumber % number == 0:
            divisor.append(number)

    if len(divisor) > 0:
        try:
            with open(uri + 'divisor.txt', 'a') as f:
                f.write(f'{inputNumber}의 약수: ')
                f.write(f'{divisor}\n')

        except Exception as e:
            print(e)

        else:
            print('divisor write complete!')


elif ex_num == 4:
# <Q> --------------------------------------------------------------------------------------------
# 사용자가 입력한 숫자까지의 소수를 텍스트 파일에 기록

    # 소수
    inputNumber = int(input("0보다 큰 정수 입력: "))

    prime = []
    for number in range(2, (inputNumber + 1)):
        flag = True
        for n in range(2, number):
            if number % n == 0:
                flag = False
                break

        if (flag):
            prime.append(number)

    if len(prime) > 0:
        try:
            with open(uri + 'prime.txt', 'a') as f:
                f.write(f'{inputNumber}까지의 소수: ')
                f.write(f'{prime}\n')

        except Exception as e:
            print(e)

        else:
            print('prime write complete!')




elif ex_num == 5:
# <Q> --------------------------------------------------------------------------------------------
# 두 개의 수를 입력하면 공약수를 텍스트 파일에 작성

    # 수 두개의 공약수
    num1 = int(input('1보다 큰 정수 입력: '))
    num2 = int(input('1보다 큰 정수 입력: '))

    common = []
    for i in range(1, (num1 + 1)):
        if num1 % i == 0 and num2 % i == 0:
            common.append(i)

    if len(common) > 0:
        try:
            with open(uri + 'common2.txt', 'a') as f:
                f.write(f'{num1}와 {num2}의 공약수: ')
                f.write(f'{common}\n')

        except Exception as e:
            print(e)

        else:
            print('common factor write complete!')

    # 수 세개의 공약수
    num1 = int(input('1보다 큰 정수 입력: '))
    num2 = int(input('1보다 큰 정수 입력: '))
    num3 = int(input('1보다 큰 정수 입력: '))

    common = []
    for i in range(1, (num1 + 1)):
        if num1 % i == 0 and num2 % i == 0 and num3 % i == 0:
            common.append(i)

    if len(common) > 0:
        try:
            with open(uri + 'common3.txt', 'a') as f:
                f.write(f'{num1}, {num2}, {num3}의 공약수: ')
                f.write(f'{common}\n')

        except Exception as e:
            print(e)

        else:
            print('common factor write complete!')


elif ex_num == 6:
# <Q> --------------------------------------------------------------------------------------------
# 두 개의 수를 입력하면 최대공약수를 텍스트 파일에 작성

    # 수 두개의 최대공약수
    num1 = int(input('1보다 큰 정수 입력: '))
    num2 = int(input('1보다 큰 정수 입력: '))
    maxComNum = 0

    for i in range(1, (num1 + 1)):
        if num1 % i == 0 and num2 % i == 0:
            maxNum = i

    try:
        with open(uri + 'maxComNum2.txt', 'a') as f:
            f.write(f'{num1}와 {num2}의 최대공약수: {maxNum}\n')

    except Exception as e:
        print(e)

    else:
        print('max common factor write complete!')


    # 수 세개의 최대공약수
    num1 = int(input('1보다 큰 정수 입력: '))
    num2 = int(input('1보다 큰 정수 입력: '))
    num3 = int(input('1보다 큰 정수 입력: '))
    maxComNum = 0

    for i in range(1, (num1 + 1)):
        if num1 % i == 0 and num2 % i == 0 and num3 % i == 0:
            maxComNum = i

    try:
        with open(uri + 'maxComNum3.txt', 'a') as f:
            f.write(f'{num1}, {num2}, {num3}의 최대공약수: {maxComNum}\n')

    except Exception as e:
        print(e)

    else:
        print('max common factor write complete!')



elif ex_num == 7:
# <Q> --------------------------------------------------------------------------------------------
# 섬마을에 과일, 생선, 야채를 판매하는 배가 다음 주기로 입항한다고 할 때,
# 모든 배가 입항하는 날짜를 텍스트 파일에 기록
# (첫 입항일은 2023년 1월 1일 오전 10시로 한다.)

    ship1 = 3; ship2 = 4; ship3 = 5 # 주기
    maxDay = 0  # 최대공약수

    for i in range(1, (ship1 + 1)):
        if ship1 % i == 0 and ship2 % i == 0:
            maxDay = i
    print('{}, {}의 최대공약수: {}'.format(ship1, ship2,maxDay))

    minDay = (ship1 * ship2) // maxDay
    print('{}, {}의 최소공배수: {}'.format(ship1, ship2, minDay))


    newDay = minDay
    for i in range(1, (newDay + 1)):
        if newDay % i == 0 and ship3 % i == 0:
            maxDay = i
    print('{}, {}, {}의 최대공약수: {}'.format(ship1, ship2, ship3, maxDay))

    minDay = (newDay * ship3) // maxDay
    print('{}, {}, {}의 최소공배수: {}'.format(ship1, ship2, ship3, minDay))

    print('{}일마다 모든 선박이 입항합니다.'.format(minDay))

# MyCode --------------------------------------
    min_val = min(ship1, ship2, ship3)
    print(min_val)

    gcd = 0
    for i in range(1, min_val + 1):
        if ship1 % i == 0 and ship2 % i == 0 and ship3 % i == 0:
           gcd = i

    lcm = (ship1 * ship2 * ship3) // (gcd ** 2)

    print(gcd, lcm)
# ---------------------------------------------------

    from datetime import datetime
    from datetime import timedelta

    n = 1
    # 첫입항일 세팅
    baseTime = datetime(2023, 1, 1, 10, 0, 0)
    # baseTime = datetime.now()

    print(f'<2021년 모든 선박 입항일>\n {baseTime}')
    with open(uri + 'ship_arrive.txt', 'w') as f:
        f.write(f'2023년 모든 선박 입항일\n')
        f.write(f'{baseTime}\n')

    nextTime = baseTime + timedelta(days=minDay)
    while True:

        print(f' {nextTime}')
        with open(uri + 'ship_arrive.txt', 'a') as f:
            f.write(f'{nextTime}\n')

        nextTime = nextTime + timedelta(days=minDay)
        if nextTime.year > 2023:
            break

# MyCode --------------------------------------
    with open(uri + 'ship_arrive.txt', 'a') as f:
        f.write(f'2023년 모든 선박 입항일\n')
        f.write(f'{baseTime}\n')

        nextTime = baseTime + timedelta(days=lcm)
        while nextTime.year == 2023:
            f.write(f'{nextTime}\n')
            nextTime += timedelta(days=lcm)
# ------------------------------------------------
    with open(uri + 'ship_arrive.txt', 'a') as f:
        print(f'2023년 모든 선박 입항일', file=f)
        print(f'{baseTime}', file=f)

        nextTime = baseTime + timedelta(days=lcm)
        while nextTime.year == 2023:
            print(f'{nextTime}', file=f)
            nextTime += timedelta(days=lcm)
