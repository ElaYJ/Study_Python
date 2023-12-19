'''
 # [자료구조] Container Data Type
'''

# List
student1 = '홍길동'
student2 = '박찬호'
student3 = '이용규'
student4 = '박승철'
student5 = '김지은'

students = ['홍길동', '박찬호', '이용규', '박승철', '김지은']
print('students: {}'.format(students))
print('type of students: {}'.format(type(students)))

for student in students:
    print('student : {}'.format(student))


# Tuple - 요소 변경 불가 (한번 정해진 정보는 수정할 수 었다.)
job1 = '의사'
job2 = '속기사'
job3 = '전기기사'
job4 = '감정평가사'
job5 = '회계사'

jobs = ('의사', '속기사', '전기기사', '감정평가사', '회계사')
print('jobs: {}'.format(jobs))
print('type of jobs: {}'.format(type(jobs)))

for job in jobs:
    print('job : {}'.format(job))


# Dictionary - {Key : Value} 형태
korScore = 88
engScore = 91
matScore = 95
sciScore = 90
hisScore = 100

scores = {'kor':88, 'eng':91, 'mat':95, 'sci':90, 'his':100}
print('scores: {}'.format(scores))
print('type of scores: {}'.format(type(scores)))

for score in scores.keys():
    print('{} : {}'.format(score, scores[score]))


# Set - 데이터 중복을 허용하지 않는다.
sales1 = 100
sales2 = 150
sales3 = 90
sales4 = 110

allSales = {100, 150, 90, 110}
print('allSales: {}'.format(allSales))
print('type of allSales: {}'.format(type(allSales)))

for sales in allSales:
    print('sales : {}'.format(sales))
