# <Q> -----------------------------------------------------------------------
# 학급 학생(20명)들의 중간고사와 기말고사 성적을 이용해서 각각의 순위를 구하고,
# 중간고사 대비 기말고사 순위 변화(편차)를 출력하는 프로그램 (시험 성적은 난수를 이용한다.)

import random

class RankDeviation:

    def __init__(self, mss, ess):
        self.midStuScos = mss
        self.endStuScos = ess
        self.midRanks = [0] * len(mss)
        self.endRanks = [0] * len(mss)
        self.rankDeviation = [0] * len(mss)

    def setRank(self, ss, rs):
        for idx, sco1 in enumerate(ss):
            for sco2 in ss:
                if sco1 < sco2:
                    rs[idx] += 1

    def setMidRank(self):
        self.setRank(self.midStuScos, self.midRanks)

    def getMidRank(self):
        return self.midRanks

    def setEndRank(self):
        self.setRank(self.endStuScos, self.endRanks)

    def getEndRank(self):
        return self.endRanks

    def printRankDeviation(self):

        for idx, mRank in enumerate(self.midRanks):
            deviation = mRank - self.endRanks[idx]

            if deviation > 0:
                deviation = '↑' + str(abs(deviation))
            elif deviation < 0:
                deviation = '↓' + str(abs(deviation))
            else:
                deviation = '=' + str(abs(deviation))

            print(f'mid_rank: {mRank+1:>2}등 \t '\
                  f'end_rank: {self.endRanks[idx]+1:>2}등 \t '\
                  f'Deviation: {deviation}')



# <EX> -------------------------------------------------------------------------------
# 숫자로 이루어진 리스트에서 Item(요소)의 순위를 출력하고,
# 순위에 따라 Item(요소)를 정렬하는 모듈을 만든다. 리스트는 50부터 100까지의 난수 20개를 이용한다.

def rankAlgorithm(ns):

    ranks = [0 for i in range(len(ns))]

    for idx, n1 in enumerate(ns):
        for n2 in ns:
            if n1 < n2:
                ranks[idx] += 1

    print(f'nums: {ns}')
    print(f'ranks: {ranks}')

    for i, n in enumerate(ns):
        print(f'num: {n} \t rank: {ranks[i] + 1}')

    sortedNums = [0 for n in range(len(ns))]

    for idx, rank in enumerate(ranks):
        sortedNums[rank] = ns[idx]

    return sortedNums






