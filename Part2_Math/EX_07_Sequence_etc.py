'''
 # [계차 수열]
 # [피보나치 수열]
 # [팩토리얼]
'''

option_no = int(input('OPTION NO. '))

if option_no == 1:
# 계차수열 ===================================================================================
# {2, 5, 11, 20, 32, 47, 65, 86, 110, 137, 167, …}

    # an = (3n^2 - 3n + 4)/2
    inputA1 = int(input('a1 입력: '))
    inputN = int(input('an 입력: '))

    valueAN = ((3 * inputN ** 2) - (3 * inputN) + 4) / 2
    print('an의 {}번째 항의 값: {}'.format(inputN, int(valueAN)))



elif option_no == 2:
# 피보나치수열 ===================================================================================

    inputN = int(input('n 입력: '))

    valueN = 0
    sumN = 0

    valuePreN1 = 0
    valuePreN2 = 0

    n = 1
    while n <= inputN:
        if n == 1 or n == 2:
            valueN = 1
            valuePreN1 = valueN
            valuePreN2 = valueN
            sumN += valueN
            n += 1

        else:
            valueN = valuePreN1 + valuePreN2
            valuePreN1 = valuePreN2
            valuePreN2 = valueN
            sumN += valueN
            n += 1


    print('{}번째 항의 값: {}'.format(inputN, valueN))
    print('{}번째 항까지의 합: {}'.format(inputN, sumN))


elif option_no == 3:
# 팩토리얼 ===================================================================================

    inputN = int(input('n 입력: '))

    # 반복문 사용

    result = 1
    for n in range(1, inputN + 1):
        result *= n

    print('for문\t-> {}!: {}'.format(inputN, result))


    result = 1
    n = 1
    while n <= inputN:
        result *= n
        n += 1

    print('while문\t-> {}!: {}'.format(inputN, result))



    # 재귀 함수 사용

    def factorialFun(n):
        if n <= 1: return 1

        return n * factorialFun(n - 1)

    print('재귀함수\t-> {}!: {}'.format(inputN, factorialFun(inputN)))


    # 파이썬 함수 사용

    import math
    math.factorial(inputN)

    print('math모듈\t-> {}!: {}'.format(inputN, math.factorial(inputN)))


elif option_no == 4:
# 군수열 ===================================================================================

    n = 1 # Group NO.
    nCnt = 1 # total Term NO.
    searchNC = 0; searchNP = 0
    sumN = 0
    flag = True # 총합이 100이상이면 False~!
    # 전체 수열이 각 항별로 차례대로 돌아감
    while flag:
        # 하나의 군별로 돌아감
        for i in range(1, (n + 1)):
            if i == n: # 군 내 마지막 항은 콤마 없이...
                print('{}/{} '.format(i, (n - i + 1)), end='')
            else:
                print('{}/{}, '.format(i, (n - i + 1)), end='')

            sumN += i / (n - i + 1)

            nCnt += 1 # 전체 항
            if (sumN > 100): # 총합이 100을 넘어가면 ALL STOP~!!
                searchNC = i
                searchNP = n - i + 1
                flag = False # while문 종료
                break # for문 종료

        print() # 하나의 군이 끝나면 개행
        n += 1  # 다음 군(Next Group)

    print('수열의 합이 최초 100을 초과하는 항, 값, 합: {}항, {}/{}, {}'
          .format(nCnt, searchNC, searchNP, round(sumN, 2)))


