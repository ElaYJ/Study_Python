
def quickSort(ns, asc=True):

    if len(ns) < 2:
        return ns

    midIdx = len(ns) // 2
    midVal = ns[midIdx]


    smallNums = []; sameNums = []; bigNums = []

    for n in ns:
        if n < midVal:
            smallNums.append(n)
        elif n == midVal:
            sameNums.append(n)
        else:
            bigNums.append(n)

    if asc:
        return quickSort(smallNums, asc=asc) + sameNums + quickSort(bigNums, asc=asc)
    else:
        return quickSort(bigNums, asc=asc) + sameNums + quickSort(smallNums, asc=asc)


if __name__ == '__main__':
    nums = [8, 1, 4, 3, 2, 5, 4, 10, 6, 8]
    print(f'quick sorted nums: {quickSort(nums)}')
    print(f'quick sorted nums: {quickSort(nums, asc=False)}')