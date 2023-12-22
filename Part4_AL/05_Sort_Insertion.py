'''
 # [삽입 정렬] 정렬되어 있는 자료 배열과 비교해서, 정렬 위치를 찾는다.
'''

nums = [5, 10, 2, 1, 0]

# ascending
for i1 in range(1, len(nums)):
    i2 = i1 - 1 # 정렬이 완료되었다고 가정한 데이터의 index
    cNum = nums[i1] # 정렬이 완료된 데이터와 비교 연산할 현재 수

    while nums[i2] > cNum and i2 >= 0:
        nums[i2 + 1] = nums[i2]
        i2 -= 1

    nums[i2+1] = cNum

    print(f'nums: {nums}')
print()


nums = [0, 5, 2, 10, 1]

# descending
for i1 in range(1, len(nums)):
    i2 = i1 - 1
    cNum = nums[i1]

    while nums[i2] < cNum and i2 >= 0:
        nums[i2 + 1] = nums[i2]
        i2 -= 1

    nums[i2+1] = cNum

    print(f'nums: {nums}')
print()


import module_sort_insertion as sin

result = sin.sortNumber(nums, asc=False)
print(f'result: {result}')
print()




# <Q> -----------------------------------------------------------------
# 1 부터 1000 까지의 난수 100 개를 생성하고 , 다음의 요구 사항을 만족하는 모듈
# 요구 사항 1) 생성된 난수들을 오름 차순 또는 내림 차순으로 정렬하는 알고리즘 구현
# 요구 사항 2) 생성된 난수 중 최솟값, 최댓값을 반환하는 함수 구현

import module_sort_insertion as sin
import random

nums = random.sample(range(1, 100), 10)
print(f'not sortedNumber: {nums}')

# 객체 생성
sn = sin.SortNumbers(nums)

# ascending
sn.setSort()
sortedNumber = sn.getSortedNumbers()
print(f'sortedNumber by ASC: {sortedNumber}')

# descending
sn.isAscending(False)
sn.setSort()
sortedNumber = sn.getSortedNumbers()
print(f'sortedNumber by DESC: {sortedNumber}')

# min & max
print(f'MinNumber : {sn.getMinNumber()}')
print(f'MaxNumber : {sn.getMaxNumber()}')








# <EX> -----------------------------------------------------------------------
# 숫자로 이루어진 리스트를 삽입정렬 알고리즘을 이용해서 오름차순과 내림차순으로 정렬하는 모듈
# 단, 정렬하는 과정도 출력하도록 한다

#import module_sort_insertion
import random

if __name__ == '__main__':
    nums = random.sample(range(1, 20), 10)

    print(f'not sorted nums:\n{nums}')
    result = sin.sortInsertSortAlgorithm(nums)
    print(f'sorted nums by ASC:\n{result}')

    print(f'not sorted nums:\n{nums}')
    result = sin.sortInsertSortAlgorithm(nums, asc=False)
    print(f'sorted nums by DESC:\n{result}')

