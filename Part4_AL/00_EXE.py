import random

datas = [3, 2, 5, 7, 9, 1, 0, 8, 6, 4]
nums = (4, 7, 10, 2, 4, 7, 0, 2, 7, 3, 9)

result1 = datas + [127,]
result2 = nums + (127,)
print(result1)
print(result2)

datas += (127,)
nums += (127,)
print(datas)
print(result2)


ranks = [0 for i in range(20)]
print(ranks)

import random as rd
students = [rd.randint(170, 185) for i in range(20)]
print(students)

#indexes = [0 for i in range(maxNum + 1)]
indexes = [0] * 10
print(indexes)


cs = ['c', 'x', 'Q', 'A', 'e', 'P', 'p']
asciis = [ord(c) for c in cs]
print(asciis)

scores = [random.randint(30,100) for i in range(5)]
print(scores)

scores = []
for i in range(100):
    r_nums = random.randint(71, 100)
    if r_nums != 100: r_nums = r_nums - (r_nums % 5) # 점수를 5단위로 맞춤
    scores.append(r_nums)

dic_indexes = {}
for n in scores:
    if n not in dic_indexes:
        dic_indexes[n] = 0
    dic_indexes[n] += 1
print(f'indexes: {dic_indexes}')



