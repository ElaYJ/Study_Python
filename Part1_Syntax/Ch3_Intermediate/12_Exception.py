'''
 # [예외처리] : 예상하지 못한 예외가 프로그램 전체에 영향이 없도록 처리하는 것!
    ▶ 예외란, 문법적인 문제는 없으나 실행 중 발생하는 예상하지 못한 문제이다.
      (에러는 소프트웨어적으로 처리하고 해결할 수 없는 문제이다.
       ex> Syntax나 Network 문제 혹은 전기나 천재지변 등)
    ▶ 예외에러마다 담당하는 다양한 클래스가 있다.
    ▶ 이 예외 관련 클래스들은 모두 Exception Class를 상속하고 있다.
    ▶ 발생된 예외를 별도로 처리함으로써 프로그램 전체의 실행에 문제가 없도록 하는 것이 바로 예외처리이다.
'''

# 예외 발생 ====================================================================================

def add(n1, n2):
    print(n1 + n2)

def sub(n1, n2):
    print(n1 - n2)

def mul(n1, n2):
    print(n1 * n2)

def div(n1, n2):
    print(n1 / n2)


firstNum = int(input('first number: '))     # 10
secondNum = int(input('second number: '))   # 0 -> ZeroDivisionError 발생!

add(firstNum, secondNum)
sub(firstNum, secondNum)
mul(firstNum, secondNum)
div(firstNum, secondNum)
'''
# 위 코드는 문법적으로 문제없이 실행되지만 사용자가 두번째 피연산자로 '0'을 입력함으로써
# 예상하지 못했던 문제가 발생하게 되는데 이를 '예외'라고 한다.
'''

# ZeroDivisionError: division by zero
#print(10 / 0)

# ValueError: invalid literal for int() with base 10: 'Hello'
#int('Hello')

# IndexError: list index out of range
tempList = [1, 2, 3, 4, 5]
print(tempList[0])
print(tempList[1])
print(tempList[2])
print(tempList[3])
print(tempList[4])
#print(tempList[5])

# IndentationError: unexpected indent
if 10 <= 20:
    print('result: ', end='')
        #print('10 <= 20')

# FileNotFoundError: [Errno 2] No such file or directory: 'c:/python/test.txt'
#file = open('c:/python/test.txt', 'r')



# 예외 처리 ====================================================================================
# try ~ except 키워드
# 예외 발생 예상 구문을 try ~ except 키워드로 감싸서 처리한다.
# 정확하게 예외가 발생할 것같은 구문만 감싸야 한다.
# try는 예외가 발생하는 순간 바로 예외를 except로 던저버리므로 아래 구문이 실행되지 못하기 때문이다.
try:
    print(10 / 0)
except:
    print('예외 발생!! 예외 확인 하세요.')


n1= 10; n2 = 0

#print(n1 / n2) # 예외 에러 발생
print(n1 * n2)
print(n1 - n2)
print(n1 + n2)


n1= 10; n2 = 0
# 예외 처리
try:
    print(n1 / n2)
except:
    print('예상치 못한 예외가 발생했습니다.')
    print('다른 프로그램 실행에는 문제 없습니다.')

print(n1 * n2)
print(n1 - n2)
print(n1 + n2)

# <Q> ---------------------------------------------------------------------------------------
# 사용자로부터 숫자 5개를 입력받을 때 숫자가 아닌 자료형이 입력되면 예외 처리하는 프로그램

nums = []
print(id(nums))

n = 1
while n < 6:
    try:
        num = int(input('input number: '))
    except:
        print('예외 발생!')
        continue # 5개를 다 받을 때까지 실행

    nums.append(num)
    n += 1

print(f'nums: {nums}')


# else Keyword ================================================================================
# 예외가 발생하지 않은 경우 실행하는 구문이다.
nums = []
print(id(nums))

n = 1
while n < 6:

    try:
        num = int(input('input number: '))

    except:
        print('예외 발생')
        continue

    else:
        if num % 2 == 0:
            nums.append(num)
            n += 1

        else:
            print('입력한 숫자는 홀수 입니다.', end='')
            print('다시 입력 하세요.')
            continue

print(f'nums: {nums}')

# <Q> ------------------------------------------------------------------------------------
# 사용자로부터 숫자 5개를 입력받아 짝수, 홀수, 실수로 구분해서 각각을 리스트에 저장하는 프로그램
# 군집합에서 분류로 자주 사용하는 코드이므로 잘 기억해 둘 것!!!

eveList = [];
oddList = [];
floatList = []

n = 1
while n < 6:

    try:
        num = float(input('input number: '))

    except:
        print('exception raise!!')
        print('input number again!!')
        continue

    else:

        if num - int(num) != 0:
            print('float number!')
            floatList.append(num)
        else:
            if num % 2 == 0:
                print('even number!')
                eveList.append(int(num))

            else:
                print('odd number')
                oddList.append(int(num))

        n += 1

print(f'eveList: {eveList}')
print(f'oddList: {oddList}')
print(f'floatList: {floatList}')


# finally Keyword ==============================================================================
# 예외 발생과 상관없이 항상 실행하는 구문이다.

# 예외가 발생하는지 감시 : 예외가 발생하면 예외를 except로 던짐
try:
    inputData = input('input number: ')
    numInt = int(inputData)
# 예외가 발생하면 실행
except:
    print('exception raise!!')
    print('not number!!')
    numInt = 0
# 예외가 발생하지 않으면 실행 : 짝/홀수 구분
else:
    if numInt % 2 == 0:
        print('inputData is even number!!')
    else:
        print('inputData is odd number!!')
# 예외 발생과 상관없이 항상 실행
finally:
    print(f'inputData: {inputData}')

# <Q> ----------------------------------------------------------------------------------
# 사용자로부터 숫자 5개를 입력받아 짝수, 홀수, 실수와 입력한 모든 데이터를 각각 출력하는 프로그램

eveList = []; oddList = []; floatList = []
dataList = []

n = 1
while n < 6:

    try:
        data = input('input number: ')
        floatNum = float(data)

    except:
        print('exception raise!!')
        print('input number again!!')
        continue

    else:

        if floatNum - int(floatNum) != 0:
            print('float number!')
            floatList.append(floatNum)
        else:
            if floatNum % 2 == 0:
                print('even number!')
                eveList.append(int(floatNum))

            else:
                print('odd number')
                oddList.append(int(floatNum))

        n += 1

    finally:
        dataList.append(data)


print(f'eveList: {eveList}')
print(f'oddList: {oddList}')
print(f'floatList: {floatList}')
print(f'dataList: {dataList}')

