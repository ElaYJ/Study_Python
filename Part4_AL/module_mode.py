# <EX> ----------------------------------------------------------------------------
# 최빈값 알고리즘을 이용해 나이 분포를 간단한 그래프로 출력하는 모듈
# 다음은 어떤 회사의 전직원 나이를 나타내는 리스트이다.

class MaxAlgorithm:

    def __init__(self, ns):
        self.nums = ns
        self.maxNum = 0
        self.maxNumIdx = 0

    def setMaxIdxAndNum(self):
        self.maxNum = 0
        self.maxNumIdx = 0

        for i, n in enumerate(self.nums):
            if self.maxNum < n:
                self.maxNum = n
                self.maxNumIdx = i

        return self.maxNum

    def getMaxNum(self):
        return self.maxNum

    def getMaxNumIdx(self):
        return self.maxNumIdx



#import maxMod

class ModeAlgorithm:

    def __init__(self, ns, mn):
        self.nums = ns
        self.maxNum = mn
        self.indexes = []

    # 인덱스 리스트 생성 및 빈도 저장
    def setIndexList(self):
        self.indexes = [0 for i in range(self.maxNum + 1)]

        for n in self.nums:
            self.indexes[n] = self.indexes[n] + 1

    def getIndexList(self):
        if sum(self.indexes) == 0:
            return None
        else:
            return self.indexes

    def printAges(self):

        n = 1
        while True:

            maxAlo = MaxAlgorithm(self.indexes)
            maxAlo.setMaxIdxAndNum()
            maxNum = maxAlo.getMaxNum()
            maxNumIdx = maxAlo.getMaxNumIdx()

            if maxNum == 0:
                break

            print(f'[{n:0>3}] {maxNumIdx}세 빈도수: {maxNum}\t', end='')
            print('+' * maxNum)
            self.indexes[maxNumIdx] = 0

            n += 1



# <EX> ----------------------------------------------------------------------------
# 최빈도 알고리즘을 이용해 모든 회차의 각 번호에 대한 빈도수를 출력하는 프로그램
# 다음은 회차별 로또 번호이다.

class LottoMode:

    def __init__(self, ln):
        self.lottoNums = ln
        self.modeList = [0 for n in range(1, 47)]

    def getLottoNumMode(self):

        for roundNums in self.lottoNums:
            for num in roundNums:
                self.modeList[num] = self.modeList[num] + 1

        return self.modeList

    def printModeList(self):
        if sum(self.modeList) == 0:
            return None

        for i, m in enumerate(self.modeList):
            if i != 0:
                print(f'번호: {i:>2}, 빈도: {m}, {"*" * m}')
