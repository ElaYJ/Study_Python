'''
 # [순위]
'''
import random

scores = random.sample(range(50, 101), 10)
ranks = [0 for i in range(10)]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


for idx, sco1 in enumerate(scores):
    for sco2 in scores:
        if sco1 < sco2:
            ranks[idx] += 1

print(scores)
print(ranks)

for i, s in enumerate(scores):
    print(f'score:{s} \t rank:{ranks[i] + 1}')
print()

#------------------------------------------------------------------------
# ChatGPT 구현 코드

def selection_sort_with_rank(items):
    n = len(items)
    ranks = [0] * n

    for i in range(n):
        current_rank = 1
        for j in range(n):
            if i != j:
                if items[i] < items[j]:
                    current_rank += 1

        ranks[i] = current_rank

    return ranks

# 예시
scores = [80, 95, 70, 85]
ranks = selection_sort_with_rank(scores)

for i, rank in enumerate(ranks):
    print(f"Item {i+1}: Score {scores[i]}, Rank {rank}")
print()




if __name__ == '__main__':

# <Q> -----------------------------------------------------------------------
# 학급 학생(20명)들의 중간고사와 기말고사 성적을 이용해서 각각의 순위를 구하고,
# 중간고사 대비 기말고사 순위 변화(편차)를 출력하는 프로그램 (시험 성적은 난수를 이용한다.)

    import module_sort_ranking as rm
    import random

    midStuScos = random.sample(range(50, 101), 20)
    endStuScos = random.sample(range(50, 101), 20)

    rd = rm.RankDeviation(midStuScos, endStuScos)

    rd.setMidRank()
    print(f'midStuScos: {midStuScos}')
    print(f'mid_rank: {rd.getMidRank()}')

    rd.setEndRank()
    print(f'endStuScos: {endStuScos}')
    print(f'end_rank: {rd.getEndRank()}')

    rd.printRankDeviation()

    print()


# <EX> -------------------------------------------------------------------------------
# 숫자로 이루어진 리스트에서 Item(요소)의 순위를 출력하고,
# 순위에 따라 Item(요소)를 정렬하는 모듈을 만든다. 리스트는 50부터 100까지의 난수 20개를 이용한다.

    nums = random.sample(range(50, 101), 10)
    sNums = rm.rankAlgorithm(nums)
    print(f'sNums: {sNums}')


# <EX> -------------------------------------------------------------------------------
# 알파벳 문자들과 정수들에 대한 순위를 정하는 프로그램을 순위 알고리즘을 이용해 구현
# 단, 알파벳은 아스키코드 값을 이용한다

datas = [32, 'a', 'z', 45, 'G', 39, 50, 'T', 't', 22, 31, 55, 's', 63, 59, 'E']
print(f'datas: {datas}')

ascIIDatas = []
for data in datas:
    if str(data).isalpha():
        ascIIDatas.append(ord(data))
        continue

    ascIIDatas.append(data)

print(f'ascIIDatas: {ascIIDatas}')


ranks = [0 for i in range(len(ascIIDatas))]

for idx, data1 in enumerate(ascIIDatas):
    for data2 in ascIIDatas:
        if data1 < data2:
            ranks[idx] += 1

print(f'ranks: {ranks}')

for i, d in enumerate(datas):
    print(f'data: {d:>2} \t rank:{ranks[i] + 1:>2}')


