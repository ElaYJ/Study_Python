'''
 # [재귀] 나 자신을 다시 호출하는 것
 # [하노이의 탑] 파이썬을 이용해서 하노이의 탑 게임 진행 과정을 출력하자
'''

# 반복문 대신 재귀함수를 사용한 예
def recusion(num):

    if num > 0:
        print('*' * num)
        return recusion(num - 1)
    else:
        return 1

recusion(10)


# 재귀함수를 이용한 팩토리얼
def factorial(num):

    if num > 0:
        return num * factorial(num - 1)
    else:
        return 1

print(f'factorial(10): {factorial(10)}')





# <Q> --------------------------------------------------------------------
# 재귀 알고리즘을 이용한 최대공약수 계산
# 유클리드 호제법

# def greatestCommonDevide(n1, n2):
#     maxNum = 0
#     for i in range(1, (n1 + 1)):
#         if n1 % i == 0 and n2 % i == 0:
#             maxNum = i
#
#     return maxNum
#
# print(f'gcd(82, 32): {greatestCommonDevide(82, 32)}')
# print(f'gcd(96, 40): {greatestCommonDevide(96, 40)}')



def gcd(n1, n2):

    if n1 % n2 == 0:
        return n2
    else:
        return gcd(n2, n1 % n2)

print(f'gcd(82, 32): {gcd(82, 32)}')
print(f'gcd(96, 40): {gcd(96, 40)}')



# <EX> ----------------------------------------------------------------------------
# 재귀 알고리즘을 이용한 1월부터 12월까지 전월대비 매출 증감액을 나타내는 프로그램

sales = [12000, 13000, 12500, 11000, 10500, 98000, 91000, 91500, 10500, 11500, 12000, 12500]

def salesUpAndDown(ss):

    if len(ss) == 1:
        return ss

    print(f'sales: {ss}')
    currentSales = ss.pop(0)
    nextSales = ss[0]
    increase = nextSales - currentSales
    if increase > 0:
        increase = '+' + str(increase)
    print(f'매출 증감액: {increase}')

    return salesUpAndDown(ss)

if __name__ == '__main__':
    salesUpAndDown(sales)


# <EX> ----------------------------------------------------------------------------
# 사용자가 정수 두개를 입력하면 작은 정수와 큰 정수 사이의 모든 정수의 합을 구하는 프로그램을
# 재귀 알고리즘을 이용해서 만들기

class NumsSum:

    def __init__(self, n1, n2):
        self.bigNum = 0
        self.smallNum = 0
        self.setN1N2(n1, n2)

    def setN1N2(self, n1, n2):
        self.bigNum = n1
        self.smallNum = n2

        if n1 < n2:
            self.bigNum = n2
            self.smallNum = n1

    def addNum(self, n):
        if n <= 1:
            return n

        return n + self.addNum(n - 1)

    def sumBetweenNums(self):
        return self.addNum(self.bigNum - 1) - self.addNum(self.smallNum)

#import mod

num1 = int(input(f'input number1: '))
num2 = int(input(f'input number2: '))
ns = NumsSum(num1, num2)
result = ns.sumBetweenNums()
print(f'result: {result}')







'''
 # 하노이의 탑
'''

def moveDisc(discCnt, fromBar, toBar, viaBar):                    # 원판 개수, 출발 기둥, 도착 기둥, 경유 기둥
    if discCnt == 1:
        print(f'{discCnt}disc: {fromBar}에서 {toBar}(으)로 이동!')

    else:
        moveDisc(discCnt-1, fromBar, viaBar, toBar)              # (discNo-1)개들을 경유 기둥으로 이동
        print(f'{discCnt}disc: {fromBar}에서 {toBar}(으)로 이동!') # discNo를 목적 기둥으로 이동
        moveDisc(discCnt-1, viaBar, toBar, fromBar)              # (discNo-1)개들을 도착 기둥으로 이동

moveDisc(3, 1, 3, 2)


