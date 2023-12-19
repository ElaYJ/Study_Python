# nCr = nPr / r!
def getCombinationCnt(n, r, logPrint = True):

    resultP = 1
    resultR = 1
    resultC = 1

    # nPr
    for n in range(n, (n - r), -1):
        resultP = resultP * n
    if logPrint: print('result_nPr : {}'.format(resultP))

    # r!
    for n in range(r, 0, -1):
        resultR = resultR * n
    if logPrint: print('result_r! : {}'.format(resultR))

    # nCr
    resultC = int(resultP / resultR)
    if logPrint: print('result_nCr: {}'.format(resultC))

    return resultC



from itertools import combinations

def getCombinations(ns, r):

    # cList = list(combinations(ns, r))

    c_rlt = combinations(ns, r)
    print(f'c_result: {c_rlt}')

    c_list = list(c_rlt)
    print(f'c_list: {c_list}')

    print(f'{len(ns)}C{r} 개수: {len(c_list)}')

    # for n in combinations(ns, r):
    #     print(n, end=', ')



if __name__ == '__main__':
    numN = int(input('numN 입력: '))
    numR = int(input('numR 입력: '))


    print(f'{numN}C{numR}: {getCombinationCnt(numN, numR, logPrint=False)}')

    ns = [1, 2, 3, 4, 5, 6, 7, 8]
    getCombinations(ns, 3)


