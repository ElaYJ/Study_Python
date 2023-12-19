'''
 # [군 수열(group sequence)]
'''

# inputN = int(input('n항 입력: '))
inputN = 50

n = 1 # 그룹: 1군, 2군, 3군, ...
nCnt = 1 # 전체 항의 개수
searchN = 0

flag = True
# 전체 항을 도는 while문
while flag:
    # 군을 도는 for문
    # 1군이면 1번, 2군이면 2번, ...
    print('{: >2}군: '.format(n), end='')
    for i in range(1, (n + 1)):
        if i == n: # 각 군의 마지막 항에는 콤마 생략
            print('{} '.format(i), end='')
        else:
            print('{}, '.format(i), end='')

        nCnt += 1
        if (nCnt > inputN):
            searchN = i
            flag = False
            break

    print() # 한 군이 끝나면 개행
    n += 1

print('{}항: {}'.format(inputN, searchN))




# inputN = int(input('n항 입력: '))
inputN = 25

n = 1; nCnt = 1
searchNC = 0; searchNP = 0 # 분자값과 분모값을 각각 따로 구한다.

flag = True
while flag:

    print('{: >2}군: '.format(n), end='')
    for i in range(1, (n + 1)):
        if i == n:
            print('{}/{} '.format(i, (n - i + 1)), end='')
        else:
            print('{}/{}, '.format(i, (n - i + 1)), end='')

        nCnt += 1
        if (nCnt > inputN):
            searchNC = i
            searchNP = n - i + 1
            flag = False
            break

    print()
    n += 1

print('{}항: {}/{}'.format(inputN, searchNC, searchNP))
