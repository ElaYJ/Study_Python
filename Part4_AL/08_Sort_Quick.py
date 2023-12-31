'''
 # [퀵 정렬] 기준 값보다 작은 값과 큰 값으로 분리한 후 다시 합친다.
'''

def qSort(ns):

    if len(ns) < 2:
        return ns

    # pivot 기준값 설정
    midIdx = len(ns) // 2
    midVal = ns[midIdx]

    smallNums = [] # pivot보다 작은 수
    sameNums = [] # pivot과 같은 수
    bigNums = [] # pivot보다 큰 수

    # pivot과 비교 연산
    for n in ns:
        if n < midVal:
            smallNums.append(n)
        elif n == midVal:
            sameNums.append(n)
        else:
            bigNums.append(n)

    return qSort(smallNums) + sameNums + qSort(bigNums)


nums = [8, 1, 4, 3, 2, 5, 4, 10, 6, 8]
print(qSort(nums))
print()



# <Q> --------------------------------------------------------------------
# 1부터 100까지의 난수 10개를 생성하고,
# 다음의 요구 사항을 만족하는 모듈을 만들기
# 요구 사항 1) 퀵정렬 알고리즘을 이용한 난수 정렬 모듈 구현
# 요구 사항 2) 위의 모듈에 오름차순과 내림차순을 선택할 수 있는 옵션 추가


import random as rd
import module_sort_quick as sm

rNums = rd.sample(range(1, 100), 10)
print(f'not sorted rNums: {sm.quickSort(rNums)}')
print(f'merge sorted rNums by ASC: {sm.quickSort(rNums)}')
print(f'merge sorted rNums by DESC: {sm.quickSort(rNums, asc=False)}')


