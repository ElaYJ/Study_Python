'''
# [연습문제] 반복문
'''

# 1. ----------------------------------------------------------------------------------------------
# 1부터 100까지 정수 중 십의자리(tenth digit, tens)와 일의자리(one digit)에 대해 각각 홀/짝수를 구분하는 프로그램

for i in range(1, 101):
    if i < 10:
        if i % 2 == 0:
            print(f'[{i}] : 짝수!')
        else:
            print(f'[{i}] : 홀수!')
    else:
        # num01 = i % 10
        # num10 = i // 10
        tenDigit, oneDigit = divmod(i, 10)

        result10 = ''
        if tenDigit % 2 == 0:
            result10 = '짝수!!'
        else:
            result10 = '홀수!!'

        result01 = '0'
        if oneDigit != 0:
            if oneDigit % 2 == 0:
                result01 = '짝수!!'
            else:
                result01 = '홀수!!'

        print(f'[{i}] 십의자리: {result10}, 일의자리: {result01}')
print()


# 2. ----------------------------------------------------------------------------------------------
# 1부터 사용자가 입력한 정수까지의 합, 홀수의 합, 짝수의 합, 그리고 팩토리얼을 출력하는 프로그램
num = 10 # int(input('정수 입력 : '))
addsum = 0; oddSum = 0; evenSum = 0
factorial = 1

for i in range(1, num + 1):
    addsum += i

    if i % 2 != 0:
        oddSum += i
    else:
        evenSum += i

    factorial *= i

print('전체 합의 결과 : {:,}'.format(addsum))
print('홀수 합의 결과 : {:,}'.format(oddSum))
print('짝수 합의 결과 : {:,}'.format(evenSum))
print('팩토리얼({}!) 결과 : {:,}'.format(num, factorial))
print()


# 3. ----------------------------------------------------------------------------------------------
# '*'을 이용해 모양 출력

for i in range(1, 6):           # │ *
    for j in range(i):          # │ **
        print('*', end='')      # │ ***
    print()                     # │ ****
print()                         # │ *****

#---------------------------------------------

for i in range(1, 6):
    for j1 in range(5 - i):     # │     *
        print(' ', end='')      # │    **
    for j2 in range(i):         # │   ***
        print('*', end='')      # │  ****
    print()                     # │ *****
print()

for i in range(1, 6):
    space = ' ' * (5 - i)
    star = '*' * (i)
    print(space + star)
print()

#---------------------------------------------

for i in range(5, 0, -1):       # │ *****
    for j in range(i):          # │ ****
        print('*', end='')      # │ ***
    print()                     # │ **
print()                         # │ *

#---------------------------------------------

for i in range(5, 0, -1):
    for j1 in range(5 - i):     # │ *****
        print(' ', end='')      # │  ****
    for j2 in range(i):         # │   ***
        print('*', end='')      # │    **
    print()                     # │     *
print()

for i in range(1, 6):
    for j in range(i - 1):
        print(' ', end='')
    for j in range(6 - i):
        print('*', end='')
    print()
print()

for i in range(5, 0, -1):
    space = ' ' * (5 - i)
    star = '*' * (i)
    print(space + star)
print()

#---------------------------------------------

for i in range(1, 10):              # │ *
    if i < 5:                       # │ **
        for j in range(i):          # │ ***
            print('*', end='')      # │ ****
    else:                           # │ *****
        for j in range(10 - i):     # │ ****
            print('*', end='')      # │ ***
    print()                         # │ **
print()                             # │ *

#---------------------------------------------

for i in range(1, 6):
    for j in range(1, 6):           # │ *
        if j == i:                  # │  *
            print('*', end='')      # │   *
        else:                       # │    *
            print(' ', end='')      # │     *
    print()
print()

for i in range(1, 6):
    space = ' ' * (i - 1)
    print(space + '*')
print()

#---------------------------------------------

for i in range(1, 6):
    for j in range(5, 0, -1):       # │     *
        if j == i:                  # │    *
            print('*', end='')      # │   *
        else:                       # │  *
            print(' ', end='')      # │ *
    print()
print()

for i in range(1, 6):
    space = ' ' * (5 - i)
    print(space + '*')
print()

#---------------------------------------------
for i in range(1, 6):           # │ *
    for j in range(i):          # │ **
        print('*', end='')      # │ ***
    print()                     # │ ****
print()                         # │ *****

#---------------------------------------------

for i in range(1, 6):
    for j1 in range(5 - i):
        print(' ', end='')
    for j2 in range (i * 2 - 1): # 별은 홀수개로 찍는다. 1, 3, 5, 6, 9
        print('*', end='')
    print()
for i in range(1, 6):
    for j1 in range(i - 1):
        print(' ', end='')
    for j2 in range(11 - (i * 2)):
        print('*', end='')
    print()
print()
'''
     *
    ***
   *****
  *******
 *********
 *********
  *******
   *****
    ***
     *    
'''
for i in range(1, 10):
    if i <= 5: # 1 ~ 5
        for j1 in range(5 - i):
            print(' ', end='')
        for j2 in range(i * 2 - 1):  # 별은 홀수개로 찍는다. 1, 3, 5, 7, 9
            print('*', end='')
        print()
    else: # 6 ~ 9
        for j1 in range(i - 5): # 1, 2, 3, 4
            print(' ', end='')
        for j2 in range(19 - (i * 2)): # 7, 5, 3, 1
            print('*', end='')
        print()
'''
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
'''
for i in range(1, 10):
    if i <= 5:
        space = ' ' * (5 - i)
        star = '*' * (i * 2 -1)
        print(space + star)
    else:
        space = ' ' * (i - 5)
        star = '*' * (19 - (i * 2))
        print(space + star)
print()

# 4. ----------------------------------------------------------------------------------------------
# 집 앞 버스 정류장에서 학교까지 가는 버스 A, B, C의 운행정보가 다음과 같을 때,
# 2대 이상의 버스가 동시에 정차하는 시간대를 출력
# < 버스 A, B 운행 정보 > - 오전 6시 첫차 / 오후 23시 운행 종료
#                       - 버스 A : 15분 간격 운행 / 버스 B : 13분 간격 운행
# < 버스 C 운행 정보 > - 오전 6시 20분 첫차 / 오후 22시 운행 종료
#                    - 버스 C : 8분 간격 운행
busA = 15; busB = 13; busC = 8 # 운행시간은 분(minute)을 기준으로 계산
totalRunTime = 17 * 60 # 총운행시간 : 6시 ~ 23시, 17시간

for i in range(totalRunTime + 1):
    if i < 20 or i > (totalRunTime - 60): # Bus A, B만 운행하는 시간, Bus C가 운행하지 않는 시간
        if i % busA == 0 and i % busB == 0:
            hour = 6 + i // 60
            min = i % 60
            print('Bus A 와 Bus B 동시 정차!! \t {:0>2}:{:0>2}'.format(hour, min) )
    else:
        if i % busA == 0 and i % busB == 0:
            hour = 6 + i // 60
            min = i % 60
            print('Bus A 와 Bus B 동시 정차!! \t {:0>2}:{:0>2}'.format(hour, min))
        elif i % busA == 0 and i % busC == 0:
            hour = 6 + i // 60
            min = i % 60
            print('Bus A 와 Bus C 동시 정차!! \t {:0>2}:{:0>2}'.format(hour, min))
        elif i % busC == 0 and i % busB == 0:
            hour = 6 + i // 60
            min = i % 60
            print('Bus B 와 Bus C 동시 정차!! \t {:0>2}:{:0>2}'.format(hour, min) )
        elif i % busA == 0 and i % busB and i % busC == 0:
            hour = 6 + i // 60
            min = i % 60
            print('Bus A & Bus B & Bus C 동시 정차!! \t {:0>2}:{:0>2}'.format(hour, min))
print()


# 5. ----------------------------------------------------------------------------------------------
# 톱니(sawtooth)가 각각 n1개와 n2개의 톱니바퀴(gear)가 서로 맞물려 회전할 때,
# 회전을 시작한 후 처음 맞물린 톱니가 최초로 다시 만나게 될 때까지의 톱니의 수와 각각의 바퀴 회전수 출력
gearATcnt = 12 # int(input('Gear A 톱니수 입력 : '))
gearBTcnt = 7 # int(input('Gear B 톱니수 입력 : '))

# # (단, n2는 n1 보다 크다.) 조건을 만족할 때만 적용 가능
# gearA = 0; gearB = 0 # 누적되는 톱니 수
# lcm = 0 # the least[lowest] common multiple, 최소공배수
#
# while True:
#     if gearA != 0:
#         if gearA != lcm:
#             gearA += gearATcnt
#             print(f'gearA: {gearA}')
#         else:
#             break
#     else:
#         gearA += gearATcnt
#         print(f'1_gearA: {gearA}')
#     # 7 -> 14 -> 21 -> 28 -> 35 -> 42 -> 49 -> 56
#
#     if gearB != 0 and gearB % gearATcnt == 0: # 최소공배수 조건 만족
#         lcm = gearB
#         print(f'lcm: {lcm}')
#     # 0 -> 84
#     else:
#         gearB += gearBTcnt
#         print(f'gearB: {gearB}')
#     # 12 -> 24 -> 36 -> 48 -> 60 -> 72 -> 84 -> end
#
# print('최초로 다시 만나는 톱니수(최소공배수) : {}번째 톱니'.format(lcm))
# print('Gear A 회전수 : {}회전'.format(lcm // gearATcnt))
# print('Gear B 회전수 : {}회전'.format(lcm // gearBTcnt))

stdGear = gearATcnt if gearATcnt > gearBTcnt else gearBTcnt
stepGear = gearATcnt if gearATcnt < gearBTcnt else gearBTcnt
accumulate = stdGear
lcm = 0  # the least[lowest] common multiple, 최소공배수

while True:
    if lcm != 0:
        break

    if accumulate % stepGear == 0:
        lcm = accumulate
        print(f'lcm: {lcm}')
    else:
        accumulate += stdGear
        print(f'accumulate: {accumulate}')

print('최초로 다시 만나는 톱니수(최소공배수) : {}번째 톱니'.format(lcm))
print('Gear A 회전수 : {}회전'.format(lcm // gearATcnt))
print('Gear B 회전수 : {}회전'.format(lcm // gearBTcnt))
print()


# 6. ----------------------------------------------------------------------------------------------
# 윤년 계산기
# < 윤년 조건 > - 연도가 4로 나누어 떨어지고 100으로 나누어 떨어지지 않으면 윤년이다.
#              - 또는 연도가 400으로 나누어 떨어지면 윤년이다.
targetYear = 2024 # int(input('연도 입력 : '))

if (targetYear % 4 == 0 and targetYear % 100 != 0) or (targetYear % 400 == 0):
    print('{}년: 윤년!!'.format(targetYear))
else:
    print('{}년: 평년'.format(targetYear))
print()

for year in range(2023, (2023 + 101)):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print('{}년: 윤년!!'.format(year))
    else:
        print('{}년: 평년'.format(year))


