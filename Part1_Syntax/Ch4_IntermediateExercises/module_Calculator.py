def add(n1, n2):
    print('덧셈 연산')
    try:
        n1 = float(n1) # 문자가 들어오면 Error~!!
    except:
        print('첫 번째 피연산자는 숫자가 아닙니다.')
        return

    try:
        n2 = float(n2)
    except:
        print('두 번째 피연산자는 숫자가 아닙니다.')
        return

    print(f'{n1} + {n2} = {n1 + n2}')


def sub(n1, n2):
    print('뺄셈 연산')
    try:
        n1 = float(n1)
    except:
        print('첫 번째 피연산자는 숫자가 아닙니다.')
        return

    try:
        n2 = float(n2)
    except:
        print('두 번째 피연산자는 숫자가 아닙니다.')
        return

    print(f'{n1} - {n2} = {n1 - n2}')


def mul(n1, n2):
    print('곱셈 연산')
    try:
        n1 = float(n1)
    except:
        print('첫 번째 피연산자는 숫자가 아닙니다.')
        return

    try:
        n2 = float(n2)
    except:
        print('두 번째 피연산자는 숫자가 아닙니다.')
        return

    print(f'{n1} * {n2} = {n1 * n2}')


def div(n1, n2):
    print('나눗셈 연산')
    try:
        n1 = float(n1)
    except:
        print('첫 번째 피연산자는 숫자가 아닙니다.')
        return

    try:
        n2 = float(n2)
    except:
        print('두 번째 피연산자는 숫자가 아닙니다.')
        return

    # if n2 == 0:
    #     print('0으로 나눌 수 없습니다.')
    #     return
    #
    # print(f'{n1} / {n2} = {n1 / n2}')
    
    try:
        print(f'{n1} / {n2} = {n1 / n2}')
    except ZeroDivisionError as e:
        print(e)
        print('0으로 나눌 수 없습니다.')
    

def mod(n1, n2):
    print('나머지 연산')
    try:
        n1 = float(n1)
    except:
        print('첫 번째 피연산자는 숫자가 아닙니다.')
        return

    try:
        n2 = float(n2)
    except:
        print('두 번째 피연산자는 숫자가 아닙니다.')
        return

    if n2 == 0:
        print('0으로 나눌 수 없습니다.')
        return

    print(f'{n1} % {n2} = {n1 % n2}')


def flo(n1, n2):
    print('몫 연산')
    try:
        n1 = float(n1)
    except:
        print('첫 번째 피연산자는 숫자가 아닙니다.')
        return

    try:
        n2 = float(n2)
    except:
        print('두 번째 피연산자는 숫자가 아닙니다.')
        return

    if n2 == 0:
        print('0으로 나눌 수 없습니다.')
        return

    print(f'{n1} // {n2} = {int(n1 // n2)}')


def exp(n1, n2):
    print('거듭제곱 연산')
    try:
        n1 = float(n1)
    except:
        print('첫 번째 피연산자는 숫자가 아닙니다.')
        return

    try:
        n2 = float(n2)
    except:
        print('두 번째 피연산자는 숫자가 아닙니다.')
        return

    print(f'{n1} ** {n2} = {n1 ** n2}')
