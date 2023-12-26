'''
 # [재귀] 나 자신을 다시 호출하는 것
 # [하노이의 탑] 파이썬을 이용해서 하노이의 탑 게임 진행 과정을 출력
'''
import random


# 반복문 대신 재귀함수를 사용한 예> 별찍기
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
print()




# <Q> --------------------------------------------------------------------
# 유클리드 호제법 : 재귀 알고리즘을 이용한 최대공약수 계산

def greatestCommonDevide(n1, n2):
    maxNum = 0
    for i in range(1, (n1 + 1)):
        if n1 % i == 0 and n2 % i == 0:
            maxNum = i

    return maxNum

print(f'gcd(82, 32): {greatestCommonDevide(82, 32)}')
print(f'gcd(96, 40): {greatestCommonDevide(96, 40)}')


def gcd(n1, n2):

    # 다음 코드는 if n2 == 0: return n1일 때보다
    # 재귀 함수 단계 하나를 낮출수 있다.
    if n1 % n2 == 0:
        return n2
    else:
        return gcd(n2, n1 % n2)

print(f'gcd(82, 32): {gcd(82, 32)}')
print(f'gcd(96, 40): {gcd(96, 40)}')
print()


# [확인코드]
recur_step = 0

def euclidGCD1(n1, n2):
    global recur_step
    recur_step += 1
    print(f'recur_step: {recur_step}')

    if n2 == 0: return n1
    return euclidGCD1(n2, n1%n2)

print(f'euclidGCD1(82, 32): {euclidGCD1(82, 32)}')
print(f'euclidGCD1(96, 40): {euclidGCD1(96, 40)}')

recur_step = 0

def euclidGCD2(n1, n2):
    global recur_step
    recur_step += 1
    print(f'recur_step: {recur_step}')

    if n1 % n2 == 0: return n2
    else:
        return euclidGCD2(n2, n1 % n2)
print(f'euclidGCD2(82, 32): {euclidGCD2(82, 32)}')
print(f'euclidGCD2(96, 40): {euclidGCD2(96, 40)}')
print()



# <EX> ----------------------------------------------------------------------------
# 재귀 알고리즘을 이용해 1월부터 12월까지 전월대비 매출 증감액을 나타내는 프로그램

sales = [12000, 13000, 12500, 11000, 10500, 98000, 91000, 91500, 10500, 11500, 12000, 12500]

def salesUpAndDown(ss):

    if len(ss) == 1:
        print(f'sales: {ss}')
        return ss

    print(f'sales: {ss}')

    currentSales = ss.pop(0) # 12000 [13000, 12500, 11000, 10500, 98000, 91000, 91500, 10500, 11500, 12000, 12500]
    nextSales = ss[0] # 13000
    increase = nextSales - currentSales

    if increase > 0:
        increase = '+' + str(increase)
    print(f'매출 증감액: {increase}\n')

    return salesUpAndDown(ss)

if __name__ == '__main__':
    salesUpAndDown(sales)
    print()


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

    # small_num < sum(nums) < big_num
    # big & small num은 합에 포함되지 X
    # 처음부터 (big_num - 1)까지의 합을 구해서 big_num 제외
    # 처음부터 (small_num)까지의 합을 빼서 small_num을 제외
    def sumBetweenNums(self):
        return self.addNum(self.bigNum - 1) - self.addNum(self.smallNum)

#import mod

num2 = random.randint(1, 50)#int(input(f'input number2: '))
num1 = random.randint(1, 50)#int(input(f'input number1: '))
ns = NumsSum(num1, num2)
result = ns.sumBetweenNums()
print(f'small_num({min(num1, num2)}) < sum_result({result}) < big_num({max(num1, num2)})')
print(sum(range(min(num1, num2)+1, max(num1, num2))))
print()




'''
 # 하노이의 탑
'''
# 원판 개수, 출발 기둥, 도착 기둥, 경유 기둥
def moveDisc(discCnt, fromBar, toBar, viaBar):
    global recur_step

    if discCnt == 1:
        # printA
        print(f'A> {discCnt}개 disc: {fromBar}기둥에서 {toBar}기둥으로 이동!')

    else:
        # (discCnt-1)개들을 경유 기둥으로 이동
        # recurA
        moveDisc(discCnt-1, fromBar, viaBar, toBar)
        print('recurA CLOSE!!')

        # discCnt를 목적 기둥으로 이동
        # printB
        print(f'B> {discCnt}개 disc: {fromBar}기둥에서 {toBar}기둥으로 이동!')

        # (discCnt-1)개들을 도착 기둥으로 이동
        # recurB
        moveDisc(discCnt-1, viaBar, toBar, fromBar)
        print('recurB CLOSE!!')


moveDisc(3, 1, 3, 2)

'''
(3, 1, 3, 2)입력 : 3개의 disc를 1번 기둥에서 3번 기둥으로 옮긴다. 2번 기둥 경유

 -> recurA-1(2, 1, 2, 3) : 2개의 disc를 1번 기둥에서 2번 기둥으로 옮긴다. 3번 기둥 경유
 
    -> recurA-2(1, 1, 3, 2) : 1개의 disc를 1번 기둥에서 3번 기둥으로 옮긴다. 2번 기둥 경유
        ⭐printA : "1개 dice: 1기둥에서 3기둥으로 이동!"
        <recurA-2 CLOSE!!>
        
    ⭐printB: "2개 dice: 1기둥에서 2기둥으로 이동!"
    
    -> recurB-1(1, 3, 2, 1) : 1개의 disc를 3번 기둥에서 2번 기둥으로 옮긴다. 1번 기둥 경우
        ⭐printA : "1개 dice: 3기둥에서 2기둥으로 이동!"
        <recurB-1 CLOSE!!>
        
    <recurA-1 CLOSE!!>
    
 ⭐printB: "3개 dice: 1기둥에서 3기둥으로 이동!"
 
 -> recurB-1(2, 2, 3, 1) : 2개의 disc를 2번 기둥에서 3번 기둥으로 옮긴다. 1번 기둥 경유
 
     -> recurA-2(1, 2, 1, 3) : 1개의 disc를 2번 기둥에서 1번 기둥으로 옮긴다. 3번 기둥 경유
        ⭐printA : "1개 dice: 2기둥에서 1기둥으로 이동!"
        <recurA-2 CLOSE!!>
        
    ⭐printB: "2개 dice: 2기둥에서 3기둥으로 이동!"
    
    -> recurB-1(1, 1, 3, 2) : 1개의 disc를 1번 기둥에서 3번 기둥으로 옮긴다. 2번 기둥 경우
        ⭐printA : "1개 dice: 1기둥에서 3기둥으로 이동!"
        <recurB-1 CLOSE!!>
        
    <recurA-1 CLOSE!!>
    
<시작 함수 종료>
'''
