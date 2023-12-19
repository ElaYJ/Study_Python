import random

#excute_no = 1
excute_no = 2

if excute_no == 1:
    rNum1 = random.randint(100, 1000)
    rNum2 = random.randint(100, 1000)

    print(f'rNum1: {rNum1}')
    print(f'rNum2: {rNum2}')

    maxNum = 0
    # 둘 중 작은 수만큼만 돌면 된다.
    for n in range(1, (min(rNum1, rNum2) + 1)):
        if rNum1 % n == 0 and rNum2 % n == 0:
            print(f'공약수: {n}')
            maxNum = n

    print(f'최대공약수: {maxNum}')

    # 공통된 약수가 없다면 두 수는 서로소이다.
    if maxNum == 1:
        print(f'{rNum1}과 {rNum2}는 서로소이다.')


else:

    rNum1 = random.randint(1, 100)
    rNum2 = random.randint(1, 100)

    print(f'rNum1: {rNum1}')
    print(f'rNum2: {rNum2}')

    maxNum = 0
    for n in range(1, (min(rNum1, rNum2) + 1)):
        if rNum1 % n == 0 and rNum2 % n == 0:
            print(f'공약수: {n}')
            maxNum = n

    print(f'최대공약수: {maxNum}')

    minNum = (rNum1 * rNum2) // maxNum
    print('최소공배수: {}'.format(minNum))
