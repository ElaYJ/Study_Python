'''
 # [최빈값] 데이터에서 빈도수가 가장 많은 데이터를 최빈값이라고 한다. (빈도수가 가장 높은 데이터)
'''


class MaxAlgorithm:

    def __init__(self, ns):
        self.nums = ns
        self.maxNum = 0
        self.maxNumIdx = 0

    def setMaxIdxAndNum(self):
        self.maxNum = self.nums[0]
        self.maxNumIdx = 0

        for i, n in enumerate(self.nums):
            if self.maxNum < n:
                self.maxNum = n
                self.maxNumIdx = i

    def getMaxNum(self):
        return self.maxNum

    def getMaxNumIdx(self):
        return self.maxNumIdx

nums = [1, 3, 7, 6, 7, 7, 7, 12, 12, 17]

maxAl = MaxAlgorithm(nums)
maxAl.setMaxIdxAndNum()
maxNum = maxAl.getMaxNum()
print(f'maxNum: {maxNum}')

#indexes = [0 for i in range(maxNum + 1)]
indexes = [0] * (maxNum+1)
print(f'indexes: {indexes}')
print(f'indexes length: {len(indexes)}')

for n in nums:
    indexes[n] = indexes[n] + 1
print(f'indexes: {indexes}')

maxAl = MaxAlgorithm(indexes)
maxAl.setMaxIdxAndNum()
max_mode = maxAl.getMaxNum()
max_mode_num = maxAl.getMaxNumIdx()
print(f'max_mode: {max_mode}')
print(f'max_mode_num: {max_mode_num}')
print(f'즉, {max_mode_num}의 빈도수가 {max_mode}로 가장 높다.')
print()

print(nums)

dic_idxs = {}
for n in nums:
    if n not in dic_idxs:
        dic_idxs[n] = 0
    dic_idxs[n] += 1
print(dic_idxs)

max_mode = 0; mode_num = 0
for key, val in dic_idxs.items():
    if max_mode < val:
        max_mode = val
        mode_num = key
print(f'즉, {mode_num}의 빈도수가 {max_mode}로 가장 높다.')
print()


import module_mode as md

# <Q> -----------------------------------------------------------------------------
# 최빈값 알고리즘을 이용해서 학생 100명의 점수 분포를 출력

import random

scores = []

for i in range(100):
    rn = random.randint(71, 100)
    if rn != 100: rn = rn - (rn % 5) # 점수를 5단위로 맞춤
    scores.append(rn)

print(f'scores: {scores}')
print(f'scores length: {len(scores)}')

# 최댓값 알고리즘
maxAl = md.QMaxAlgorithm(scores)
maxAl.setMaxIdxAndNum()
maxNum = maxAl.getMaxNum()
print(f'maxNum: {maxNum}')

# 인덱스 리스트 생성
indexes = [0 for i in range(maxNum + 1)]
print(f'indexes: {indexes}')
print(f'indexes length: {len(indexes)}')

# 인덱스 리스트에 빈도 저장
for n in scores:
    indexes[n] = indexes[n] + 1
print(f'indexes: {indexes}')


# 빈도수 별 찍기
n = 1
while True:

    maxAl = md.QMaxAlgorithm(indexes)
    maxAl.setMaxIdxAndNum()
    maxNum = maxAl.getMaxNum()
    maxNumIdx = maxAl.getMaxNumIdx()
    # print(f'maxNum: {maxNum}')
    # print(f'maxNumIdx: {maxNumIdx}')

    if maxNum == 0:
        break

    print(f'{n}. {maxNumIdx}빈도수: {maxNum}\t', end='')
    print('+' * maxNum)
    indexes[maxNumIdx] = 0

    n += 1

# 인덱스 Dic으로 생성
# dic_indexes = {n:0 for n in nums}
# print(dic_indexes)

dic_indexes = {}
for n in scores:
    if n not in dic_indexes: # dict에 해당 키가 없으면 +1연산을 할 수 없으므로 0으로 초기화 해준다.
        dic_indexes[n] = 0
    dic_indexes[n] += 1
print(f'dic_indexes: {dic_indexes}')

ordered_mode = {}
n = 1
while True:

    max_freq = 0; mode_num = 0
    for score, frequency in dic_indexes.items():
        if max_freq < frequency:
            max_freq = frequency
            mode_num = score

    if len(dic_indexes) == 0: break

    print(f'{n}. {mode_num:>3}점 빈도수: {max_freq:>2}\t' + ('+' * max_freq))

    # 해당 요소를 삭제해서 비교 횟수를 줄이고 빈도수로 정렬된 새로운 dict를 생성한다.
    ordered_mode[mode_num] = dic_indexes.pop(mode_num)
    n += 1

print(ordered_mode, dic_indexes)



# <EX> ----------------------------------------------------------------------------
# 최빈값 알고리즘을 이용해 나이 분포를 간단한 그래프로 출력하는 모듈
# 다음은 어떤 회사의 전직원 나이를 나타내는 리스트이다.

#import maxMod
#import module_mode as mode

ages = [25, 27, 27, 24, 31, 34, 33, 31, 29, 25,
        45, 37, 38, 46, 47, 22, 24, 29, 33, 35,
        27, 34, 37, 40, 42, 29, 27, 25, 26, 27,
        31, 31, 32, 38, 25, 27, 28, 40, 41, 34]

print(f'employee cnt: {len(ages)}명')

maxAlg = md.MaxAlgorithm(ages)
maxAlg.setMaxIdxAndNum()
maxAge = maxAlg.getMaxNum()
print(f'maxAge: {maxAge}세')

modAlg = md.ModeAlgorithm(ages, maxAge)
modAlg.setIndexList()
print(f'IndexList: {modAlg.getIndexList()}')

modAlg.printAges()
print()

myMode = md.myModeAlgorithm(ages, maxAge)
myMode.setIndexList()
print(f'IndexList: {myMode.getIndexList()}')

myMode.printAges()
print()

# <EX> ----------------------------------------------------------------------------
# 최빈도 알고리즘을 이용해 모든 회차의 각 번호에 대한 빈도수를 출력하는 프로그램

#import mod

# 다음은 회차별 로또 번호이다.
lottoNums = [[13, 23, 15, 5, 6, 39], [36, 13, 5, 3, 30, 16], [43, 1, 15, 9, 3, 38],
             [32, 42, 24, 45, 8, 31], [18, 39, 41, 11, 4, 9], [12, 39, 11, 38, 32, 5],
             [29, 25, 13, 6, 14, 8], [21, 33, 19, 20, 42, 7], [6, 28, 3, 45, 41, 24],
             [42, 15, 8, 5, 35, 4], [14, 4, 35, 24, 29, 3], [15, 20, 6, 37, 34, 39],
             [27, 5, 32, 15, 25, 19], [45, 25, 2, 8, 30, 43], [4, 19, 33, 10, 6, 24],
             [25, 26, 45, 23, 24, 16], [33, 28, 45, 21, 38, 24], [4, 30, 29, 28, 32, 38],
             [11, 28, 12, 2, 42, 3], [40, 29, 16, 8, 9, 28], [6, 9, 37, 30, 3, 35],
             [29, 18, 41, 28, 38, 15], [9, 31, 13, 44, 1, 36], [36, 1, 37, 32, 15, 12],
             [41, 32, 16, 6, 26, 33], [12, 43, 10, 29, 39, 9], [41, 9, 23, 35, 18, 17],
             [35, 38, 3, 28, 36, 31], [21, 44, 4, 29, 18, 7], [20, 23, 6, 2, 34, 44]]

lm = md.LottoMode(lottoNums)
mList = lm.getLottoNumMode()
print(f'mList: {mList}')

lm.printModeList()


