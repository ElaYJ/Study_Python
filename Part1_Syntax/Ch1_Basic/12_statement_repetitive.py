'''
# [반복문]
    ▶ 'for문' - 횟수에 의한 반복
    ▶ 'while문' - 조건에 의한 반복
'''
print('{} * {} = {}'.format(2, 1, (2 * 1)))
print('{} * {} = {}'.format(2, 2, (2 * 2)))
print('{} * {} = {}'.format(2, 3, (2 * 3)))
print('{} * {} = {}'.format(2, 4, (2 * 4)))
print('{} * {} = {}'.format(2, 5, (2 * 5)))
print('{} * {} = {}'.format(2, 6, (2 * 6)))
print('{} * {} = {}'.format(2, 7, (2 * 7)))
print('{} * {} = {}'.format(2, 8, (2 * 8)))
print('{} * {} = {}'.format(2, 9, (2 * 9)))

for i in range(1, 10):
    print('{} * {} = {}'.format(2, i, (2 * i)))

print('{}선수에게 메일 발송'.format('박찬호'))
print('{}선수에게 메일 발송'.format('박세리'))
print('{}선수에게 메일 발송'.format('박지성'))
print('{}선수에게 메일 발송'.format('김연경'))
print('{}선수에게 메일 발송'.format('이승엽'))

players = ['박찬호', '박세리', '박지성', '김연경', '이승엽'] # List
for player in players:
    print('{}선수에게 메일 발송'.format(player))


# 'for ~ in 키워드' : 횟수에 의한 반복(지정한 횟수만큼 반복 실행) --------------------------------------------
for i in range(5):
#   pass -> 실행문을 나중에 코딩하겠음.
    print('{}. Hello python!'.format(i + 1))

# 사용자가 입력한 숫자에 맞는 구구단을 출력하는 코드 작성
userGugudan = 7 # int(input('구구단 몇단을 출력하세겠습니까? '))
for i in range(9):
    result = userGugudan * (i + 1)
    print('{} * {} = {}'.format(userGugudan, (i + 1), result))

# range() 함수 - 'range(start, end, step)'
# range(1, 11, 1) : 1부터 10까지 1씩 증가, 시작이 '0'이거나 단계가 '1'인 경우 생략 가능!
startNum = 5 # int(input('반복의 시작 입력 : '))
endNum = 15 # int(input('반복의 끝 입력 : '))
for i in range(startNum, (endNum + 1)):
    print(f'{i}', end = ' ')
print()

# 횟수에 의한 반복이라면 while문보다 'for문'이 더 적합하다.
# 1부터 10까지의 합을 구하는 경우라면 for문이 while문보다 더 간결하다.
'''
sum = 0
n = 1
while n < 11:
    sum += n
    n += 1
print('sum : {}'.format(sum))
'''
sum = 0
for i in range(1, 11):
    sum += i
print('sum : {}'.format(sum))


# 'while 조건문' : 조건에 의한 반복(지정 조건에 만족할 때까지 반복 실행) --------------------------------------
n = 1
while n < 10:
    print('{} * {} = {}'.format(7, n, (7 * n)))
    n += 1

# 1부터 100까지의 정수 중 2의 배수와 3의 배수를 구분해 출력하기 (단, while문 이용)
# 개인적으로 for문이 더 적합해 보임
n = 1
while n < 101:
    if n % 2 == 0:
        print('{}은 2의 배수이다.'.format(n))
    if n % 3 == 0:
        print('{}은 3의 배수이다.'.format(n))
    n += 1

# [MC] 각 결과값을 리스트에 담아 한번에 출력
n = 1
twoTimes = []; threeTimes = []
while n <= 100:
    if n % 2 == 0:
        twoTimes.append(n)
    if n % 3 == 0:
        threeTimes.append(n)
    n += 1
print('2의 배수 :', twoTimes)
print('3의 배수 :', threeTimes)

# 조건에 의한 반복이라면 for문보다 'while문'이 더 적합하다.
# 1부터 시작해서 7의 배수의 합이 50이상인 최초의 정수를 출력하는 코드
'''
sum = 0; maxInt = 0
# 1부터 100까지 다 돌아야 끝나므로 비효율적!
for i in range(1, 101):
    if i % 7 == 0 and sum <= 50:
        sum += i
        maxInt = i
    print('i : {}'.format(i))
print('7의 배수의 합이 50이상인 최초의 정수는 {}이다.'.format(maxInt))
'''
sum = 0; maxInt = 0; n = 1
# sum 조건을 만족하는 순간 루프를 빠져나오므로 효율적!!
while n <= 100 and sum <= 50:
    if n % 7 == 0:
        sum += n
        maxInt = n
    print('n : {}'.format(n))
    n += 1
print('7의 배수의 합이 50이상인 최초의 정수는 {}이다.'.format(maxInt))

# 무한루프 : while문에서 조건식의 결과가 항상 True인 경우로 반복문을 빠져나올 수 없는 상태
# 하루에 독감으로 병원에 내방하는 환자 수가 50명에서 100명 사이일 때,
# 누적 독감 환자 수가 최초 10,000명을 넘는 날짜를 구하는 코드로,
# 조건식에 논리형 데이터를 사용해 무한 반복을 실행시킨다.
import random

sum = 0; date = 1
flag = True
while flag:
    patientCount = random.randint(50, 100)
    sum += patientCount
    date += 1
    print('날짜 : {}, \t 오늘 환자수 : {}, \t 누적 환자수 : {}'.
          format(date, patientCount, sum))

    if sum >= 10000:
        flag = False


# 'continue' 키워드 ----------------------------------------------------------------------------------
# 반복문 실행 중 'continue'를 만나면 이하 실행문을 생략하고, 처음으로 돌아가 다시 반복문을 실행하다.
for i in range(1, 100):
    if i % 7 != 0:
        continue
    print('{:0>2}은 7의 배수이다.'.format(i))

# 'else' 키워드 --------------------------------------------------------------------------------------
# else의 실행문은 반복문이 모두 종료되고 난 이후 한번 실행된다.
cnt = 0
for i in range(1, 100):
    if i % 7 != 0:   continue

    print('{:0>2}은 7의 배수이다.'.format(i))
    cnt += 1 # 반복문의 실행문이 실행된 횟수가 저장된다.
else:
    print('99까지 정수 중 7의 배수는 {}개이다.'.format(cnt))

# 1부터 100까지의 정수 중 3과 7의 공배수와 최소공배수를 출력하는 코드
lcm = 0 # the least[lowest] common multiple (최소공배수)
for i in range(1, 101):
    if i % 3 != 0 or i % 7 != 0:
        continue

    print('3과 7의 공배수 : {}'.format(i))
    # lcm은 최초 공배수에 해당하므로 lcm이 '0'일 때 한 번만 실행!
    if lcm == 0:
        lcm = i

else:
    print('최소공배수 : {}'.format(lcm))


# 'break' 키워드 ---------------------------------------------------------------------------------------
# 반복문 실행 중 'break'를 만나면 반복문을 종료하고 빠져나온다.
num = 0
while True:
    print('Hello~')
    num += 1
    if (num >= 5):
        break

# 1부터 100까지 정수를 더할 때, 합계가 100이 넘는 최초의 정수 찾기 코드
sum = 0; searchNum = 0
for i in range(1, 101):
    sum += i

    if (sum > 100):
        searchNum = i
        break

print('searchNum : {}'.format(searchNum))

# 10의 팩토리얼(10!)을 계산하는 과정에서 결과값이 50을 넘을 때의 숫자 구하기
result = 1; num = 0
for i in range(1, 11):
    result *= i

    if result > 50:
        num = i
        break

print('num : {}, result : {}'.format(num, result))

# 새끼 강아지의 현재 체중은 880g이고 체중이 2.2kg가 넘으면 이유식을 중단하려고 한다.
# 하루 한번 이유식을 먹을 때마다 체중이 70g씩 증가한다고 할때, 예상되는 이유식 중단 날짜는?
limitWeight = 2200
curWeight = 880
date = 1
while True:
    if curWeight >= limitWeight:
        break

    curWeight += 70
    date += 1

print('이유식 중단 날짜 : {}일'.format(date))


# 중첩 반복문 : 반복문 내에 또 다른 반복문 선언 -------------------------------------------------------------
for i in range(1, 5): # 세로
    for j in range(i): # 가로
        print('*', end='')
    print()

for i in range(5, 0, -1):
    for j in range(i):
        print('*', end='')
    print()

# 구구단 전체를 출력하는 코드
for i in range(1, 10):
    for j in range(2, 10):
        print('{} * {} = {: >2}'.format(j, i, (j * i)), end='\t')
    print()
