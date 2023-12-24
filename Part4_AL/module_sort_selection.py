# <Q> -----------------------------------------------------------------
# 선택정렬 알고리즘을 이용해서 학생 20명의 시험 점수를 오름차순과 내림차순으로 정렬하는 모듈
# 시험 점수는 50 부터 100 까지로 한다.


def sortNumber(ns, asc=True):

    if asc:
        for i in range(len(ns) - 1):
            minIdx = i

            for j in range(i + 1, len(ns)):
                if ns[minIdx] > ns[j]:
                    minIdx = j

            ns[i], ns[minIdx] = ns[minIdx], ns[i]

    else:
        for i in range(len(ns) - 1):
            maxIdx = i

            for j in range(i + 1, len(ns)):
                if ns[maxIdx] < ns[j]:
                    maxIdx = j

            ns[i], ns[maxIdx] = ns[maxIdx], ns[i]

    return ns


def selectionSort(ns, asc=True):

    for i in range(len(ns) - 1):
        targetIdx = i

        for j in range(i + 1, len(ns)):
            if asc:
                if ns[targetIdx] > ns[j]:
                    targetIdx = j
            else:
                if ns[targetIdx] < ns[j]:
                    targetIdx = j

        ns[i], ns[targetIdx] = ns[targetIdx], ns[i]

    return ns





# <EX> --------------------------------------------------------------------------
# 숫자로 이루어진 리스트를 선택정렬 알고리즘을 이용해서 오름차순과 내림차순으로 정렬하는 모듈
# 단, 정렬하는 과정도 출력한다

from copy import deepcopy

def selectSortAlgorithm(ns, asc=True):

    c_ns = deepcopy(ns)

    for i in range(len(c_ns) - 1):
        switch_idx = i

        for j in range(i + 1, len(c_ns)):

            # ascending - minimum value
            if asc:
                if c_ns[switch_idx] > c_ns[j]:
                    switch_idx = j
            # descending - maximum value
            else:
                if c_ns[switch_idx] < c_ns[j]:
                    switch_idx = j

        c_ns[i], c_ns[switch_idx] = c_ns[switch_idx], c_ns[i]

        print(f'nums: {c_ns}')

    return c_ns

def selectionSortAlgorithm(ns, asc=True):

    c_ns = deepcopy(ns)

    for i in range(len(c_ns) - 1):

        switch_idx = i
        for j in range(i + 1, len(c_ns)):

            if asc:
                if c_ns[switch_idx] > c_ns[j]:
                    switch_idx = j
            else:
                if c_ns[switch_idx] < c_ns[j]:
                    switch_idx = j

        if switch_idx != i:
            c_ns[i], c_ns[switch_idx] = c_ns[switch_idx], c_ns[i]

        print(f'nums: {c_ns}')

    return c_ns