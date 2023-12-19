'''
 # [순열]
 # [조합]
 # [확률]
'''

option_no = int(input('option_NO: '))

if option_no == 1:
# 순열 ===================================================================================
# 9P4, 6P2
    numN = int(input('numN 입력: '))
    numR = int(input('numR 입력: '))

    result = 1
    print('nPr: ', end='')
    for n in range(numN, (numN - numR), -1):
        if n == (numN - numR + 1):
            print('{} '.format(n), end='')
        else:
            print('{} × '.format(n), end='')
        result *= n
    print('= {}'.format(result))

    print('result: {:,}'.format(result))

elif option_no == 4:
# Q2
    fNum1 = int(input('factorial1: '))
    result1 = 1

    for n in range(fNum1, 0, -1):
        result1 *= n
    print('result1: {}'.format(result1))

    fNum2 = int(input('factorial2: '))
    result2 = 1

    for n in range(fNum2, 0, -1):
        result2 *= n
    print('result2: {}'.format(result2))

    print('모든 경우의 수: {}'.format(result1 * result2))

    import math

    result1 = math.factorial(fNum1)
    result2 = math.factorial(fNum2)
    print('모든 경우의 수: {}'.format(result1 * result2))



elif option_no == 2:
# 조합 ===================================================================================
# 9c4, 6c2

    numN = int(input('numN 입력: '))
    numR = int(input('numR 입력: '))
    resultP = 1
    resultR = 1
    resultC = 1

    print('nPr: ', end='')
    for n in range(numN, (numN - numR), -1):
        if n == (numN - numR + 1):
            print('{} '.format(n), end='')
        else:
            print('{} × '.format(n), end='')
        resultP *= n
    print('= {}'.format(resultP))
    print('resultP: {:,}'.format(resultP))

    print('r!: ', end='')
    for n in range(numR, 0, -1):
        if n == 1:
            print(f'{n} ', end='')
        else:
            print(f'{n} × ', end='')
        resultR *= n
    print(f'= {resultR}')
    print('resultR: {:,}'.format(resultR))

    resultC = int(resultP / resultR)
    print(f'nCr = nPr / r! = {resultP} / {resultR} = {resultC}')
    print('resultC: {:,}'.format(resultC))


elif option_no == 5:

    numN = int(input('numN 입력: '))
    numR = int(input('numR 입력: '))
    resultP = 1
    resultR = 1
    resultC = 1

    for n in range(numN, (numN - numR), -1):
        print('n : {}'.format(n))
        resultP = resultP * n

    for n in range(numR, 0, -1):
        print('n : {}'.format(n))
        resultR = resultR * n

    resultC = int(resultP / resultR)
    print('resultC: {}'.format(resultC))

    result = (1 / resultC) * 100
    print('{}%'.format(round(result, 2)))





elif option_no == 3:
# 확률 ===================================================================================

    def proFun():
        numN = int(input('numN 입력: '))
        numR = int(input('numR 입력: '))
        resultP = 1
        resultR = 1
        resultC = 1

        for n in range(numN, (numN - numR), -1):
            resultP *= n
        print('resultP: {}'.format(resultP))

        for n in range(numR, 0, -1):
            resultR *= n
        print('resultR: {}'.format(resultR))

        resultC = int(resultP / resultR)
        print('resultC: {}'.format(resultC))

        return resultC


    sample = proFun()
    print('sample: {}'.format(sample))

    event1 = proFun()
    print('event1: {}'.format(event1))

    event2 = proFun()
    print('event2: {}'.format(event2))

    probability = (event1 * event2) / sample
    print('probability: {}%'.format(round(probability * 100, 2)))


