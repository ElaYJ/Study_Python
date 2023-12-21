'''
 # [근삿값] 특정 값(참값)에 가장 가까운 값
'''


import random

nums = random.sample(range(0, 50), 20)
print(f'nums: {nums}')

inputNum = int(input('input number: '))
print(f'inputNum: {inputNum}')
nearNum = 0
minNum = 50

for n in nums:
    absNum = abs(n - inputNum)
    # print(f'absNum: {absNum}')
    if absNum < minNum:
        minNum = absNum
        nearNum = n

print(f'nearNum: {nearNum}')







# <Q> -----------------------------------------------------------------------------
# 근삿값 알고리즘을 이용해서 시험 점수를 입력하면 학점이 출력되는 프로그램
# 평균 점수에 따른 학점 기준 점수 는 다음과 같다.
# • 95 에 근삿값이면 A 학점
# • 85 에 근삿값이면 B 학점
# • 75 에 근삿값이면 C 학점
# • 65 에 근삿값이면 D 학점
# • 55 에 근삿값이면 F 학점

import module_approximate as near

scores = []

kor = int(input('input kor score: '))
scores.append(kor)
eng = int(input('input eng score: '))
scores.append(eng)
mat = int(input('input mat score: '))
scores.append(mat)
sci = int(input('input sci score: '))
scores.append(sci)
his = int(input('input his score: '))
scores.append(his)

totalScore = sum(scores)
print(f'totalScore: {totalScore}')

avgScore = totalScore / len(scores)
print(f'avgScore: {avgScore}')

grade = near.getNearNum(avgScore)
print(f'grade: {grade}')





# <EX> ----------------------------------------------------------------------------
# 근사값 알고리즘을 이용해 수심을 입력하면 수온을 출력하는 모듈
# 다음 표는 수심에 따른 수온을 나타내고 있다.

#import nearMod

depth = int(float(input('input depth: ')))
print(f'depth: {depth}m')

na = near.NearAlgorithm(depth)
temp = na.getNearNumber()
print(f'water temperature: {temp}도')





# <EX> ----------------------------------------------------------------------------
# 사용자의 몸무게(kg) 와 키(m)를 입력하면 체질량지수(BMI)를 계산하고,
# 근삿값 알고리즘과 BMI 표를 이용해 신체 상태를 출력하는 프로그램

#import nearMod

uWeight = float(input('input weight(Kg): '))
uHeight = float(input('input height(m): '))

na = near.BmiAlgorithm(uWeight, uHeight)
na.calculatorBMI()
na.printUserCondition()








