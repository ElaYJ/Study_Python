'''
 # [선택 정렬] 주어진 리스트 중에 최소값을 찾아, 그 값을 맨 앞에 위치한 값과 교체하는 방식으로
              자료를 정렬하는 알고리즘이다
'''

nums = [4, 2, 5, 1, 3]
print(f'initial nums: {nums}')

for i in range(len(nums)-1):
	minIdx = i

    # 최소값 찾기
	for j in range(i+1, len(nums)):
		if nums[minIdx] > nums[j]:
			minIdx = j


	tempNum = nums[i]
	nums[i] = nums[minIdx]
	nums[minIdx] = tempNum

        print(f'nums: {nums}')


print(f'final nums: {nums}')
print()




import module_sort_selection as sm
import random

# <Q> ------------------------------------------------------------------------
# 선택정렬 알고리즘을 이용해서 학생 20명의 시험 점수를 오름차순과 내림차순으로 정렬하는 모듈
# 시험 점수는 50 부터 100 까지로 한다.

import copy

scores = random.sample(range(50, 101), 20)
print(f'scores: {scores}')
print(f'scores length: {len(scores)}')

# ascending
# result = sm.sortNumber(scores)
result = sm.sortNumber(copy.deepcopy(scores))
print(f'result(ASC): {result}')

# descending
# result = sm.sortNumber(scores, asc=False)
result = sm.sortNumber(copy.deepcopy(scores), asc=False)
print(f'result(DESC): {result}')


# <EX> ---------------------------------------------------------------------------
# 숫자로 이루어진 리스트를 선택정렬 알고리즘을 이용해서 오름차순과 내림차순으로 정렬하는 모듈만들기
# 단, 정렬하는 과정도 출력한다

# import random
# import selectMod

if __name__ == '__main__':
    nums = random.sample(range(1, 20), 10)

    print(f'not sorted nums:\n{nums}')
    result = sm.sortSelectSortAlgorithm(nums)
    print(f'sorted nums by ASC:\n{result}')

    print(f'not sorted nums:\n{nums}')
    result = sm.sortSelectSortAlgorithm(nums, asc=False)
    print(f'sorted nums by DESC:\n{result}')

