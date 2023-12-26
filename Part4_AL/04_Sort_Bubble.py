'''
 # [버블 정렬] 처음부터 끝까지 인접하는 인덱스의 값을 순차적으로 비교하면서 큰 숫자를 가장 끝으로 옮기는 알고리즘
'''

nums = [10, 2, 7, 21, 0]
print(f'not sorted nums: {nums}')

length = len(nums) - 1

for i in range(length): # 한번 돌 때마다 가장 큰 수가 오른쪽 끝으로 이동
    for j in range(length - i):
        if nums[j] > nums[j+1]:
            # C++ style Swap
            temp = nums[j]
            nums[j] = nums[j+1]
            nums[j+1] = temp
        print(nums)
    print()

print(f'after nums: {nums}')
print(f'sorted nums: {nums}')
print()

import copy

def bubbleSort(ns):
    cns = copy.copy(ns)

    length = len(cns) - 1
    for i in range(length):
        for j in range(length - i):
            if cns[j] > cns[j + 1]:
                # Python style Swap
                cns[j], cns[j+1] = cns[j+1], cns[j]

    return cns

nums = [10, 2, 7, 21, 0]
sortedNums = bubbleSort(nums)

print('>>> Deep Copy <<<')
print(f'after nums: {nums}')
print(f'sortedNums: {sortedNums}')
print()



# <Q> ---------------------------------------------------------------------------
# 새 학년이 되어 학급에 20명의 새로운 학생들이 모였다. 학생들을 키 순서로 줄 세운다.
# 학생들의 키는 random 모듈을 이용해서 170 ~ 185 사이로 생성한다

import module_sort_bubble as sb
import random as rd

students = []
for i in range(10):
    students.append(rd.randint(170, 185))

# 아래와 같이 써도 가능함.
# students = [rd.randint(170, 185) for i in range(10)]

print(f'students: {students}')
print(f'students length: {len(students)}')
print()

# 깊은 복사
print('>>> 깊은 복사 <<<')
sortedStudents = sb.bubbleSort(students)
print(f'after students: {students}')
print(f'sortedStudents: {sortedStudents}')
print()

# 얕은 복사
print('>>> 얕은 복사 <<<')
sortedStudents = sb.bubbleSort(students, deepCopy=False)
print(f'after students: {students}')
print(f'sortedStudents: {sortedStudents}')
print()



# <EX> --------------------------------------------------------------------------
# 숫자로 이루어진 리스트를 버블정렬 알고리즘을 이용해서 오름차순과 내림차순으로 정렬하는 모듈
# 단, 정렬하는 과정도 출력한다

import random
import module_sort_bubble as sb

if __name__ == '__main__':

    nums = random.sample(range(1, 20), 10)
    print(f'not sorted nums: {nums}\n')

    result = sb.sortBybubleSortAlgorithm(nums)
    print(f'sorted nums by ASC: {result}\n', '-'*30, '\n')

    result = sb.sortBybubleSortAlgorithm(nums, asc=False)
    print(f'sorted nums by DESC: {result}\n')

    result = sb.improvedBubbleSort(nums)
    print(f'sorted nums by ASC: {result}\n', '-'*30, '\n')

    result = sb.improvedBubbleSort(nums, asc=False)
    print(f'sorted nums by DESC: {result}\n')

