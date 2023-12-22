# <Q> -----------------------------------------------------------------
# 선택정렬 알고리즘을 이용해서 학생 20명의 시험 점수를 오름차순과 내림차순으로 정렬하는 모듈
# 시험 점수는 50 부터 100 까지로 한다.


def sortNum(ns, asc=True):

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


def sortNumber(ns, asc=True):

    cnt = 0

    for i in range(len(ns) - 1):
        targetIdx = i

        for j in range(i + 1, len(ns)):
            if asc:
                if ns[targetIdx] > ns[j]:
                    targetIdx = j
                    cnt += 1
            else:
                if ns[targetIdx] < ns[j]:
                    targetIdx = j
                    cnt += 1

        ns[i], ns[targetIdx] = ns[targetIdx], ns[i]

    print(f'cnt: {cnt}')

    return ns





# <EX> --------------------------------------------------------------------------
# 숫자로 이루어진 리스트를 선택정렬 알고리즘을 이용해서 오름차순과 내림차순으로 정렬하는 모듈
# 단, 정렬하는 과정도 출력한다

import copy

def sortSelectSortAlgorithm(ns, asc=True):

    c_ns = copy.copy(ns)

    for i in range(len(c_ns) - 1):
        minIdx = i

        for j in range(i + 1, len(c_ns)):

            if asc:     # ascending
                if c_ns[minIdx] > c_ns[j]:
                    minIdx = j
            else:       # descending
                if c_ns[minIdx] < c_ns[j]:
                    minIdx = j

        c_ns[i], c_ns[minIdx] = c_ns[minIdx], c_ns[i]

        print(f'nums: {c_ns}')

    return c_ns

