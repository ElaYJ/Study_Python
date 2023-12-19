from time import sleep

class CarRacing:

    def __init__(self):
        self.cars = []
        self.rankings = []

    # 레이싱에 참여하는 자동차 클래스 등록
    def addCar(self, c):
        self.cars.append(c)

    def printCurrentCarDistance(self):
        for car in self.cars:
            #print(f'{car.name}: {car.distance}\t\t', end='')
            print(f'{car}\t\t', end='')
        print()

    def startRacing(self):
        # 10시간 레이싱 후 이동거리가 가장 먼 자동차가 우승이다.
        for i in range(10):
            print(f'Racing {i+1}시간 후 이동거리: ')
            for car in self.cars:
                car.distance += car.getDistanceForHour()

            #sleep(1) # 1초 Delay(프로그램을 잠시 쉬었다 진행)
            self.printCurrentCarDistance()

    def printRanking(self):

        # 정렬 case_1
        # Sorting HOW TO - https://docs.python.org/3/howto/sorting.html
        # self.rankings = sorted(self.cars, key=lambda car: car.distance, reverse=True)
        self.rankings = sorted(self.cars, key=lambda car: -car.distance)
        print(self.rankings)

        i = 1
        for rank in self.rankings:
            if i == 1:  print(type(rank))
            print(f'{i}위: {rank.name}({rank.distance})')
            i += 1

        # 정렬 case_2
        self.cars.sort(key=lambda car: car.distance, reverse=True)
        i = 1
        for car in self.cars:
            if i == 1:
                print(f'{car.name}({car.distance})\t- {i}위 우승!!')
            else:
                print(f'{car.name}({car.distance})\t- {i}위')
            i += 1

