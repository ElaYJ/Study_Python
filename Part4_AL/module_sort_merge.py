# def mSort(ns):
#     if len(ns) < 2:
#         return ns
#
#     midIdx = len(ns) // 2
#     leftNums = mSort(ns[0:midIdx])
#     rightNums = mSort(ns[midIdx:len(ns)])
#
#     mergedNums = []
#     leftIdx = 0; rightIdx = 0
#     while leftIdx < len(leftNums) and rightIdx < len(rightNums):
#         if leftNums[leftIdx] < rightNums[rightIdx]:
#             mergedNums.append(leftNums[leftIdx])
#             leftIdx += 1
#         else:
#             mergedNums.append(rightNums[rightIdx])
#             rightIdx += 1
#
#     mergedNums = mergedNums + leftNums[leftIdx:]
#     mergedNums = mergedNums + rightNums[rightIdx:]
#     return mergedNums


def mSort(ns, asc=True):
    if len(ns) < 2:
        return ns

    midIdx = len(ns) // 2
    leftNums = mSort(ns[0:midIdx], asc=asc)
    rightNums = mSort(ns[midIdx:len(ns)], asc=asc)

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

    mergedNums = mergedNums + leftNums[leftIdx:]
    mergedNums = mergedNums + rightNums[rightIdx:]
    return mergedNums


if __name__ == '__main__':
    nums = [8, 1, 4, 3, 2, 5, 10, 6]
    print(f'merge sorted nums: {mSort(nums)}')
    print(f'merge sorted nums: {mSort(nums, asc=False)}')




# <EX> ---------------------------------------------------------------------------
# 숫자로 이루어진 리스트를 선택정렬 알고리즘을 이용해서 오름차순과 내림차순으로 정렬하는 모듈만들기
# 단, 정렬하는 과정도 출력한다

def mSort(ns, asc=True):
    if len(ns) < 2:
        return ns

    midIdx = len(ns) // 2
    leftNums = mSort(ns[0:midIdx], asc=asc)
    rightNums = mSort(ns[midIdx:len(ns)], asc=asc)

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


