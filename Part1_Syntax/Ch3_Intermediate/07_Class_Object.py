'''
 # [객체지향] : Object Oriented Program
    ▶ 현실의 객체 성질을 반영해 프로그램 코드를 짜는 것
    ▶ 객체(Object) = 속성(Attribute) + 기능(Function) : 객체는 속성과 기능으로 구성된다.
    ▶ 객체지향 프로그래밍은 클래스로 구현 가능한다. 클래스로 객체를 찍어낼 수 있다.
    ▶ 객체 사용의 장점(객체지향 프로그래밍을 하는 이유)
        - 코드 재사용과 모듈화에 좋다.
        - 결합도는 낮을수록 좋다.

 # [클래스]
'''

# 클래스 만들기 ==================================================================================
# class Keyword를 이용해 클래스를 선언하고,
# 속성은 변수로 구현하고, 기능은 함수(method)로 구현한다.

# 자동차 클래스
class Car:
    # 생성자는 안보이는 곳에 숨어 있다.

    # 객체 초기화 함수
    def __init__(self, color, length):
        # 속성(변수)
        self.color = color
        self.length = length
    # 기능_1
    def doStop(self):
        print('STOP!!')
    # 기능_2
    def doStart(self):
        print('START!!')
    # 기능_3
    def printCarInfo(self):
        print(f'color: {self.color}')
        print(f'length: {self.length}')
        print()

# 비행기 클래스
class AirPlane:

    def __init__(self, color, length, weight):
        self.color = color
        self.length = length
        self.weight = weight

    def takeOff(self):
        print('take-off')

    def landing(self):
        print('landing')

    def printAriPlaneInfo(self):
        print(f'color: {self.color}')
        print(f'length: {self.length}')
        print(f'weight: {self.weight}')
        print()

# 객체 생성 =====================================================================================
# class Car의 생성자를 호출한다. 생성자는 클래스의 이름과 동일하다.
# 객체는 클래스의 생성자를 호출함으로써 생성된다. 객체는 클래스를 통해 만들어진다.

# 자동차 객체 생성
car1 = Car('red', 200)
car2 = Car('blue', 300)

car1.printCarInfo()
car2.printCarInfo()


# 비행기 객체 생성
airPlane1 = AirPlane('red', 200, 2000)
airPlane2 = AirPlane('blue', 150, 2200)
airPlane3 = AirPlane('green', 180, 2100)
airPlane4 = AirPlane('white', 220, 1900)
airPlane5 = AirPlane('black', 210, 2300)

airPlane1.printAriPlaneInfo()
airPlane2.printAriPlaneInfo()
airPlane3.printAriPlaneInfo()
airPlane4.printAriPlaneInfo()
airPlane5.printAriPlaneInfo()



# 객체 속성값 변경 ===============================================================================

# 클래스 선언
class NewGenerationPC:
    def __init__(self, name, cpu, memory, ssd):
        self.name = name
        self.cpu = cpu
        self.memory = memory
        self.ssd = ssd

    def doExcel(self):
        print('EXCEL RUN!!')

    def doPhotoshop(self):
        print('PHOTOSHOP RUN!!')

    def printPCInfo(self):
        print(f'name: {self.name}')
        print(f'cpu: {self.cpu}')
        print(f'memory: {self.memory}')
        print(f'ssd: {self.ssd}')
        print()

# 객체 생성
myPc = NewGenerationPC('myPC', 'i5', '16G', '256G')
friendPc = NewGenerationPC('friendPC', 'i7', '32G', '512G')

myPc.printPCInfo()
friendPc.printPCInfo()

# 객체 속성값 변경
myPc.cpu = 'i9'
myPc.memory = '64G'
myPc.ssd = '1T'

myPc.printPCInfo()
friendPc.printPCInfo()

# <Q> -----------------------------------------------------------------------------------------
# 계산기 클래스를 만들고 사칙연산을 실행
# 객체를 만들 때 속성값을 주지 않고 객체 생성 후 변수에 접근해 속성값을 변경하여 사칙연산을 수행

class Calculator:

    def __init__(self):
        self.number1 = 0
        self.number2 = 0
        self.result = 0

    def add(self):
        self.result = self.number1 + self.number2
        return self.result

    def sub(self):
        self.result = self.number1 - self.number2
        return self.result

    def mul(self):
        self.result = self.number1 * self.number2
        return self.result

    def div(self):
        self.result = self.number1 / self.number2
        return self.result


calculator = Calculator()
calculator.number1 = 10
calculator.number2 = 20

print(f'calculator.add(): {calculator.add()}')
print(f'calculator.sub(): {calculator.sub()}')
print(f'calculator.mul(): {calculator.mul()}')
print(f'calculator.div(): {calculator.div()}')

calculator.number1 = 3
calculator.number2 = 5

print(f'calculator.add(): {calculator.add()}')
print(f'calculator.sub(): {calculator.sub()}')
print(f'calculator.mul(): {calculator.mul()}')
print(f'calculator.div(): {calculator.div()}')
print()


# 레퍼런스 변수 ================================================================================
# 객체의 메모리 주소를 저장하고 이를 이용해 객체를 참조하는 변수
# 레퍼런스 변수끼리의 대입은 주소만 복사되는 얕은 복사가 이루어진다.

class Robot:

    def __init__(self, color, height, weight):
        self.color = color
        self.height = height
        self.weight = weight

    def printRobotInfo(self):
        print('-' * 20)
        print(f'color: {self.color}')
        print(f'height: {self.height}')
        print(f'weight: {self.weight}')
        print('-' * 20)


rb1 = Robot('red', 200, 80)
rb2 = Robot('blue', 300, 120)
# 얕은 복사 : 객체가 복사된 것이 아니라 객체를 가리키는 주소가 복사된 것!
# 결국 rb3은 rb1과 같은 객체의 주소를 가지고 있어 동일 객체를 가리키고 있다.
rb3 = rb1

rb1.printRobotInfo()
rb2.printRobotInfo()
rb3.printRobotInfo()

rb1.color = 'gray'
rb1.height = 250
rb1.weight = 100

rb1.printRobotInfo()
rb2.printRobotInfo()
rb3.printRobotInfo()

