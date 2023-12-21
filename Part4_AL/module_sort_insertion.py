def sortNum(ns, asc=True):

    if asc:
        for i1 in range(1, len(ns)):
            i2 = i1 - 1
            cNum = ns[i1]

            while ns[i2] > cNum and i2 >= 0:
                ns[i2 + 1] = ns[i2]
                i2 -= 1

            ns[i2+1] = cNum
    else:
        for i1 in range(1, len(ns)):
            i2 = i1 - 1
            cNum = ns[i1]

            while ns[i2] < cNum and i2 >= 0:
                ns[i2 + 1] = ns[i2]
                i2 -= 1

            ns[i2 + 1] = cNum

    return ns


def sortNumber(ns, asc=True):

    for i1 in range(1, len(ns)):
        i2 = i1 - 1
        cNum = ns[i1]

        if asc:
            while ns[i2] > cNum and i2 >= 0:
                ns[i2 + 1] = ns[i2]
                i2 -= 1
        else:
            while ns[i2] < cNum and i2 >= 0:
                ns[i2 + 1] = ns[i2]
                i2 -= 1

        ns[i2+1] = cNum

    return ns



# <Q> ---------------------------------------------------------------
# 1 부터 1000 까지의 난수 100 개를 생성하고 , 다음의 요구 사항을 만족하는 모듈
# # 요구 사항 1) 생성된 난수들을 오름 차순 또는 내림 차순으로 정렬하는 알고리즘 구현
# # 요구 사항 2) 생성된 난수 중 최솟값, 최댓값을 반환하는 함수 구현

class SortNumbers:

    def __init__(self, ns, asc=True):
        self.nums = ns
        self.isAsc = asc

    def isAscending(self, flag):
        self.isAsc = flag

    def setSort(self):

        for i1 in range(1, len(self.nums)):
            i2 = i1 - 1
            cNum = self.nums[i1]

            if self.isAsc:
                while self.nums[i2] > cNum and i2 >= 0:
                    self.nums[i2 + 1] = self.nums[i2]
                    i2 -= 1
            else:
                while self.nums[i2] < cNum and i2 >= 0:
                    self.nums[i2 + 1] = self.nums[i2]
                    i2 -= 1

            self.nums[i2 + 1] = cNum

    def getSortedNumbers(self):
        return self.nums

    def getMinNumber(self):
        if self.isAsc:
            return self.nums[0]
        else:
            return self.nums[len(self.nums)-1]

    def getMaxNumber(self):
        if self.isAsc:
            return self.nums[len(self.nums)-1]
        else:
            return self.nums[0]




# <EX> --------------------------------------------------------------------------
# 숫자로 이루어진 리스트를 삽입정렬 알고리즘을 이용해서 오름차순과 내림차순으로 정렬하는 모듈
# 단, 정렬하는 과정도 출력하도록 한다

import copy

def sortInsertSortAlgorithm(ns, asc=True):

    c_ns = copy.copy(ns)

    for i1 in range(1, len(c_ns)):
        i2 = i1 - 1
        cNum = c_ns[i1]

        if asc:     # ascending
            while c_ns[i2] > cNum and i2 >= 0:
                c_ns[i2 + 1] = c_ns[i2]
                i2 -= 1

        else:       # descending
            while c_ns[i2] < cNum and i2 >= 0:
                c_ns[i2 + 1] = c_ns[i2]
                i2 -= 1

        c_ns[i2+1] = cNum
        print(f'nums: {c_ns}')

    return c_ns