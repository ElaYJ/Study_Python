'''
 # [병합 정렬] 자료구조를 분할하고 각각의 분할된 자료구조를 정렬한 후 다시 병합하여 정렬
        ▶ 재귀 함수를 이용해 구현
'''

def mSort(ns):
    # Item이 1개가 될 때까지
    if len(ns) < 2:
        return ns

    # 재귀함수로 분할한다.
    print('>>> Divide <<<')
    mid_idx = len(ns) // 2

    left_area = mSort(ns[0:mid_idx])
    print(f'left Area : {left_area}\n' + ('-' * 30))

    right_area = mSort(ns[mid_idx:len(ns)])
    print(f'right Area: {right_area}\n' + ('-' * 30) + '\n')


    # 병합
    print('>>> Merge <<<')
    sorted_area = []

    left_idx = 0; right_idx = 0
    while left_idx < len(left_area) and right_idx < len(right_area):

        if left_area[left_idx] < right_area[right_idx]:
            sorted_area.append(left_area[left_idx])
            left_idx += 1
        else:
            sorted_area.append(right_area[right_idx])
            right_idx += 1

    sorted_area = sorted_area + left_area[left_idx:]
    sorted_area = sorted_area + right_area[right_idx:]

    print(f'mergedNums: {sorted_area}\n' + ('-' * 30) + '\n')

    return sorted_area


nums = [8, 1, 4, 3, 2, 5, 10, 6]
print(f'nums: {nums}')
print(f'sorted nums: {mSort(nums)}')
print()


# [MyCode] 병합 부분을 함수로 구분한다.
def mergeSort(arr, asc=True):

    if len(arr) <= 1:
        return arr

    mid_idx = len(arr) // 2

    left_area = mergeSort(arr[:mid_idx], asc)  # 0 <= left_area <= mid_idx - 1
    right_area = mergeSort(arr[mid_idx:], asc)  # mid_idx <= right_area <= len(ns) -1

    return mergeTwoArea(left_area, right_area, asc)

def mergeTwoArea(left, right, asc):
    sorted_area = []

    i = j = 0
    while i < len(left) and j < len(right):

        if asc:
            if left[i] < right[j]:
                sorted_area.append(left[i])
                i += 1
            else:
                sorted_area.append(right[j])
                j += 1
        else:
            if left[i] > right[j]:
                sorted_area.append(left[i])
                i += 1
            else:
                sorted_area.append(right[j])
                j += 1

    sorted_area.extend(left[i:])
    sorted_area.extend(right[j:])

    return sorted_area


print(f'nums: {nums}')
print(f'mergedNums by ASC : {mergeSort(nums)}')
print(f'mergedNums by DESC: {mergeSort(nums, asc=False)}')
print(f'nums: {nums}')
print()




import module_sort_merge as sm
import random

# <Q> --------------------------------------------------------------------
# 1부터 100까지의 난수 10개를 생성하고,
# 다음의 요구 사항을 만족하는 모듈을 만들기
# 요구 사항 1) 병합정렬 알고리즘을 이용한 난수 정렬 모듈 구현
# 요구 사항 2) 위의 모듈에 오름차순과 내림차순을 선택할 수 있는 옵션 추가

#import random as rd

rNums = random.sample(range(1, 101), 10)
print(f'not sorted rNums: {rNums}\n')
print(f'merge sorted rNums by ASC: {sm.mergeSortADE(rNums)}\n')
print(f'merge sorted rNums by DESC: {sm.mergeSortADE(rNums, asc=False)}\n')



# <EX> ---------------------------------------------------------------------------
# 숫자로 이루어진 리스트를 선택정렬 알고리즘을 이용해서 오름차순과 내림차순으로 정렬하는 모듈만들기
# 단, 정렬하는 과정도 출력한다


#import mergeAlgorithm

rNums = random.sample(range(1, 101), 20)

print(f'before sorted rNums:\n{rNums}\n')
print(f'merge sorted rNums by ASC:\n{sm.mergeSortAlgorithm(rNums)}\n')
print(f'merge sorted rNums by DESC:\n{sm.mergeSortAlgorithm(rNums, asc=False)}\n')
print(f'after sorted rNums:\n{rNums}\n')







