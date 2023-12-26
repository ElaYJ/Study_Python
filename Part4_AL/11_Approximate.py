'''
 # [근삿값] 특정 값(참값)에 가장 가까운 값
'''


import random

nums = random.sample(range(0, 50), 10)
print(f'nums: {nums}')

inputNum = random.randint(0,49) # int(input('input number: '))
print(f'inputNum: {inputNum}')
nearNum = 0
minNum = 50

for n in nums:
    absNum = abs(n - inputNum)
    print(f'absNum: {absNum}')
    if absNum < minNum:
        minNum = absNum
        nearNum = n

print(f'nearNum: {nearNum}')
print()




import module_approximate as near

# <Q> -----------------------------------------------------------------------------
# 근삿값 알고리즘을 이용해서 시험 점수를 입력하면 학점이 출력되는 프로그램
# 평균 점수에 따른 학점 기준 점수 는 다음과 같다.
# • 95 에 근삿값이면 A 학점
# • 85 에 근삿값이면 B 학점
# • 75 에 근삿값이면 C 학점
# • 65 에 근삿값이면 D 학점
# • 55 에 근삿값이면 F 학점

my_scores = [random.randint(50, 100) for i in range(5)]
print(my_scores)

totalScore = sum(my_scores)
print(f'totalScore: {totalScore}')

avgScore = totalScore / len(my_scores)
print(f'avgScore: {avgScore}')

grade = near.getNearNum(avgScore)
print(f'grade: {grade}')
print()




# <EX> ----------------------------------------------------------------------------
# 근사값 알고리즘을 이용해 수심을 입력하면 수온을 출력하는 모듈
# 다음 표는 수심에 따른 수온을 나타내고 있다.

depth = random.randint(0, 3500) / 100
print(f'float depth: {depth}m')
depth = int(depth)
print(f'int depth: {depth}')

na = near.NearAlgorithm(depth)
temp = na.getNearNumber()
print(f'water temperature: {temp}도')
print()




# <EX> ----------------------------------------------------------------------------
# 사용자의 몸무게(kg) 와 키(m)를 입력하면 체질량지수(BMI)를 계산하고,
# 근삿값 알고리즘과 BMI 표를 이용해 신체 상태를 출력하는 프로그램

uWeight = float(random.randint(40, 100)) #float(input('input weight(Kg): '))
uHeight = float(random.randint(145, 190)/100) #float(input('input height(m): '))
print(f'user weight: {uWeight}kg\nuser height: {uHeight}m')

na = near.BMIAlgorithm(uWeight, uHeight)
na.calculateBMI()
na.printUserCondition()








