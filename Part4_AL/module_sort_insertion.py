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

import copy

def insertSort(nums, asc=True):

    c_nums = copy.copy(nums)

    for cur_idx in range(1, len(c_nums)):
        bef_idx = cur_idx - 1
        cur_val = c_nums[cur_idx]

        if asc:
            while c_nums[bef_idx] > cur_val:
                if bef_idx < 0: break
                c_nums[bef_idx + 1] = c_nums[bef_idx]
                bef_idx -= 1
        else:
            while c_nums[bef_idx] < cur_val:
                if bef_idx < 0: break
                c_nums[bef_idx + 1] = c_nums[bef_idx]
                bef_idx -= 1

        c_nums[bef_idx + 1] = cur_val

    return c_nums




# <Q> ---------------------------------------------------------------
# 1 부터 1000 까지의 난수 100 개를 생성하고 , 다음의 요구 사항을 만족하는 모듈
# # 요구 사항 1) 생성된 난수들을 오름 차순 또는 내림 차순으로 정렬하는 알고리즘 구현
# # 요구 사항 2) 생성된 난수 중 최솟값, 최댓값을 반환하는 함수 구현

class InsertionSort:

    def __init__(self, ns, asc=True):
        # self.nums = ns # Shallow Copy
        self.nums = copy.deepcopy(ns)
        print(f'self.nums id: {id(self.nums)}, ns id: {id(ns)}')
        self.isAsc = asc
        self.nots_flag = True # not sorted flag

    def isAscending(self, flag):
        self.isAsc = flag
        self.nots_flag = True

    def setSort(self):

        for cur_idx in range(1, len(self.nums)):
            bef_idx = cur_idx - 1
            cur_val = self.nums[cur_idx]

            if self.isAsc:
                while self.nums[bef_idx] > cur_val and bef_idx >= 0:
                    self.nums[bef_idx + 1] = self.nums[bef_idx]
                    bef_idx -= 1
            else:
                while self.nums[bef_idx] < cur_val and bef_idx >= 0:
                    self.nums[bef_idx + 1] = self.nums[bef_idx]
                    bef_idx -= 1

            self.nums[bef_idx + 1] = cur_val

        self.nots_flag = False

    # get()메서드를 호출했을 때 정렬 작업이 되어 있는지 확인하고
    # 정렬되어 있지 않다면 setSort()메서드를 호출한다.
    
    def getSortedNumbers(self):
        if self.nots_flag: self.setSort()
        return self.nums

    def getMinNumber(self):
        if self.nots_flag: self.setSort()

        if self.isAsc:
            return self.nums[0]
        else:
            return self.nums[len(self.nums)-1]

    def getMaxNumber(self):
        if self.nots_flag: self.setSort()

        if self.isAsc:
            return self.nums[len(self.nums)-1]
        else:
            return self.nums[0]




# <EX> --------------------------------------------------------------------------
# 숫자로 이루어진 리스트를 삽입정렬 알고리즘을 이용해서 오름차순과 내림차순으로 정렬하는 모듈
# 단, 정렬하는 과정도 출력하도록 한다

def insertSortAlgorithm(ns, asc=True):

    c_ns = copy.copy(ns)

    for i1 in range(1, len(c_ns)):
        i2 = i1 - 1
        cNum = c_ns[i1]

        cnt = 0
        if asc:     # ascending
            while c_ns[i2] > cNum and i2 >= 0:
                c_ns[i2 + 1] = c_ns[i2]
                i2 -= 1
                cnt += 1

        else:       # descending
            while c_ns[i2] < cNum and i2 >= 0:
                c_ns[i2 + 1] = c_ns[i2]
                i2 -= 1
                cnt += 1

        c_ns[i2+1] = cNum
        print(f'nums: {c_ns}\t cnt: {cnt}')

    return c_ns


# [MyCode]
def insertionSortAlgorithm(nums, asc=True):

    c_nums = copy.deepcopy(nums)

    for cur_idx in range(1, len(c_nums)):
        bef_idx = cur_idx - 1
        cur_val = c_nums[cur_idx]

        mv_cnt = 0
        if asc:
            while c_nums[bef_idx] > cur_val and bef_idx >= 0:
                c_nums[bef_idx + 1] = c_nums[bef_idx]
                bef_idx -= 1
                mv_cnt += 1
        else:
            while c_nums[bef_idx] < cur_val and bef_idx >= 0:
                c_nums[bef_idx + 1] = c_nums[bef_idx]
                bef_idx -= 1
                mv_cnt += 1

        c_nums[bef_idx + 1] = cur_val
        print(f'c_nums: {c_nums}\t mv_cnt: {mv_cnt}')

    return c_nums
