'''
 # [연습문제]
'''

exe_no = int(input('EXE NO. '))

if exe_no == 1:
# <Q1> ---------------------------------------------------------------------------------------------
# 1부터 사용자가 입력한 숫자까지의 약수(Divisor)와 소수(Prime)를 리스트에 각각 저장하고 출력하는 프로그램

    inputNum = int(input('1보다 큰 정수 입력: '))
    listD = []
    listP = []

    for n in range(1, inputNum+1):
        if n == 1:
            listD.append(n)
        else:
            if inputNum % n == 0:
                listD.append(n)

    for number in range(2, inputNum+1):
        flag = True
        for n in range(2, number):
            if number % n == 0:
                flag = False
                break

        if flag:
            listP.append(number)


    print(f'{inputNum}의 약수: {listD}')
    print(f'{inputNum}까지의 소수: {listP}')



elif exe_no == 2:
# <Q2> ---------------------------------------------------------------------------------------------
# 1부터 100사이에서 난수 10개를 생성한 후 짝수와 홀수를 구분해서 리스트에 저장하고,
# 각각의 개수를 출력하는 프로그램

    import random

    randomList = random.sample(range(1, 101), 10)
    print(f'randomList {randomList}')
    evens = []
    odds = []

    for n in randomList:
        if n % 2 == 0:
            evens.append(n)
        else:
            odds.append(n)

    print(f'짝수: {evens} -> 개수: {len(evens)}개')
    print(f'홀수: {odds} -> 개수: {len(odds)}개')





elif exe_no == 3:
# <Q3> ---------------------------------------------------------------------------------------------
# 공원 입장료를 나타낸 표에서 1일 총 입장객이 100명이라고 할 때, 1일 전체 입장 요금을 구하는 프로그램
# 단, 입장 고객의 나이는 난수를 이용한다.

    import random

    visitors = []

    for n in range(100):
        visitors.append(random.randint(1, 100))

    group1, group2, group3, group4, group5 = 0,0,0,0,0
    for age in visitors:

        if age >= 0 and age <= 7:
            group1 += 1
        elif age >= 8 and age <= 13:
            group2 += 1
        elif age >= 14 and age <= 19:
            group3 += 1
        elif age >= 20 and age <= 64:
            group4 += 1
        else:
            group5 += 1

    group1Price = group1 * 0
    group2Price = group2 * 200
    group3Price = group3 * 300
    group4Price = group4 * 500
    group5Price = group5 * 0

    print('-' * 30)
    print(' 영유아\t: {: >2}명\t: {: >7}원'.format(group1, group1Price))
    print(' 어린이\t: {: >2}명\t: {: >7}원'.format(group2, group2Price))
    print(' 청소년\t: {: >2}명\t: {: >7}원'.format(group3, group3Price))
    print(' 성인 \t: {: >2}명\t: {: >7}원'.format(group4, group4Price))
    print(' 어르신\t: {: >2}명\t: {: >7}원'.format(group5, group5Price))

    sum = group1Price + group2Price + group3Price + group4Price + group5Price
    #sumFormat = format(sum, ',')
    print('-' * 30)
    print(' 1일 요금 총합계 : {:,}원'.format(sum))
    print('-' * 30)




elif exe_no == 4:
# <Q4> ---------------------------------------------------------------------------------------------
# 친구 이름 5명을 리스트에 저장하고 오름차순과 내림차순으로 정렬

    friends = []

    for i in range(5):
        friends.append(input('친구 이름 입력: '))

    print(f'친구들 : {friends}')

    friends.sort()
    print(f'오름차순 : {friends}')

    friends.sort(reverse=True)
    print(f'내림차순 : {friends}')




elif exe_no == 5:
# <Q5> ---------------------------------------------------------------------------------------------
# 다음 리스트에서 중복 아이템(숫자)를 제거하는 프로그램

    numbers = [2, 22, 7, 8, 9, 2, 7, 3, 5, 2, 7, 1, 3]
    print(f'numbers : {numbers}')

    for n in numbers:
        if numbers.count(n) >= 2:
            numbers.remove(n)

    print(f'numbers : {numbers}')




elif exe_no == 6:
# <Q6> ---------------------------------------------------------------------------------------------
# 4개의 숫자 중 서로 다른 숫자 2개를 선택해서 만들 수 있는 모든 경우의 수를 출력하는 프로그램

    numbers = [4, 6, 7, 9]
    result = []

    for n1 in numbers:
        for n2 in numbers:
            if n1 == n2:
                continue

            result.append([n1, n2])

    print(f'result: {result}')
    print(f'result length: {len(result)}')


    # n!/(n-r)!
    import math

    permutation = math.factorial(len(numbers)) / math.factorial((len(numbers) - 2))
    print(f'permutation : {int(permutation)}')




elif exe_no == 7:
# <Q7> ---------------------------------------------------------------------------------------------
# 4개의 숫자 중 서로 다른 숫자 3개를 선택해서 만들 수 있는 모든 경우의 수를 출력하는 프로그램

    numbers = [4, 6, 7, 9]
    result = []

    for n1 in numbers:
        for n2 in numbers:
            if n1 == n2:
                continue
            for n3 in numbers:
                if n1 == n3 or n2 == n3:
                    continue

                result.append([n1, n2, n3])

    print(f'result: {result}')
    print(f'result length: {len(result)}')


    import math

    permutation = math.factorial(len(numbers)) / math.factorial((len(numbers) - 3))
    print(f'permutation : {int(permutation)}')
