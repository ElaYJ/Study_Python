'''
 # [확률(probability)]
'''

def combinationFund():
    numN = int(input('numN 입력: '))
    numR = int(input('numR 입력: '))
    resultP = 1
    resultR = 1
    resultC = 1

    # nPr
    for n in range(numN, (numN-numR), -1):
        resultP = resultP * n
    print('resultP: {}'.format(resultP))

    # r!
    for n in range(numR, 0, -1):
        resultR = resultR * n
    print('resultR: {}'.format(resultR))

    # nCr = nPr / r!
    resultC = int(resultP / resultR)
    print('resultC: {}'.format(resultC))

    return resultC

# 표본공간
sample = combinationFund()
print('sample: {}'.format(sample))

# 사건_1 :
event1 = combinationFund()
print('event1: {}'.format(event1))

# 사건_2 :
event2 = combinationFund()
print('event2: {}'.format(event2))

# 확률(%)
probability = (event1 * event2) / sample
print('probability: {}%'.format(round(probability * 100, 2)))
