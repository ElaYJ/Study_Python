# <EX> --------------------------------------------------------------------------
# 최솟값 알고리즘을 이용해서 숫자로 이루어진 리스트에서 최솟값과 최솟값의 개수를 찾는 모듈 만들기
# 리스트는 1부터 50까지의 난수 30개를 이용하되, 중복이 허용되도록 한다.

class MinAlgorithm:

    def __init__(self, ns):
        self.nums = ns
        self.minNum = 0
        self.minNumCnt = 0

    def setMinNum(self):
        self.minNum = 51

        for n in self.nums:
            if self.minNum > n:
                self.minNum = n

    def getMinNum(self):
        self.setMinNum()

        return self.minNum

    def setMinNumCnt(self):
        self.setMinNum()

        for n in self.nums:
            if self.minNum == n:
                self.minNumCnt += 1

    def getMinNumCnt(self):
        self.setMinNumCnt()

        return self.minNumCnt



# <EX> -----------------------------------------------------------------------------
# 학급 전체 학생의 시험 점수에 대한 평균과 최솟값을 구하고 평균과 최솟값의 편차를 출력하는 프로그램을
# 최솟값 알고리즘을 이용해서 만들기


def getAvg(ns):

    total = 0
    for n in ns:
        total += n

    return total / len(ns)

def getMin(ns):

    minN = ns[0]
    for n in ns:
        if minN > n:
            minN = n

    return minN

def getDeviation(n1, n2):
    return round(abs(n1 - n2), 2)

def getMaxOrMin(ns, maxFlag = True):

    resultN = ns[0]
    for n in ns:
        if maxFlag:
            if resultN < n:
                resultN = n
        else:
            if resultN > n:
                resultN = n

    return resultN


# Class로 구조화
class ScoreManagement:

    def __init__(self, ss):
        self.scores = ss
        self.score_tot = 0
        self.score_avg = 0
        self.score_min = 0
        self.score_max = 0

    def getMinScore(self):
        # scores가 초기화되지 않았다면...
        if self.scores == None or len(self.scores) == 0:
            return None

        self.score_min = self.scores[0]
        for score in self.scores:
            if self.score_min > score:
                self.score_min = score

        return self.score_min

    def getMaxScore(self):
        if self.scores == None or len(self.scores) == 0:
            return None

        self.score_max = self.scores[0]
        for score in self.scores:
            if self.score_max < score:
                self.score_max = score

        return self.score_max

    def getTotScore(self):
        if self.scores == None or len(self.scores) == 0:
            return None

        # 초기화하지 않으면 외부에서 호출할 때마다 값이 누적된다.
        self.score_tot = 0
        for score in self.scores:
            self.score_tot += score

        return self.score_tot

    def getAvgScore(self):
        if self.scores == None or len(self.scores) == 0:
            return None

        self.score_avg = round(self.getTotScore() / len(self.scores), 2)
        return self.score_avg

    def getMaxDeviation(self):
        result = abs(self.getAvgScore() - self.getMaxScore())
        return round(result, 2)

    def getMinDeviation(self):
        result = abs(self.getAvgScore() - self.getMinScore())
        return round(result, 2)
