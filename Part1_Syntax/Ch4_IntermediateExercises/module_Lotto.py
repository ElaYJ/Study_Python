import random

userNums = []; randNums = []
winningNums = [] # the winning lottery numbers (복권 당첨 번호)
randBonusNum = 0

def setUserNums(ns):
    global userNums
    userNums = ns

def getUserNums():
    return userNums

def setRandNums():
    global randNums
    randNums = random.sample(range(1, 46), 6)

def getRandNums():
    return randNums

def setBonusNum():
    global randBonusNum

    while True:
        randBonusNum = random.randint(1, 45)
        if randBonusNum not in randNums:
            break

def getBonusNum():
    return randBonusNum

def lottoResult():
    global userNums
    global randNums
    global winningNums

    winningNums = []
    for un in userNums:
        if  un in randNums:
            winningNums.append(un)

    if len(winningNums) == 6:
        print(f'1등 담첨!!')
        print(f'번호: {winningNums}')

    elif (len(winningNums) == 5) and (randBonusNum in userNums):
        print(f'2등 담첨!!')
        print(f'번호: {winningNums}, 보너스 번호: {randBonusNum}')

    elif len(winningNums) == 5:
        print(f'3등 담첨!!')
        print(f'번호: {winningNums}')

    elif len(winningNums) == 4:
        print(f'4등 담첨!!')
        print(f'번호: {winningNums}')

    if len(winningNums) == 3:
        print(f'5등 담첨!!')
        print(f'번호: {winningNums}')

    else:
        print('아쉽습니다. 다음 기회에~')
        print(f'기계 번호: {randNums}')
        print(f'보너스 번호: {randBonusNum}')
        print(f'선택 번호: {userNums}')
        print(f'일치 번호: {winningNums}')


def startLotto():
    n1 = int(input('번호(1~45) 입력: '))
    n2 = int(input('번호(1~45) 입력: '))
    n3 = int(input('번호(1~45) 입력: '))
    n4 = int(input('번호(1~45) 입력: '))
    n5 = int(input('번호(1~45) 입력: '))
    n6 = int(input('번호(1~45) 입력: '))
    selectNums = [n1, n2, n3, n4, n5, n6]

    setUserNums(selectNums)
    setRandNums()
    setBonusNum()

    lottoResult()