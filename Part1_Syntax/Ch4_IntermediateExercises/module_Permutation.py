def getPermutationCnt(n, r, logPrint = True):

    result = 1
    for n in range(n, (n-r), -1):
        if logPrint: print('n : {}'.format(n))
        result = result * n

    return result



from itertools import permutations

def getPermutations(ns, r):

    # pList = list(permutations(ns, r))
    pResult = permutations(ns, r)
    print(f'pResult: {pResult}')
    pList = list(pResult)
    print(f'pList: {pList}')

    print(f'{len(ns)}P{r} 개수: {len(pList)}')

    # for n in permutations(ns, r):
    #     print(n, end=', ')
    # print(pList)


if __name__ == '__main__':
    numN = int(input('numN 입력: '))
    numR = int(input('numR 입력: '))


    print(f'{numN}P{numR}: {getPermutationCnt(numN, numR, logPrint=False)}')

    ns = [1, 2, 3, 4, 5, 6, 7, 8]
    getPermutations(ns, 3)


