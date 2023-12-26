def mergeSort(ns):
    if len(ns) < 2:
        return ns

    midIdx = len(ns) // 2
    leftNums = mergeSort(ns[0:midIdx])
    rightNums = mergeSort(ns[midIdx:len(ns)])

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
    return mergedNums


# <Q> --------------------------------------------------------------------
# 1부터 100까지의 난수 10개를 생성하고,
# 다음의 요구 사항을 만족하는 모듈을 만들기
# 요구 사항 1) 병합정렬 알고리즘을 이용한 난수 정렬 모듈 구현
# 요구 사항 2) 위의 모듈에 오름차순과 내림차순을 선택할 수 있는 옵션 추가

def mergeSortADE(ns, asc=True):
    if len(ns) < 2:
        return ns

    midIdx = len(ns) // 2
    leftNums = mergeSortADE(ns[0:midIdx], asc=asc)
    rightNums = mergeSortADE(ns[midIdx:len(ns)], asc=asc)

    mergedNums = []
    leftIdx = 0; rightIdx = 0
    while leftIdx < len(leftNums) and rightIdx < len(rightNums):

        if asc:

            if leftNums[leftIdx] < rightNums[rightIdx]:
                mergedNums.append(leftNums[leftIdx])
                leftIdx += 1
            else:
                mergedNums.append(rightNums[rightIdx])
                rightIdx += 1

        else:

            if leftNums[leftIdx] > rightNums[rightIdx]:
                mergedNums.append(leftNums[leftIdx])
                leftIdx += 1
            else:
                mergedNums.append(rightNums[rightIdx])
                rightIdx += 1

    mergedNums += leftNums[leftIdx:]
    mergedNums += rightNums[rightIdx:]
    print(f'mergedNums: {mergedNums}')

    return mergedNums


if __name__ == '__main__':

    nums = [8, 1, 4, 3, 2, 5, 10, 6]
    print(f'merge sorted nums: {mergeSortADE(nums)}')
    print(f'merge sorted nums: {mergeSortADE(nums, asc=False)}')




# <EX> ---------------------------------------------------------------------------
# 숫자로 이루어진 리스트를 선택정렬 알고리즘을 이용해서 오름차순과 내림차순으로 정렬하는 모듈만들기
# 단, 정렬하는 과정도 출력한다

def mergeSortAlgorithm(arr, asc=True):
    if len(arr) < 2:
        return arr

    mid_idx = len(arr) // 2
    left_area = mergeSortAlgorithm(arr[:mid_idx], asc=asc)
    right_area = mergeSortAlgorithm(arr[mid_idx:], asc=asc)

    sorted_area = []
    l_idx = 0; r_idx = 0
    while l_idx < len(left_area) and r_idx < len(right_area):

        if asc:
            if left_area[l_idx] < right_area[r_idx]:
                sorted_area.append(left_area[l_idx])
                l_idx += 1
            else:
                sorted_area.append(right_area[r_idx])
                r_idx += 1

        else:
            if left_area[l_idx] > right_area[r_idx]:
                sorted_area.append(left_area[l_idx])
                l_idx += 1
            else:
                sorted_area.append(right_area[r_idx])
                r_idx += 1

    sorted_area.extend(left_area[l_idx:])
    sorted_area.extend(right_area[r_idx:])

    print(f'mergedNums: {sorted_area}')
    return sorted_area


