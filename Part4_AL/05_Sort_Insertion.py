'''
 # [삽입 정렬] 정렬되어 있는 자료 배열과 비교해서, 정렬 위치를 찾는다.
'''

nums = [5, 10, 2, 1, 0]

# ascending
for cur_idx in range(1, len(nums)):
    befor_idx = cur_idx - 1 # 정렬이 완료되었다고 가정한 데이터의 가장 오른쪽 index
    cNum = nums[cur_idx] # 정렬이 완료된 데이터와 비교 연산할 현재 데이터

    while nums[befor_idx] > cNum and befor_idx >= 0: # index가 검색 범위 안에 있어야 한다.
        nums[befor_idx + 1] = nums[befor_idx] # 현재 값과 비교하는 대상을 한 칸 뒤로 밀기
        befor_idx -= 1

    nums[befor_idx+1] = cNum

    print(f'nums: {nums}')
print()


nums = [0, 5, 2, 10, 1]

# descending
for cur_idx in range(1, len(nums)):
    befor_idx = cur_idx - 1
    cNum = nums[cur_idx]

    while nums[befor_idx] < cNum and befor_idx >= 0:
        nums[befor_idx + 1] = nums[befor_idx]
        befor_idx -= 1

    nums[befor_idx+1] = cNum

    print(f'nums: {nums}')
print()


import module_sort_insertion as sin
import random

nums = random.sample(range(1, 11), 5)
print(f'NOT sorted nums: {nums}')
print()

print('>>> Deep Copy <<<')
result = sin.insertSort(nums)
print(f'result: {result}')
print(f'sorted nums: {nums}')
print()

print('>>> Shallow Copy <<<')
result = sin.sortNumber(nums)
print(f'result: {result}')
print(f'sorted nums: {nums}')
print()




# <Q> -----------------------------------------------------------------
# 1 부터 1000 까지의 난수 100 개를 생성하고 , 다음의 요구 사항을 만족하는 모듈
# 요구 사항 1) 생성된 난수들을 오름 차순 또는 내림 차순으로 정렬하는 알고리즘 구현
# 요구 사항 2) 생성된 난수 중 최솟값, 최댓값을 반환하는 함수 구현

import module_sort_insertion as sin
#import random

nums = random.sample(range(1, 100), 10)
print(f'not sortedNumber: {nums}')

# 객체 생성
sn = sin.InsertionSort(nums)

# ascending
sn.setSort()
sorted_num = sn.getSortedNumbers()
print(f'sortedNumber by ASC: {sorted_num}')

# descending
sn.isAscending(False)
sn.setSort()
sorted_num = sn.getSortedNumbers()
print(f'sortedNumber by DESC: {sorted_num}')

# min & max
print(f'MinNumber : {sn.getMinNumber()}')
print(f'MaxNumber : {sn.getMaxNumber()}')
print()

my_nums = random.sample(range(1, 100), 10)
print(f'before sortedNumber: {my_nums}')

# 객체 생성
my_sn = sin.InsertionSort(my_nums)

# ascending
my_sorted_num = my_sn.getSortedNumbers()
print(f'sortedNumber by ASC: {my_sorted_num}')

# descending
my_sn.isAscending(False)
my_sorted_num = my_sn.getSortedNumbers()
print(f'sortedNumber by DESC: {my_sorted_num}')

# min & max
print(f'MinNumber : {my_sn.getMinNumber()}')
print(f'MaxNumber : {my_sn.getMaxNumber()}')
print(f'after sortedNumber: {my_nums}')
print()






# <EX> -----------------------------------------------------------------------
# 숫자로 이루어진 리스트를 삽입정렬 알고리즘을 이용해서 오름차순과 내림차순으로 정렬하는 모듈
# 단, 정렬하는 과정도 출력하도록 한다

#import module_sort_insertion as sin
import random

if __name__ == '__main__':
    nums = random.sample(range(1, 20), 10)
    print(f'before sorted nums: {nums}\n')

    result = sin.insertSortAlgorithm(nums)
    print(f'sorted nums by ASC: {result}\n')

    result = sin.insertSortAlgorithm(nums, asc=False)
    print(f'sorted nums by DESC: {result}\n')

    print(f'after sorted nums: {nums}\n')

    nums = random.sample(range(1, 20), 10)
    print(f'before sorted nums: {nums}\n')

    result = sin.insertionSortAlgorithm(nums)
    print(f'sorted nums by ASC: {result}\n')

    result = sin.insertionSortAlgorithm(nums, asc=False)
    print(f'sorted nums by DESC: {result}\n')

    print(f'after sorted nums: {nums}\n')

