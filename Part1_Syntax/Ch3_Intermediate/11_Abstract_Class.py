'''
 # [추상 클래스]
    ▶ 상위 추상 클래스는 하위 클래스에게 어떤 특정 메서드에 대한 구현을 강제한다.
    ▶ 하위 클래스에게 특정 메서드를에 대한 구현을 강요하는 클래스를 추상 클래스라고 한다.
    ▶ 추상 클래스는 메서드를 선언만하고 상속하는 하위 클래스가 메서드를 구체화하는 것이다.
    ▶ 고정된 기능이 아니라 상속하는 각자의 클래스에 맞게 알아서 쓰라는 의미!
'''

# 추상 클래스를 선언하기 위한 모듈 2가지
from abc import ABCMeta
from abc import abstractmethod

# 추상클래스
# 비행기의 비행 기능은 민항기나 전투기가 다르므로 각 클래스에 맞게 구현해서 쓰라는 의미!
class AirPlane(metaclass=ABCMeta):

    # 메서드의 이름만 있고 실행부가 없다.
    # 기능에 대한 구체적인 내용이 없는 것~!
    @abstractmethod
    def flight(self):
        pass

    def forward(self):
        print('전진!!')

    def backward(self):
        print('후진!!')


class Airliner(AirPlane):

    def __init__(self, c):
        self.color = c

    def flight(self):
        print('시속 400km/h 비행!!')

# 전투기
class fighterPlane(AirPlane):

    def __init__(self, c):
        self.color = c

    def flight(self):
        print('시속 700km/h 비행!!')


ap1 = Airliner('red')
ap1.flight()
ap1.forward()
ap1.backward()

ap2 = fighterPlane('blue')
ap2.flight()
ap2.forward()
ap2.backward()
print()


# <Q> ---------------------------------------------------------------------------------
# 계산기 추상 클래스를 만들고 이를 이용해서 새로운 계산기 클래스 만들기
# 추상 클래스에는 덧셈, 뺄셈, 곱셈, 나눗셈 기능이 선언되어 있어야 한다.

class Calculator(metaclass=ABCMeta):

    @abstractmethod
    def add(self, n1, n2):
        pass

    @abstractmethod
    def sub(self, n1, n2):
        pass

    @abstractmethod
    def mul(self, n1, n2):
        pass

    @abstractmethod
    def div(self, n1, n2):
        pass


class ChildCalculator(Calculator):

    def add(self, n1, n2):
        print(n1 + n2)

    def sub(self, n1, n2):
        print(n1 - n2)

    def mul(self, n1, n2):
        print(n1 * n2)

    def div(self, n1, n2):
        print(n1 / n2)

childCal = ChildCalculator()
childCal.add(10, 20)
childCal.sub(10, 20)
childCal.mul(10, 20)
childCal.div(10, 20)
print()


class DeveloperCalculator(Calculator):

    def add(self, n1, n2):
        print(n1 + n2)

    def sub(self, n1, n2):
        print(n1 - n2)

    def mul(self, n1, n2):
        print(n1 * n2)

    def div(self, n1, n2):
        print(n1 / n2)

    def mod(self, n1, n2):
        print(n1 % n2)

    def flo(self, n1, n2):
        print(n1 // n2)


devCal = DeveloperCalculator()
devCal.add(10, 20)
devCal.sub(10, 20)
devCal.mul(10, 20)
devCal.div(10, 20)
devCal.mod(10, 20)
devCal.flo(10, 20)
