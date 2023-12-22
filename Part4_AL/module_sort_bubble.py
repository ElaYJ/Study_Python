# <Q> ---------------------------------------------------------------------------
# 새 학년이 되어 학급에 20명의 새로운 학생들이 모였다. 학생들을 키 순서로 줄 세운다.
# 학생들의 키는 random 모듈을 이용해서 170 ~ 185 사이로 생성한다

import copy

def bubbleSort(ns, deepCopy = True):

    if deepCopy:
        cns = copy.copy(ns)
    else:
        cns = ns

    length = len(cns) - 1
    for i in range(length):
        for j in range(length - i):
            if cns[j] > cns[j + 1]:
                cns[j], cns[j + 1] = cns[j + 1], cns[j]

    return cns


# <EX> --------------------------------------------------------------------------
# 숫자로 이루어진 리스트를 버블정렬 알고리즘을 이용해서 오름차순과 내림차순으로 정렬하는 모듈
# 단, 정렬하는 과정도 출력한다

def sortBybubleSortAlgorithm(ns, asc=True):

    c_ns = copy.copy(ns)

    length = len(c_ns) - 1
    for i in range(length):
        for j in range(length-i):

            # Ascending
            if asc:
                if c_ns[j] > c_ns[j+1]:
                    c_ns[j], c_ns[j+1] = c_ns[j+1], c_ns[j]
            # Descending
            else:
                if c_ns[j] < c_ns[j+1]:
                    c_ns[j], c_ns[j+1] = c_ns[j+1], c_ns[j]

            print(f'ns: {c_ns}')
        print()

    return c_ns

