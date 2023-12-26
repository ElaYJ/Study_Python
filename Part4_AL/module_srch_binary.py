# [MyCode]
def binary_search(nums, key):
    low, high = 0, len(nums)-1

    # 검색 성공 조건
    while low <= high:
        mid_idx = (low + high) // 2

        if key == nums[mid_idx]:
            return mid_idx
        elif key > muns[mid_idx]:
            low = mid_idx +1
        else:
            high = mid_idx -1

    # 검색 실패 조건: low > high
    return -1


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

    print(f'0> staIdx: {staIdx}, midIdx: {midIdx}({midVal}), endIdx: {endIdx}')

    while sn >= ns[0] and sn <= ns[len(ns) - 1]:

        if sn == ns[len(ns) - 1]:
            print(f'1> staIdx: {staIdx}, midIdx: {midIdx}({midVal}), endIdx: {endIdx}')
            searchResultIdx = len(ns) - 1
            break

        # 2진으로 나눠가다 start_idx와 end_idx가 나란히 존해했을 때
        # 찾는 값이 없으면 무한 루프에 빠지게 된다.
        if staIdx + 1 == endIdx:
            print(f'2> staIdx: {staIdx}, midIdx: {midIdx}({midVal}), endIdx: {endIdx}')
            if ns[staIdx] != sn and ns[endIdx] != sn: break

        if sn > midVal:
            staIdx = midIdx
            midIdx = (staIdx + endIdx) // 2
            midVal = ns[midIdx]
            print(f'3>+staIdx: {staIdx},+midIdx: {midIdx}({midVal}), endIdx: {endIdx}')

        elif sn < midVal:
            endIdx = midIdx
            midIdx = (staIdx + endIdx) // 2
            midVal = ns[midIdx]
            print(f'4> staIdx: {staIdx},-midIdx: {midIdx}({midVal}),-endIdx: {endIdx}')

        elif sn == midVal:
            print(f'5> midVal({midVal}) == srchVal({sn})')
            searchResultIdx = midIdx
            break

    return searchResultIdx