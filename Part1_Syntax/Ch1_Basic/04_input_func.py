'''
# [입력함수] : input()
    ▶ input() 함수가 반환하는 값은 항상 문자(열) 자료형 'str'이다.
    ▶ split() 함수를 이용해 두 가지 값 이상을 입력 받을 수 있다.
      Default값으로 '공백'이 구문문자로 사용되지만 콤마나 슬래시로 사용하고 싶다면 -> split(,) split(/)
'''

userInputData = 'Hello~' # input('문자형을 입력하세요. ')
print(userInputData)
print(type(userInputData))

userInputData = 13 # input('정수형을 입력하세요. ')
print(userInputData)
print(type(userInputData))

userInputData = 0.17 # input('실수형을 입력하세요. ')
print(userInputData)
print(type(userInputData))

userInputData = True # input('논리형을 입력하세요. ')
print(userInputData)
print(type(userInputData))
print()

Casting
userInputData = input('문자형을 입력하세요. ')
print(userInputData)
print(type(userInputData))

userInputData = int(input('정수형을 입력하세요. '))
print(userInputData)
print(type(userInputData))

userInputData = float(input('실수형을 입력하세요. '))
print(userInputData)
print(type(userInputData))

userInputData = bool(input('논리형을 입력하세요. '))
print(userInputData)
print(type(userInputData))
print()


# <Q> -----------------------------------------------------------------------------------------------
# 사용자로부터 달러, 엔화, 유로, 또는 위안화로 금액을 입력받은 후 이를 원으로 변환하는 프로그램
# 통화별 환율 : 달러-1167 / 엔-1.096 / 유로-1268 / 위안-171
# 사용자는 '100 달러', '1000 엔', '13 유로', '100 위안'과 같이 금액과 통화명 사이에 공백을 넣어 입력한다고 가정
currency_list = {'달러':1167, '엔':1.096, '유로':1268, '위안':171}
userCurr = input('원화로 변환할 금액 입력(단, 금액과 통화단위를 띄어쓰기) : ')

num, currency = userCurr.split()
won = round(float(num) * currency_list[currency])

print('{} -> {:,}원'.format(userCurr, won))

