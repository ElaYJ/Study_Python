num_list = [3, 4, 5]
min_val = min(num_list)
print(min_val)

ship1 = 72; ship2 = 54; ship3 = 12 # 주기
min_val = min(ship1, ship2, ship3)
print(min_val)

students = ['홍길동', '강호동', '박찬호', '이용규', '박승철', '강호동', '김지은']

del students[1]
print('students: {}'.format(students))

del students[3]
print('students: {}'.format(students))

students = ['홍길동', '강호동', '박찬호', '이용규', '박승철', '강호동', '김지은']
del students[1:4]
print('students: {}'.format(students))

students = ['홍길동', '강호동', '박찬호', '이용규', '박승철', '강호동', '김지은']
del students[2:]
print('students: {}'.format(students))

students = ['홍길동', '강호동', '박찬호', '이용규', '박승철', '강호동', '김지은']
print(students)

students.clear()
print(students)


ranks = (0 for i in range(10))
print(ranks)

indexes = (0,) * 10
print(indexes)

import random
scores = (random.randint(50,101) for i in range(5))
print(scores)


myList = [ '마케팅 회의'
         , '회의록 정리'
         , '점심 약속'
         , '월간 업무 보고'
         , '치과 방문'
         , '마트 장보기']
print('일정 : {}'.format(myList))

removeItem = myList[random.randrange(len(myList))]
print(removeItem)

task = random.choice(myList)
print(task)

types = ['A', 'B', 'AB', 'O']
todayData = []

for i in range(10):
    todayData.append(random.choice(types))
print(todayData)

todayData.clear()
todayData = [random.choice(types) for i in range(10)]
print(todayData)

todayData.clear()
for i in range(10):
    btype = types[random.randrange(len(types))]
    todayData.append(btype)
print(todayData)

strs = [3.14, '십', 20, 'one', '3.141592', [20, 30], (40, 50, 60)]
print(strs)

studentTuple = ('홍길동', '박찬호', '이용규')
print(studentTuple * 3)

list_ex = [1, 2, 3, 4, 5]
print(list_ex)

item1, item2, item3, item4, item5 = list_ex
print(item1, item2, item3, item4, item5)

list_ex = item1, item2, item3, item4, item5
print(list_ex)

numbers = (8.7, 9.0, 9.1, 9.2, 8.6, 9.3, 7.9, 8.1, 8.3)

# <index: 0 ~ 3>
print(f'numbers[:4] : {numbers[0:4]}')
print(f'numbers[:4] : {type(numbers[0:4])}')

mixed_dict = {
    'name': 'Alice',
    'age': 25,
    'grades': [95, 88, 92],
    (1, 2): 'tuple_key',
    3.14: 'pi_value'
}

# Dictionary 순회(iterate)
for key, value in mixed_dict.items():
    print(f'{key}: {value}')
