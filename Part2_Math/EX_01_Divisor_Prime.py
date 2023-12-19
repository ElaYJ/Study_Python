import random

#rNum = random.randint(10, 100)
rNum = 10

print(f'randomNum: {rNum}')

for num in range(1, rNum+1):

    soinsuFlag = 0

    # 약수
    if rNum % num == 0:
        print('{: >2}: [약수]'.format(num))
        soinsuFlag += 1

    # 소수
    if num != 1:
        flag = True # 일단 소수가 맞다고 가정한 후
        for n in range(2, num): # 약수를 가지는지 확인
            if num % n == 0: # 약수가 존재하면
                flag = False # 소수가 아니다!
                break

        if (flag):
            print('{: >2}: \t  [소수]'.format(num))
            soinsuFlag += 1

    # 소인수: 약수(인수)이면서 소수
    if soinsuFlag >= 2:
        print('{: >2}: \t\t\t[소인수]'.format(num))
