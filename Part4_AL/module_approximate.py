# <Q> -----------------------------------------------------------------------------
# 근삿값 알고리즘을 이용해서 시험 점수를 입력하면 학점이 출력되는 프로그램
# 평균 점수에 따른 학점 기준 점수 는 다음과 같다.
# • 95 에 근삿값이면 A 학점
# • 85 에 근삿값이면 B 학점
# • 75 에 근삿값이면 C 학점
# • 65 에 근삿값이면 D 학점
# • 55 에 근삿값이면 F 학점

def getNearNum(an):
    baseScore = [95, 85, 75, 65, 55]
    nearNum = 0
    minNum = 100

    for n in baseScore:
        absNum = abs(n - an)

        if absNum < minNum:
            minNum = absNum
            nearNum = n

    if nearNum == 95:
        return 'A'
    elif nearNum == 85:
        return 'B'
    elif nearNum == 75:
        return 'C'
    elif nearNum == 65:
        return 'D'
    elif nearNum <= 55:
        return 'F'


# <EX> ----------------------------------------------------------------------------
# 근사값 알고리즘을 이용해 수심을 입력하면 수온을 출력하는 모듈
# 다음 표는 수심에 따른 수온을 나타내고 있다.

class NearAlgorithm:

    def __init__(self, d):
        self.temps = {0:24, 5:22, 10:20, 15:16, 20:13, 25:10, 30:6}
        self.depth = d
        self.nearNum = 0
        self.minNum = 24

    def getNearNumber(self):

        for n in self.temps.keys():
            absNum = abs(n - self.depth)
            if absNum < self.minNum:
                self.minNum = absNum
                self.nearNum = n

        print(f'near value: {self.nearNum}')
        return self.temps[self.nearNum]



# <EX> ----------------------------------------------------------------------------
# 사용자의 몸무게(kg) 와 키(m)를 입력하면 체질량지수(BMI)를 계산하고,
# 근삿값 알고리즘과 BMI 표를 이용해 신체 상태를 출력하는 프로그램

class BMIAlgorithm:

    def __init__(self, w, h):
        self.BMISection = {18.5: ['저체중', '정상'],
                           23: ['정상', '과체중'],
                           25: ['과체중', '비만']}
        self.userWeight = w
        self.userHeight = h
        self.userBMI = 0
        self.userCondition = ''
        self.nearNum = 0
        self.minNum = 25

    # BMI = weight / height * height
    def calculateBMI(self):
        self.userBMI = round(self.userWeight / (self.userHeight ** 2), 2)
        print(f'userBMI: {self.userBMI}')

    def printUserCondition(self):
        for n in self.BMISection.keys():
            absNum = abs(n - self.userBMI)
            if absNum < self.minNum:
                self.minNum = absNum
                self.nearNum = n
        print(f'self.nearNum: {self.nearNum}')

        if self.userBMI <= self.nearNum:
            self.userCondition = self.BMISection[self.nearNum][0]
        else:
            self.userCondition = self.BMISection[self.nearNum][1]
        print(f'self.userCondition: {self.userCondition}')


