'''
 # [공배수(common multiple)]
 # [최대공배수(the Least/lowest Common Multiple)]
'''

#수 두개의 최소공배수
num1 = int(input('1보다 큰 정수 입력: '))
num2 = int(input('1보다 큰 정수 입력: '))
maxNum = 0

# 둘 중 작은 수만큼만 for문을 돌면 된다.
for i in range(1, (num1 + 1)):
    if num1 % i == 0 and num2 % i == 0:
        print('공약수: {}'.format(i))
        maxNum = i

print('최대공약수: {}'.format(maxNum))

# 최소공배수는 두 수의 곱을 최대공약수로 나눈 몫과 같다.
minNum = (num1 * num2) // maxNum
print('최소공배수: {}'.format(minNum))



# 수 세개의 최소공배수
num1 = int(input('1보다 큰 정수 입력: '))
num2 = int(input('1보다 큰 정수 입력: '))
num3 = int(input('1보다 큰 정수 입력: '))
maxNum = 0

for i in range(1, (num1 + 1)):
    if num1 % i == 0 and num2 % i == 0:
        maxNum = i

print('최대공약수: {}'.format(maxNum))

minNum = (num1 * num2) // maxNum
print('{}, {}의 최소공배수: {}'.format(num1, num2, minNum))


newNum = minNum
for i in range(1, (newNum + 1)):
    if newNum % i == 0 and num3 % i == 0:
        maxNum = i

print('최대공약수: {}'.format(maxNum))

minNum = (newNum * num3) // maxNum
print('{}, {}, {}의 최소공배수: {}'.format(num1, num2, num3, minNum))




ship1 = 3; ship2 = 4; ship3 = 5
maxDay = 0

for i in range(1, (ship1 + 1)):
    if ship1 % i == 0 and ship2 % i == 0:
        maxDay = i

print('최대공약수: {}'.format(maxDay))

minDay = (ship1 * ship2) // maxDay
print('{}, {}의 최소공배수: {}'.format(ship1, ship2, minDay))


newDay = minDay
for i in range(1, (newDay + 1)):
    if newDay % i == 0 and ship3 % i == 0:
        maxDay = i

print('최대공약수: {}'.format(maxDay))

minDay = (newDay * ship3) // maxDay
print('{}, {}, {}의 최소공배수: {}'.format(ship1, ship2, ship3, minDay))

print('{}일마다 모든 선박이 입항합니다.'.format(minDay))



