# Ascending / DEscending
def quickSortADE(ns, asc=True):

    if len(ns) < 2:
        return ns

    mid_idx = len(ns) // 2
    pivot = ns[mid_idx]

    smallNums = []; sameNums = []; bigNums = []

    for n in ns:
        if n < pivot:
            smallNums.append(n)
        elif n == pivot:
            sameNums.append(n)
        else:
            bigNums.append(n)

    if asc:
        return quickSortADE(smallNums, asc=asc) + sameNums + quickSortADE(bigNums, asc=asc)
    else:
        return quickSortADE(bigNums, asc=asc) + sameNums + quickSortADE(smallNums, asc=asc)


if __name__ == '__main__':

    nums = [8, 1, 4, 3, 2, 5, 4, 10, 6, 8]
    print(f'quick sorted nums: {quickSortADE(nums)}')
    print(f'quick sorted nums: {quickSortADE(nums, asc=False)}')