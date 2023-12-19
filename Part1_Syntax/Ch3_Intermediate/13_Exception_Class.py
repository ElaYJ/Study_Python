'''
 # [예외 클래스]
    ▶ Exception은 예외를 담당하는 클래스이다.
'''

# Exception Class ==========================================================================
# 파이썬에서 Exception은 예외를 담당하는 클래스로 어떻한 에러가 발생했는지 정보를 알 수 있다.

num1 = 3 #int(input('input numer1: '))
num2 = 0 #int(input('input numer2: '))

try:
    print(f'num1 / num2 = {num1 / num2}')
except:
    print('0으로 나눌 수 없습니다.')

print(f'num1 * num2 = {num1 * num2}')
print(f'num1 - num2 = {num1 - num2}')
print(f'num1 + num2 = {num1 + num2}')


num1 = 7 #int(input('input numer1: '))
num2 = 0 #int(input('input numer2: '))

try:
    print(f'num1 / num2 = {num1 / num2}')
except Exception as e:
    print(f'exception: {e}')

print(f'num1 * num2 = {num1 * num2}')
print(f'num1 - num2 = {num1 - num2}')
print(f'num1 + num2 = {num1 + num2}')


try:
    num1 = 9 #int(input('input numer1: '))
    num2 = 0 #int(input('input numer2: '))
except Exception as e:
    print(f'exception: {e}')
    num1 = 10
    num2 = 20

try:
    print(f'num1 / num2 = {num1 / num2}')
except ZeroDivisionError as e:
    print(f'exception: {e}')

print(f'num1 * num2 = {num1 * num2}')
print(f'num1 - num2 = {num1 - num2}')
print(f'num1 + num2 = {num1 + num2}')



# raise Keyword ==========================================================================
# 강제로 Exception 객체를 생성해서 예외를 발생시키는 키워드

def divCalculator(n1, n2):

    if n2 != 0:
        print(f'{n1} / {n2} = {n1 / n2}')
    else:
        # Exception 객체를 생성해서 임의로 예외를 발생시킴.
        raise Exception('0으로 나눌 수 없습니다.')

num1 = 8 #int(input('input numer1: '))
num2 = 0 #int(input('input numer2: '))

try:
    divCalculator(num1, num2)
except Exception as e:
    print(f'Exception: {e}')


# <Q> --------------------------------------------------------------------------------
# 사용자가 문자 메시지를 보낼 때 10글자 이하면 SMS로 발송하고, 10글자를 초과하면 MMS로 발송하는
# 프로그램을 예외처리를 이용해서 만들기

def sendSMS(msg):

    if len(msg) > 10:
        raise Exception('길이 초과!! MMS전환 후 발송!!', 1)
    else:
        print('SMS 발송!!')

def sendMMS(msg):

    if len(msg) <= 10:
        raise Exception('길이 미달!! SMS전환 후 발송!!', 2)
    else:
        print('MMS 발송!!')


#msg = input('input message: ')
msg = 'HelloHelloHelloHelloHelloHello'

try:
    sendSMS(msg)

except Exception as e:
    print(f'e[0]: {e.args[0]}')
    print(f'e[1]: {e.args[1]}')

    if e.args[1] == 1:
        sendMMS(msg)
    elif e.args[1] == 2:
        sendSMS(msg)


# Exception 사용자 Class ==========================================================================
# Exception Class를 상속해서 사용자 예외 클래스를 직접 만들 수 있다.
# Exception Class를 상속받아야 예외 클래스가 될 수 있다.

# 사용자 예외 클래스
class NotUseZeroException(Exception):

    def __init__(self, n):
        super().__init__(f'{n}은 사용할 수 없습니다!!')

# 예외를 사용자 임의로 발생시키는 함수
def divCalculator(num1, num2):
    if num2 == 0:
        raise NotUseZeroException(num2)
    else:
        print(f'{num1} / {num2} = {num1 / num2}')


num1 = 10 #int(input('input number1: '))
num2 = 0 #int(input('input number2: '))

try:
    divCalculator(num1, num2)
except NotUseZeroException as e:
    print(e)


# <Q> -------------------------------------------------------------------------------------
# 관리자 암호를 입력하고 다음 상태에 따라 예외 처리하는 예외 클래스 말들기
#  - 암호 길이가 5미만인 경우 : PasswordLengthShortException
#  - 암호 길이가 10을 초과하는 경우 : PasswordLengthLongException
#  - 암호가 잘못된 경우 : PasswordWrongExcqtion
#  - 5회 시도할 기회를 준다.

class PasswordLengthShortException(Exception):

    def __init__(self, str):
            super().__init__(f'{str}: 길이 5미만!!')

class PasswordLengthLongException(Exception):

    def __init__(self, str):
            super().__init__(f'{str}: 길이 10초과!!')

class PasswordWrongException(Exception):

    def __init__(self, str):
            super().__init__(f'{str} 잘못된 비밀번호!!')


cnt = 0
while True:

    if cnt == 5:
        print('5회 실패하여 일시 잠금 상태가 됩니다. \n나중에 다시 시도해 주세요.')
        break

    adminPw = input('input admin password: ')

    try:
        if len(adminPw) < 5:
            raise PasswordLengthShortException(adminPw)

        elif len(adminPw) > 10:
            raise PasswordLengthLongException(adminPw)

        elif adminPw != 'admin1234':
            raise PasswordWrongException(adminPw)

        elif adminPw == 'admin1234':
            print('빙고!')
            break

    except PasswordLengthShortException as e1:
        print(e1)

    except PasswordLengthLongException as e2:
        print(e2)

    except PasswordWrongException as e3:
        print(e3)

    cnt += 1

