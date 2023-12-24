'''
 # [최댓값] 자료구조에서 가장 큰 값을 찾는다.
 # [최솟값] 자료구조에서 가장 작은 값을 찾는다.
'''

class MaxAlgorithm:

    def __init__(self, ns):
        self.nums = ns
        self.maxNum = 0

    def getMaxNum(self):
        self.maxNum = self.nums[0]

        for n in self.nums:
            if self.maxNum < n:
                self.maxNum = n

        return self.maxNum

ma = MaxAlgorithm([-2, -4, 5, 7, 10, 0, 8, 20, -11])
maxNum = ma.getMaxNum()
print(f'maxNum: {maxNum}')
print()



class MinAlgorithm:

    def __init__(self, ns):
        self.nums = ns
        self.minNum = 0

    def getMinNum(self):
        self.minNum = self.nums[0]

        for n in self.nums:
            if self.minNum > n:
                self.minNum = n

        return self.minNum;

ma = MinAlgorithm([-2, -4, 5, 7, 10, 0, 8, 20, -11])
minNum = ma.getMinNum()
print(f'minNum: {minNum}')
print()




# Max
# <Q> -----------------------------------------------------------------
# 리스트에서 아스키코드가 가장 큰 값을 찾는 알고리즘

class MaxASCII:

    def __init__(self, cs):
        self.chars = cs
        self.maxChar = 0
        self.asciis = []

    def getMaxChar(self):
        self.maxChar = self.chars[0]

        for c in self.chars:
            if ord(self.maxChar) < ord(c):
                self.maxChar = c

        return self.maxChar

    def getChars(self):
        return self.chars

    def getASCII(self):
        if len(self.asciis) < 1:
            self.asciis = [ord(c) for c in self.chars]

        return self.asciis

ma = MaxASCII(['c', 'x', 'Q', 'A', 'e', 'P', 'p'])
print(f'chars: {ma.getChars()}')
print(f'ASCII: {ma.getASCII()}')
maxChar = ma.getMaxChar()
print(f'maxChar: {maxChar}')
print()


# Min
# <Q> -----------------------------------------------------------------
# 리스트에서 아스키코드가 가장 작은 값을 찾는 알고리즘

class MinASCII:

    def __init__(self, cs):
        self.chars = cs
        self.minChar = 0
        self.asciis = []

    def getMinChar(self):
        asciis = self.getASCII()

        minAscii = asciis[0]

        for cNo in asciis:
            if minAscii > cNo:
                minAscii = cNo

        self.minChar = chr(minAscii)

        return self.minChar
        # self.minChar = self.chars[0]
        #
        # for c in self.chars:
        #     if ord(self.minChar) > ord(c):
        #         self.minChar = c
        #
        # return self.minChar

    def getChars(self):
        return self.chars

    def getASCII(self):
        if len(self.asciis) < 1:
            self.asciis = [ord(c) for c in self.chars]

        return self.asciis

ma = MinASCII(['c', 'x', 'Q', 'A', 'e', 'P', 'p'])
print(f'chars: {ma.getChars()}')
print(f'ASCII: {ma.getASCII()}')
minChar = ma.getMinChar()
print(f'minChar: {minChar}')
print()




import module_maximum as max

# Max
# <EX> --------------------------------------------------------------------------
# 최댓값 알고리즘을 이용해서 숫자로 이루어진 리스트에서 최댓값과 최댓값의 개수를 찾는 모듈 만들기
# 리스트는 1부터 50까지의 난수 30개를 이용하되, 중복이 허용되도록 한다.

import random

if __name__ == '__main__':

    # nums = []
    # for n in range(30):
    #     nums.append(random.randint(1, 50))
    nums = [random.randint(1, 50) for n in range(30)]

    print(f'nums:\n{nums}')
    ma = max.MaxAlgorithm(nums)
    print(f'max num: {ma.getMaxNum()}')
    print(f'max num cnt: {ma.getMaxNumCnt()}')
print()


# <EX> -----------------------------------------------------------------------------
# 학급 전체 학생의 시험 점수에 대한 평균과 최댓값을 구하고 평균과 최댓값의 편차를 출력하는 프로그램을
# 최댓값 알고리즘을 이용해서 만들기

#import mod

scores = [100, 64, 94, 66, 75, 58, 99, 76, 96, 74
         , 54, 73, 88, 70, 68, 50, 95, 89, 69, 98]

score_avg = max.getAvg(scores)
score_max = max.getMax(scores)
deviation = max.getDeviation(score_avg, score_max)

print(f'score_avg: {score_avg}')
print(f'score_max: {score_max}')
print(f'deviation: {deviation}')
print()



import module_minimum as min

# Min
# <EX> --------------------------------------------------------------------------
# 최솟값 알고리즘을 이용해서 숫자로 이루어진 리스트에서 최솟값과 최솟값의 개수를 찾는 모듈 만들기
# 리스트는 1부터 50까지의 난수 30개를 이용하되, 중복이 허용되도록 한다.

import random

if __name__ == '__main__':

    nums = [random.randint(1, 50) for n in range(30)]

    print(f'nums:\n{nums}')
    ma = min.MinAlgorithm(nums)
    print(f'min num: {ma.getMinNum()}')
    print(f'min num cnt: {ma.getMinNumCnt()}')
print()


# <EX> -----------------------------------------------------------------------------
# 학급 전체 학생의 시험 점수에 대한 평균과 최솟값을 구하고 평균과 최솟값의 편차를 출력하는 프로그램을
# 최솟값 알고리즘을 이용해서 만들기

#import mod

scores = [100, 64, 94, 66, 75, 58, 99, 76, 96, 74,
          54, 73, 88, 70, 68, 50, 95, 89, 69, 98]

scores_avg = min.getAvg(scores)
scores_min  = min.getMaxOrMin(scores, maxFlag=False)
deviation =  min.getDeviation(scores_avg, scores_min)

print(f'scores_avg: {scores_avg}')
print(f'scores_min: {scores_min}')
print(f'deviation: {deviation}')
print()

#import mod2

sm = min.ScoreManagement(scores)
print(f'score_avg: {sm.getAvgScore()}')
print(f'score_min: {sm.getMinScore()}')
print(f'score_max: {sm.getMaxScore()}')
print(f'score_min_deviation: {sm.getMinDeviation()}')
print(f'score_max_deviation: {sm.getMaxDeviation()}')
