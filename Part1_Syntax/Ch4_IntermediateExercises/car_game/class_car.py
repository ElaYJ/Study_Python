import random

class Car:

    def __init__(self, n='fire car', c='red', s=200):
        self.name = n
        self.color = c
        self.max_speed = s
        self.distance = 0 # 얼마 만큼 이동했는지

    def __repr__(self):
        return repr([self.name, self.distance])
        # TypeError: repr() takes exactly one argument (2 given)
        # repr()함수는 1개의 인수만 받을 수 있으므로 tuple로 묶어 하나로 만들어 준다.

    def printCarInfo(self):
        print(f'name: {self.name}, '
              f'color: {self.color}, '
              f'max_speed: {self.max_speed}')
              #f'current_speed: {self.cur_speed}')

    def controlSpeed(self):
        return random.randint(0, self.max_speed)

    def getDistanceForHour(self):
        return self.controlSpeed() * 1



if __name__ == '__main__':
    tempCar = Car('myCar', 'black', 250)
    tempCar.printCarInfo()
    print(tempCar.controlSpeed())
