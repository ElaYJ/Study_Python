import random

# datas = [3, 2, 5, 7, 9, 1, 0, 8, 6, 4]
# nums = (4, 7, 10, 2, 4, 7, 0, 2, 7, 3, 9)
#
# result1 = datas + [127,]
# result2 = nums + (127,)
# print(result1)
# print(result2)
#
# datas += (127,)
# nums += (127,)
# print(datas)
# print(result2)
#
#
# ranks = [0 for i in range(20)]
# print(ranks)
#
# import random as rd
# students = [rd.randint(170, 185) for i in range(20)]
# print(students)
#
# #indexes = [0 for i in range(maxNum + 1)]
# indexes = [0] * 10
# print(indexes)
#
#
# cs = ['c', 'x', 'Q', 'A', 'e', 'P', 'p']
# asciis = [ord(c) for c in cs]
# print(asciis)

scores = [random.randint(30,100) for i in range(5)]
print(scores)


def mSort(ns):
    # Item이 1개가 될 때까지
    if len(ns) < 2:
        return ns

    # 재귀함수로 분할한다.
    print('>>> 분할 <<<')
    midIdx = len(ns) // 2
    leftNums = mSort(ns[0:midIdx])
    print(f'leftNums: {leftNums}')
    rightNums = mSort(ns[midIdx:len(ns)])
    print(f'rightNums: {rightNums}')
    print('-'*30)

    # 병합
    print('>>> 병합 <<<')
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
    print('-' * 30)

    return mergedNums


nums = [8, 1, 4, 3, 2, 5, 10, 6]
print(f'mergedNums: {mSort(nums)}')
