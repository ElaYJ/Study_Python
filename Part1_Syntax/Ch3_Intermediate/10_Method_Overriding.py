'''
 # [메서드 재정의] : 하위 클래스에서 상위 클래스의 메서드를 재정의(Override)한다.
'''

class Robot:

    def __init__(self, c, h ,w):
        self.color = c
        self.height = h
        self.weight = w

    def fire(self):
        print('총알 발사!!')

    def printRobotInfo(self):
        print(f'color: {self.color}')
        print(f'height: {self.height}')
        print(f'weight: {self.weight}')
        print()


class NewRobot(Robot):

    def __init__(self, c, h ,w):
        super().__init__(c, h, w)

    # 메서드 재정의
    def fire(self):
        super().fire()
        print('레이저 발사!!')

myRobot = NewRobot('blue', 200, 300)
myRobot.printRobotInfo()
myRobot.fire()
print()


# <Q> ---------------------------------------------------------------
# 삼각형 넓이를 계산하는 클래스를 만들고 이를 상속하는 클래스에서 getArea()를
# 오버라이딩해서 출력 결과가 다음과 같을 수 있도록 클래스 만들기

class TriangleArea:

    def __init__(self, w, h):
        self.width = w
        self.height = h

    def printTriangleAreaInfo(self):
        print(f'width: {self.width}')
        print(f'height: {self.height}')

    def getArea(self):
        return self.width * self.height / 2

class NewTriangleArea(TriangleArea):

    def __init__(self, w, h):
        super().__init__(w, h)

    # 메서드 재정의
    def getArea(self):
        return str(super().getArea()) + '㎠'


ta = NewTriangleArea(7, 5)
ta.printTriangleAreaInfo()
triangleArea = ta.getArea()
print(f'TriangleArea: {triangleArea}')
