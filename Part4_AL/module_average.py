# <Q> -----------------------------------------------------------------------------
# 평균을 구하고 순위를 정하는 알고리즘
# 다음은 어떤 체조선수의 점수이다


class Top5Players:

    def __init__(self, cs, ns):
        self.currentScores = cs
        self.newScore = ns

    def setAlignScore(self):
        nearIdx = 0
        nearScore = 0
        minNum = 10.0

        for i, s in enumerate(self.currentScores):
            absNum = abs(self.newScore - s)

            if absNum < minNum:
                minNum = absNum
                nearIdx = i
                nearScore = s

        # print(f'nearIdx: {nearIdx}')
        # print(f'nearScore: {nearScore}')

        if self.newScore >= self.currentScores[nearIdx]:
            for i in range(len(self.currentScores)-1, nearIdx, -1):
                self.currentScores[i] = self.currentScores[i-1]

            self.currentScores[nearIdx] = self.newScore

        else:
            for i in range(len(self.currentScores)-1, nearIdx+1, -1):
                self.currentScores[i] = self.currentScores[i-1]

            self.currentScores[nearIdx+1] = self.newScore

        # print(f'self.currentScores: {self.currentScores}')

    def getFinalTop5Scores(self):
        return self.currentScores




# <EX> ----------------------------------------------------------------------------
# 최댓값과 최솟값을 제외한 나머지 점수에 대한 평균을 구하고 순위를 정하는 알고리즘
# 다음은 어떤 체조선수의 경기 점수이다.


class MaxAlgorithm:

    def __init__(self, ss):
        self.scores = ss
        self.maxScore = 0
        self.maxIdx = 0

    def removeMaxScore(self):
        self.maxScore = self.scores[0]

        for i, s in enumerate(self.scores):
            if self.maxScore < s:
                self.maxScore = s
                self.maxIdx = i
        print(f'self.maxScore: {self.maxScore}')
        print(f'self.maxIdx: {self.maxIdx}')

        self.scores.pop(self.maxIdx)
        print(f'scores: {self.scores}')


class MinAlgorithm:

    def __init__(self, ss):
        self.scores = ss
        self.minScore = 0
        self.minIdx = 0

    def removeMinScore(self):
        self.minScore = self.scores[0]

        for i, s in enumerate(self.scores):
            if self.minScore > s:
                self.minScore = s
                self.minIdx = i
        print(f'self.minScore: {self.minScore}')
        print(f'self.minIdx: {self.minIdx}')

        self.scores.pop(self.minIdx)
        print(f'scores: {self.scores}')



