# <EX> ---------------------------------------------------------------------
# 숫자로 이루어진 리스트에서 사용자가 입력한 숫자를 검색하는 모듈을 다음 요건에 따라 만들기
# 1. 검색 모듈은 이진 검색 알고리즘을 이용한다.
# 2. 리스트는 [1,2,4,6,7,8,10,11,13,15,16,17,20,21,23,24,27,28]을 이용한다.
# 3. 검색 과정을 로그로 출력한다.
# 4. 검색에 성공하면 해당 정수의 인덱스를 출력하고, 검색 결과가 없으면 -1을 출력한

def searchNumberByBinaryAlgorithm(ns, sn):

    searchResultIdx = -1

    staIdx = 0
    endIdx = len(ns) - 1
    midIdx = (staIdx + endIdx) // 2
    midVal = ns[midIdx]

    print(f'staIdx: {staIdx}, endIdx: {endIdx}')
    print(f'midIdx: {midIdx}, midVal: {midVal}')

    while sn >= ns[0] and sn <= ns[len(ns) - 1]:

        if sn == ns[len(ns) - 1]:
            searchResultIdx = len(ns) - 1
            break

        if staIdx + 1 == endIdx:
            if ns[staIdx] != sn and ns[endIdx] != sn: break

        if sn > midVal:
            staIdx = midIdx
            midIdx = (staIdx + endIdx) // 2
            midVal = ns[midIdx]
            print(f'+staIdx: {staIdx}, endIdx: {endIdx}')
            print(f'+midIdx: {midIdx}, midVal: {midVal}')

        elif sn < midVal:
            endIdx = midIdx
            midIdx = (staIdx + endIdx) // 2
            midVal = ns[midIdx]
            print(f'-staIdx: {staIdx}, endIdx: {endIdx}')
            print(f'-midIdx: {midIdx}, midVal: {midVal}')

        elif sn == midVal:
            searchResultIdx = midIdx
            break

    return searchResultIdx