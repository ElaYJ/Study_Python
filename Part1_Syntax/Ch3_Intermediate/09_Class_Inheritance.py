'''
 # [클래스 상속]
    ▶ 클래스는 다른 클래스를 상속받아 마치 내 것처럼 다른 클래스의 속성과 기능을 사용할 수 있다.
'''

class NormalCar:

    def drive(self):
        print('[NormalCar] drive() called!!')

    def back(self):
        print('[NormalCar] back() called!!')

# 클래스 상속
class TurboCar(NormalCar):

    def turbo(self):
        print('[TurboCar] turbo() called!!')


myTurboCar = TurboCar()
myTurboCar.drive()
myTurboCar.back()
myTurboCar.turbo()
print()


# <Q> -----------------------------------------------------------
# 덧셈, 뺄셈 기능이 있는 클래스를 만들고, 이를 상속하는 클래스를 만들어서
# 곱셈과 나눗셈 기능을 추가한다.

class CalculatorSuper:

    def add(self, n1, n2):
        return n1 + n2

    def sub(self, n1, n2):
        return n1 - n2


class CalculatorChild(CalculatorSuper):

    def mul(self, n1, n2):
        return n1 * n2

    def div(self, n1, n2):
        return n1 / n2

cal = CalculatorChild()

print(f'cal.add(10, 20): {cal.add(10, 20)}')
print(f'cal.sub(10, 20): {cal.sub(10, 20)}')
print(f'cal.mul(10, 20): {cal.mul(10, 20)}')
print(f'cal.div(10, 20): {cal.div(10, 20)}')
print()



# 클래스 생성자 ===========================================================================
# __init__() 메소드가 속성을 초기화 한다.
# 객체가 생성될 때 생성자를 호출(클래스명 명시)하면 초기화 함수인 __init__()가 자동 호출된다.
class EmptyCalculator:

    def __init__(self):
        print('[EmptyCalculator] __init__() called!!\n')

cal = EmptyCalculator()

class Calculator:

    def __init__(self, n1, n2):
        print('[Calculator] __init__() called!!')
        self.num1 = n1
        self.num2 = n2

# 매개변수로 초기화하는 방법도 있지만,
cal = Calculator(10, 20)
print(f'cal.num1: {cal.num1}')
print(f'cal.num2: {cal.num2}')
print()

# 클래스 선언 시 Default 값을 지정해 주어 객체가 생성될 때 항상 고정값으로 만들어질 수도 있다.
class DefaultCalculator:

    def __init__(self):
        print('[DefaultCalculator] __init__() called!!')
        self.num1 = 11
        self.num2 = 100

cal = DefaultCalculator()
print(f'cal.num1: {cal.num1}')
print(f'cal.num2: {cal.num2}')
print()


# 기능 메소드는 상속만 하면 하위 클래스가 바로 사용할 수 있지만,
# 속성값은 __init__() 메소드가 호출이 되어야만 초기화가 이루어지므로
# 상위 클래스의 __init__() 메소드를 반드시 호출해 주어야 한다.
class P_Class:

    def __init__(self, pNum1, pNum2):
        print('[pClass] __init__()')

        self.pNum1 = pNum1
        self.pNum2 = pNum2


class C_Class(P_Class):

    def __init__(self, cNum1, cNum2):
        print('[cClass] __init__()')

        # 상위 클래스의 속성을 초기화하기 위해
        # 부모 클래스의 __init__() 메소드를 강제로 호출하는 방법이 있고,
        P_Class.__init__(self, 100, 200)

        # super() 함수로 부모 클래스의 __init__() 메소드를 호출할 수도 있다.
        # super() 함수를 사용할 경우 'self' Keyword는 생략한다.
        super().__init__(100, 200)

        self.cNum1 = cNum1
        self.cNum2 = cNum2


cls = C_Class(10, 20)

print(f'cls.cNum1: {cls.cNum1}')
print(f'cls.cNum2: {cls.cNum2}')

print(f'cls.pNum1: {cls.pNum1}')
print(f'cls.pNum2: {cls.pNum2}')
print()


# < Q > ------------------------------------------------------------------------------
# 중간고사 클래스와 기말고사 클래스를 상속관계로 만들고 각각의 점수를 초기화한다.
# 그리고 총점과 평균을 반환하는 기능도 만들어 본다.

class MiddleExam:

    def __init__(self, s1, s2, s3):
        print('[MidExam] __init__()')

        self.mid_kor_score = s1
        self.mid_eng_score = s2
        self.mid_mat_score = s3

    def printScores(self):
        print(f'mid_kor_score: {self.mid_kor_score}')
        print(f'mid_eng_score: {self.mid_eng_score}')
        print(f'mid_mat_score: {self.mid_mat_score}')

class FinalExam(MiddleExam):

    def __init__(self, s1, s2, s3, s4, s5, s6):
        print('[EndExam] __init__()')

        super().__init__(s1, s2, s3)

        self.end_kor_score = s4
        self.end_eng_score = s5
        self.end_mat_score = s6

    def printScores(self):
        super().printScores()
        print(f'end_kor_score: {self.end_kor_score}')
        print(f'end_eng_score: {self.end_eng_score}')
        print(f'end_mat_score: {self.end_mat_score}')

    def getTotalScore(self):
        total = self.mid_kor_score + self.mid_eng_score + self.mid_mat_score
        total += (self.end_kor_score + self.end_eng_score + self.end_mat_score)

        return total

    def getAverageScore(self):
        return self.getTotalScore() / 6


exam = FinalExam(85, 90, 88, 75, 85, 95)
exam.printScores()
print(f'Total: {exam.getTotalScore()}')
print(f'Average: {round(exam.getAverageScore(), 2)}')
print()


# 다중 상속 ===============================================================================
# 2개 이상의 클래스를 상속
# 다중 상속은 남발하면 안된다.!!! 다중 상속의 늪에 빠질 수 있다.
# 동일한 이름의 메서드가 있는 경우 원칙상 가장 먼저 상속 받는 클래스의 메서드를 호출하지만
# 개발자 입장에서는 중복되는 코드가 있으면 헷갈릴 수 있다.

class Car01:
    def drive(self):
        print('drive() method called!!')

class Car02:
    def turbo(self):
        print('turbo() method called!!')

class Car03:
    def fly(self):
        print('fly() method called!!')

class Car(Car01, Car02, Car03):

    def __int__(self):
        pass

myCar = Car()

myCar.drive()
myCar.turbo()
myCar.fly()
print()


# <Q> --------------------------------------------------------------------
# BasicCalculator와 DeveloperCalculator 클래스를 만들고 이들 클래스를 상속해서
# 나만의 Calulator 클래스를 만들고 사용해 보자.

class BasicCalculator:

    def add(self, n1, n2):
        return n1 + n2

    def sub(self, n1, n2):
        return n1 - n2

    def mul(self, n1, n2):
        return n1 * n2

    def div(self, n1, n2):
        return n1 / n2

class DeveloperCalculator:

    def mod(self, n1, n2):
        return n1 % n2

    def flo(self, n1, n2):
        return n1 // n2

    def exp(self, n1, n2):
        return n1 ** n2


class Calculator(BasicCalculator, DeveloperCalculator):

    def __int__(self):
        pass


myCal = Calculator()
print(f'myCal.add(10, 20): {myCal.add(10, 20)}')
print(f'myCal.sub(10, 20): {myCal.sub(10, 20)}')
print(f'myCal.mul(10, 20): {myCal.mul(10, 20)}')
print(f'myCal.div(10, 20): {myCal.div(10, 20)}')

print(f'myCal.mod(10, 3): {myCal.mod(10, 3)}')
print(f'myCal.flo(10, 3): {myCal.flo(10, 3)}')
print(f'myCal.exp(10, 3): {myCal.exp(10, 3)}')

