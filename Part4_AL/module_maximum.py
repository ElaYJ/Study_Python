# <EX> --------------------------------------------------------------------------
# 최댓값 알고리즘을 이용해서 숫자로 이루어진 리스트에서 최댓값과 최댓값의 개수를 찾는 모듈 만들기
# 리스트는 1부터 50까지의 난수 30개를 이용하되, 중복이 허용되도록 한다.

class MaxAlgorithm:

    def __init__(self, ns):
        self.nums = ns
        self.maxNum = None
        self.maxNumIdx = None
        self.maxNumCnt = None

    def setMaxNum(self):
        self.maxNum = self.nums[0]

        for n in self.nums:
            if self.maxNum < n:
                self.maxNum = n

    def setMaxNumAndIdx(self):
        self.maxNum = self.nums[0]
        self.maxNumIdx = 0

        for i, n in enumerate(self.nums):
            if self.maxNum < n:
                self.maxNum = n
                self.maxNumIdx = i

    def setMaxNumCnt(self):
        if self.maxNum == None: self.setMaxNum()

        self.maxNumCnt = 0
        for n in self.nums:
            if self.maxNum == n:
                self.maxNumCnt += 1

    def getMaxNum(self):
        if self.maxNum == None: self.setMaxNum()

        return self.maxNum

    def getMaxNumIdx(self):
        if self.maxNumIdx == None: self.setMaxNumAndIdx()

        return self.maxNumIdx

    def getMaxNumCnt(self):
        if self.maxNumCnt == None: self.setMaxNumCnt()

        return self.maxNumCnt


# <EX> -----------------------------------------------------------------------------
# 학급 전체 학생의 시험 점수에 대한 평균과 최댓값을 구하고 평균과 최댓값의 편차를 출력하는 프로그램을
# 최댓값 알고리즘을 이용해서 만들기

def getAvg(ns):

    total = 0
    for n in ns:
        total += n

    return total / len(ns)

def getMax(ns):

    maxN = ns[0]
    for n in ns:
        if maxN < n:
            maxN = n

    return maxN

def getDeviation(n1, n2):
    return round(abs(n1 - n2), 2)

