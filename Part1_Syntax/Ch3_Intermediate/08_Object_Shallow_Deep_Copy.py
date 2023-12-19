'''
 # [객체의 얕은 복사와 깊은 복사]
    ▶ 얕은 복사란? 객체의 메모리 주소를 복사하는 것으로 객체 자체가 복사되지 않는다.
    ▶ 깊은 복사란? 객체 자체를 복사하는 것으로 또 하나의 객체가 복사되어 만들어 진다.
    ▶ copy 모듈을 이용하면 객체를 복사하는 깊은 복사가 가능하다.
    ▶ 리스트의 copy() 메소드는 주소가 아니라 실제 객체가 복사된다. -> 깊은 복사
'''

list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]
print('-- Shallow Copy --')
# 얕은 복사 : lis3과 list1은 동일 객체를 가리킨다.
list3 = list1

print(f'list1: {list1}')
print(f'list2: {list2}')
print(f'list3: {list3}')

list1.append(6)
print(f'list1: {list1}')
print(f'list2: {list2}')
print(f'list3: {list3}')

list3[2] = 3.14
print(f'list1: {list1}')
print(f'list2: {list2}')
print(f'list3: {list3}')

list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]
print('-- Deep Copy --')
# 깊은 복사 : list3과 list1은 서로 다른 객체를 가리킨다.
list3 = list1.copy()
print(f'list1: {list1}')
print(f'list2: {list2}')
print(f'list3: {list3}')

list1[2] = 3.14
print(f'list1: {list1}')
print(f'list2: {list2}')
print(f'list3: {list3}')

list3[4] = 999
print(f'list1: {list1}')
print(f'list2: {list2}')
print(f'list3: {list3}')
print()


# <Q> -----------------------------------------------------------------------------------------
# 국어, 영어, 수학 점수를 입력받아 리스트에 저장하고 원본을 유지한 상태로,
# 복사본을 만들어 과목별 점수를 10% 올렸을 경우에 평균을 출력해 보자.

# scores = [int(input('국어 점수 입력: ')),
#           int(input('영어 점수 입력: ')),
#           int(input('수학 점수 입력: '))]
scores = [77, 82, 91] # 원본
copyScores = scores.copy() # 복사본

for idx, score in enumerate(copyScores):
    result = score * 1.1
    copyScores[idx] = 100 if result > 100 else result

print(f'이전 평균: {round(sum(scores) / len(scores), 2)}')
print(f'이후 평균: {round(sum(copyScores) / len(copyScores), 2)}')
print()


# copy Module ---------------------------------------------------------------------------------
# copy 모듈을 이용해 깊은 복사를 할 수 있다.
class TempClass:

    def __init__(self, num, str):
        self.number = num
        self.str = str

    def printClsInfo(self):
        print(f'self.number: {self.number}')
        print(f'self.str: {self.str}')
        print()


tc1 = TempClass(10, 'Hello')
# 얕은 복사
tc2 = tc1

print('-- Shallow Copy --')
tc1.printClsInfo()
tc2.printClsInfo()

tc2.number = 3.14
tc2.str = 'Bye'

tc1.printClsInfo()
tc2.printClsInfo()
print()

import copy

tc1 = TempClass(10, 'Hello')
# 깊은 복사
tc2 = copy.copy(tc1)

print('-- Deep Copy --')
tc1.printClsInfo()
tc2.printClsInfo()

tc2.number = 3.14
tc2.str = 'Bye'

tc1.printClsInfo()
tc2.printClsInfo()
print()


# 리스트와 관련된 깊은 복사 방법 -----------------------------------------------

scores = [9, 8, 5, 7, 6, 10]
scoresShallowCopy = []

print('-- Shallow Copy --')
scoresShallowCopy = scores
print(f'id(scores) \t\t\t : {id(scores)}')
print(f'id(scoresShallowCopy): {id(scoresShallowCopy)}')
# id() 함수로 메모리 주소값 출력

print('-- Deep Copy --')

# case_1.
scoresDeepCopy = []
# for문 사용 : 다른 객체에 값만 복사
for s in scores:
    scoresDeepCopy.append(s)
print(f'id(scores)  \t  : {id(scores)}')
print(f'id(scoresDeepCopy): {id(scoresDeepCopy)}')
print('-' * 15)

# case_2.
scoresDeepCopy = []
# extend()로 리스트 연결 확장
scoresDeepCopy.extend(scores)
print(f'id(scores)  \t  : {id(scores)}')
print(f'id(scoresDeepCopy): {id(scoresDeepCopy)}')
print('-' * 15)

# case_3.
scoresDeepCopy = []
# 리스트의 copy() 메소드 사용
scoresDeepCopy = scores.copy()
print(f'id(scores)  \t  : {id(scores)}')
print(f'id(scoresDeepCopy): {id(scoresDeepCopy)}')
print('-' * 15)

# case_4.
scoresDeepCopy = []
# 처음부터 끝까지 slicing한 데이터 할당
scoresDeepCopy = scores[:]
print(f'id(scores)  \t  : {id(scores)}')
print(f'id(scoresDeepCopy): {id(scoresDeepCopy)}')
print()


# <Q> -----------------------------------------------------------------------------------------
# 선수의 원본 점수를 이용해서 평균을 출력하고, 최고값과 최저값을 제외한 평균을 출력하는 프로그램

player_orig_scores = [8.7, 9.1, 8.9, 9.0, 7.9, 9.5, 8.8, 8.3]
player_copy_scores = player_orig_scores.copy()

player_orig_scores.sort()

player_copy_scores.sort()
player_copy_scores.pop() # 최고값 제거
player_copy_scores.pop(0) # 최저값 제거

print(f'player_orig_scores: {player_orig_scores}')
print(f'player_copy_scores: {player_copy_scores}')


oriTot = round(sum(player_orig_scores), 2)
oriAvg = round(oriTot / len(player_orig_scores), 2)
print(f'Original Total: {oriTot}')
print(f'Original Average: {oriAvg}')

copTot = round(sum(player_copy_scores), 2)
copAvg = round(oriTot / len(player_copy_scores), 2)
print(f'Copy Total: {copTot}')
print(f'Copy Average: {copAvg}')

print(f'oriAvg - copAvg: {oriAvg - copAvg}')