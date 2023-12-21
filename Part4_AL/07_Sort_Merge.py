'''
 # [병합 정렬] 자료구조를 분할하고 각각의 분할된 자료구조를 정렬한 후 다시 병합하여 정렬
'''

def mSort(ns):
    if len(ns) < 2:
        return ns

    midIdx = len(ns) // 2
    leftNums = mSort(ns[0:midIdx])
    rightNums = mSort(ns[midIdx:len(ns)])

    mergedNums = []
    leftIdx = 0; rightIdx = 0
    while leftIdx < len(leftNums) and rightIdx < len(rightNums):
        if leftNums[leftIdx] < rightNums[rightIdx]:
            mergedNums.append(leftNums[leftIdx])
            leftIdx += 1
        else:
            mergedNums.append(rightNums[rightIdx])
            rightIdx += 1

    mergedNums = mergedNums + leftNums[leftIdx:]
    mergedNums = mergedNums + rightNums[rightIdx:]
    print(f'mergedNums: {mergedNums}')
    return mergedNums


nums = [8, 1, 4, 3, 2, 5, 10, 6]
print(f'mergedNums: {mSort(nums)}')




# <Q> --------------------------------------------------------------------
# 1부터 100까지의 난수 10개를 생성하고,
# 다음의 요구 사항을 만족하는 모듈을 만들기
# 요구 사항 1) 병합정렬 알고리즘을 이용한 난수 정렬 모듈 구현
# 요구 사항 2) 위의 모듈에 오름차순과 내림차순을 선택할 수 있는 옵션 추가

import random as rd
import module_sort_merge as sm

rNums = rd.sample(range(1, 101), 10)
print(f'not sorted rNums: {sm.mSort(rNums)}')
print(f'merge sorted rNums by ASC: {sm.mSort(rNums)}')
print(f'merge sorted rNums by DESC: {sm.mSort(rNums, asc=False)}')









# <EX> ---------------------------------------------------------------------------
# 숫자로 이루어진 리스트를 선택정렬 알고리즘을 이용해서 오름차순과 내림차순으로 정렬하는 모듈만들기
# 단, 정렬하는 과정도 출력한다


import random
#import mergeAlgorithm

rNums = random.sample(range(1, 101), 20)

print(f'not sorted rNums: {rNums}')
print(f'merge sorted rNums by ASC: {sm.mSort(rNums)}')
print(f'merge sorted rNums by DESC: {sm.mSort(rNums, asc=False)}')








