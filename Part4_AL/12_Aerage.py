'''
 # [평균] 여러 수나 양의 중간값을 갖는 수
'''
import random

nums = random.sample(range(0, 100), 30)
print(f'nums: {nums}')

total = 0
for n in nums:
    total += n

average = total / len(nums)
print(f'average: {round(average, 2)}\n')


# 50이상 90이하 수들의 평균
nums = random.sample(range(0, 100), 30)
print(f'nums: {nums}')

targetNums = []
total = 0
for n in nums:
    if n >= 50 and n <= 90:
        total += n
        targetNums.append(n)

print(f'targetNums: {targetNums}')
average = total / len(targetNums)
print(f'average: {round(average, 2)}\n')


# 정수들의 평균
nums = [4, 5.12, 0, 5, 7.34, 9.1, 9, 3, 3.159, 1, 11, 12.789]
print(f'nums: {nums}')

targetNums = []
total = 0
for n in nums:
    if n - int(n) == 0: # 정수라면,
        total += n
        targetNums.append(n)

print(f'targetNums: {targetNums}')
average = total / len(targetNums)
print(f'average: {round(average, 2)}\n')


# 실수(소수)들의 평균
nums = [4, 5.12, 0, 5, 7.34, 9.1, 9, 3, 3.159, 1, 11, 12.789]
print(f'nums: {nums}')

targetNums = []
total = 0
for n in nums:
    if n - int(n) != 0:
        total += n
        targetNums.append(n)

print(f'targetNums: {targetNums}')
average = total / len(targetNums)
print(f'average: {round(average, 2)}\n')



import module_average as avg

# <Q> -----------------------------------------------------------------------------
# 평균을 구하고 순위를 정하는 알고리즘
# 다음은 어떤 체조선수의 점수이다

scores = (8.9, 7.6, 8.2, 9.1, 8.8, 8.1, 7.9, 9.4, 7.2, 8.7)
top5PlayerScores = [9.12, 8.95, 8.12, 7.90, 7.88]

print(f'Current scores: {top5PlayerScores}')

total = 0
average = 0

for n in scores:
    total += n

average = round(total / len(scores), 2)

print(f'total: {total}')
print(f'average: {average}')

tp = avg.Top5Players(top5PlayerScores, average)
tp.setAlignScore()
top5PlayerScores = tp.getFinalTop5Scores()
print(f'Final scores: {top5PlayerScores}')
print()



# <EX> ----------------------------------------------------------------------------
# 최댓값과 최솟값을 제외한 나머지 점수에 대한 평균을 구하고 순위를 정하는 알고리즘
# 다음은 어떤 체조선수의 경기 점수이다.

top5Scores = [9.12, 8.95, 8.12, 6.90, 6.18]
scores = [6.7, 5.9, 8.1, 7.9, 6.7, 7.3, 7.2, 8.2, 6.2, 5.8]
print(f'scores: {scores}')

# 최댓값 제거
maxA = avg.MaxDelAlgorithm(scores)
maxA.removeMaxScore()

# 최솟값 제거
minA = avg.MinDelAlgorithm(scores)
minA.removeMinScore()

# 평균 구하기
total = 0
average = 0

for n in scores:
    total += n

average = round(total / len(scores), 2)

print(f'total: {round(total, 2)}')
print(f'average: {average}')

# 내 평균 끼워넣기
tp = avg.Top5Players(top5Scores, average)
tp.setAlignScore()
top5Scores = tp.getFinalTop5Scores()
print(f'top5Scores: {top5Scores}')
print()



# <EX> ----------------------------------------------------------------------------
# 홍길동 학생을 제외한 나머지 학생의 평균과 홍길동 학생의 점수의 차이를 출력하는 프로그램
# 출력은 과목별 점수와 평균 점수를 모두 출력한다.
# 다음은 홍길동 학생을 포함한 학급 전체 학생의 시험 점수 평균을 나타낸 표이다.

kor_avg = 88; eng_avg = 82; mat_avg = 90
sci_avg = 78; his_avg = 92

hong_kor_score = 85; hong_eng_score = 90; hong_mat_score = 82
hong_sci_score = 88; hong_his_score = 100

# 홍길동을 제외한 학생들의 과목별 총점
stu19cnt_kor_total = kor_avg * 20 - hong_kor_score
stu19cnt_eng_total = eng_avg * 20 - hong_eng_score
stu19cnt_mat_total = mat_avg * 20 - hong_mat_score
stu19cnt_sci_total = sci_avg * 20 - hong_sci_score
stu19cnt_his_total = his_avg * 20 - hong_his_score

# 홍길동을 제외한 학생들의 과목별 평균
stu19cnt_kor_avg = stu19cnt_kor_total / 19
stu19cnt_eng_avg = stu19cnt_eng_total / 19
stu19cnt_mat_avg = stu19cnt_mat_total / 19
stu19cnt_sci_avg = stu19cnt_sci_total / 19
stu19cnt_his_avg = stu19cnt_his_total / 19

# 홍길동과 나머지 학생들의 과목별 점수차
kor_gap = hong_kor_score - stu19cnt_kor_avg
eng_gap = hong_eng_score - stu19cnt_eng_avg
mat_gap = hong_mat_score - stu19cnt_mat_avg
sci_gap = hong_sci_score - stu19cnt_sci_avg
his_gap = hong_his_score - stu19cnt_his_avg
print(f'국어 점수 차이: {"+" + str(round(kor_gap, 2)) if kor_gap > 0 else round(kor_gap, 2)}')
print(f'영어 점수 차이: {"+" + str(round(eng_gap, 2)) if eng_gap > 0 else round(eng_gap, 2)}')
print(f'수학 점수 차이: {"+" + str(round(mat_gap, 2)) if mat_gap > 0 else round(mat_gap, 2)}')
print(f'과학 점수 차이: {"+" + str(round(sci_gap, 2)) if sci_gap > 0 else round(sci_gap, 2)}')
print(f'국사 점수 차이: {"+" + str(round(his_gap, 2)) if his_gap > 0 else round(his_gap, 2)}')

# 19명의 평균 구하기
stu19Cnt_total = stu19cnt_kor_avg + stu19cnt_eng_avg + stu19cnt_mat_avg + stu19cnt_sci_avg + stu19cnt_his_avg
stu19Cnt_avg = stu19Cnt_total / 5
# 홍길동의 평균 구하기
hong_total = hong_kor_score + hong_eng_score + hong_mat_score + hong_sci_score + hong_his_score
hong_avg = hong_total / 5

# 홍길동과 나머지 학생들의 평균차
avg_gap = round(hong_avg - stu19Cnt_avg, 2)
print(f'평균 차이: {"+" + str(round(avg_gap, 2)) if avg_gap > 0 else round(avg_gap, 2)}')

