'''
 # [연습문제] 예외처리
'''

ex_num = int (input('ex_num: '))

if ex_num == 1:
# <Q> --------------------------------------------------------------------------------------------
# 사용자가 입력한 숫자를 이용해서 산술연산 결과를 출력하는 모듈을 만들고,
# 예상하는 예외에 대한 예외처리 코드 작성

    import module_Calculator as cc

    num1 = input('첫 번째 피연산자 입력: ')
    num2 = input('두 번째 피연산자 입력: ')

    cc.add(num1, num2)
    cc.sub(num1, num2)
    cc.mul(num1, num2)
    cc.div(num1, num2)
    cc.mod(num1, num2)
    cc.flo(num1, num2)
    cc.exp(num1, num2)


elif ex_num == 2:
# <Q> --------------------------------------------------------------------------------------------
# 1 ~ 1000까지의 소수인 난수 10개를 생성하되, 소수가 아니면 사용자 예외가 발생하는 프로그램

    import random
    import module_Prime as pm

    primeNumbers = []

    n = 0
    cnt = 0
    while n < 10:

        rn = random.randint(2, 100)
        if rn not in primeNumbers:
            cnt += 1

            try:
                pm.isPrime(rn)

            except pm.NotPrimeException as e:
                print(e)
                continue

            except pm.PrimeException as e:
                print(e)
                primeNumbers.append(rn)

        else:
            cnt += 1
            print(f'{rn} is overlap number.')
            continue

        n += 1

    print(f'<{cnt}번 실행> PrimeNumbers: {primeNumbers}')


elif ex_num == 3:
# <Q> --------------------------------------------------------------------------------------------
# 상품 구매에 따른 '총 구매 금액'을 출력하되, 개수가 잘못 입력된 경우 별도로 출력하는 프로그램

    import module_CalculatePurchase as cp

    g1Cnt = input('goods1 구매 개수: ')
    g2Cnt = input('goods2 구매 개수: ')
    g3Cnt = input('goods3 구매 개수: ')
    g4Cnt = input('goods4 구매 개수: ')
    g5Cnt = input('goods5 구매 개수: ')

    cp.calculate(g1Cnt, g2Cnt, g3Cnt, g4Cnt, g5Cnt)
    cp.myCalculate(g1Cnt, g2Cnt, g3Cnt, g4Cnt, g5Cnt)


elif ex_num == 4:
# <Q> --------------------------------------------------------------------------------------------
# 회원가입 프로그램을 만들되 입력하지 않은 항목이 있을 경우 에러 메시지를 출력하는 프로그램

    import module_Member as mem

    m_name = input('이름 입력: ')
    m_mail = input('메일 주소 입력: ')
    m_pw = input('비밀번호 입력: ')
    m_addr = input('주소 입력: ')
    m_phone = input('연락처 입력: ')

    try:
        #mem.checkInputData(m_name, m_mail, m_pw, m_addr, m_phone)
        newMember = mem.RegisterMember(m_name, m_mail, m_pw, m_addr, m_phone)
        newMember.printMemberInfo()

    except mem.EmptyDataException as e:
        print(e)



elif ex_num == 5:
# <Q> --------------------------------------------------------------------------------------------
# 은행 계좌 계설 및 입/출금 프로그램

    import class_module_Bank as bank

    koreaBank = bank.Bank()

    new_account_name = input('통장 계설을 위한 예금주 입력: ')
    myAccount = bank.PrivateBank(koreaBank, new_account_name)
    myAccount.printBankInfo()

    while True:

        selectNumber = int(input('1.입금, \t2.출금, \t3.종료 '))
        if selectNumber == 1:
            m = int(input('입금액 입력: '))
            koreaBank.doDeposit(myAccount.account_no, m)
            myAccount.printBankInfo()

        elif selectNumber == 2:
            m = int(input('출금액 입력: '))
            try:
                koreaBank.doWithdraw(myAccount.account_no, m)
            except bank.LackException as e:
                print(e)
            finally:
                myAccount.printBankInfo()

        elif selectNumber == 3:
            print('Bye~')
            break

        else:
            print('잘못 입력했습니다. 다시 선택하세요. ')



