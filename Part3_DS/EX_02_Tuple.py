'''
 # [연습문제]
'''

exe_no = int(input('EXE NO. '))

if exe_no == 1:
# <Q1> ---------------------------------------------------------------------------------------------
# 자주 접속하는 웹사이트 비번을 튜플에 저장

    passwds = ('password1234', 'abc123', 'qwerty', 'letmein', 'welcome00')
    print(f'passwds : {passwds}')



elif exe_no == 2:
# <Q2> ---------------------------------------------------------------------------------------------
# 졸업 때 4.0이상의 학점을 받기 위해 길동이가 받아야 하는 4학년 1, 2학기의 최소 학점 구하기

    # 대학생 길동이의 1, 2, 3학년 성적
    scores = ((3.7, 4.2), (2.9, 4.3), (4.1, 4.2))
    total = 0

    for s1 in scores:
        for s2 in s1:
            total += s2

    total = round(total, 1)
    avg = round((total / 6), 1)
    print(f'3학년 총학점: {total}')
    print(f'3학년 평균: {avg}')

    print('-'*60)

    grade4TagetScore = round((4.0 * 8 - total), 1)
    print(f'4학년 목표 총학점: {grade4TagetScore}')

    minScore = round(grade4TagetScore / 2, 1)
    print(f'4학년 한학기 최소학점: {minScore}')

    scores = list(scores)
    scores.append((minScore, minScore))

    print('-'*60)

    scores = tuple(scores)
    print(f'scores: {scores}')



elif exe_no == 3:
# <Q3> ---------------------------------------------------------------------------------------------
# 2개의 튜플에 대한 합집합과 교집합 출력

    # case_1
    tuple1 = (1, 3, 2, 6, 12, 5, 7, 8)
    tuple2 = (0, 5, 2, 9, 8, 6, 17, 3)

    tempHap = list(tuple1)
    tempGyo = list()

    for n in tuple2:
        if n not in tempHap:
            tempHap.append(n)
        else:
            tempGyo.append(n)

    tempHap = tuple(sorted(tempHap))
    tempGyo = tuple(sorted(tempGyo))

    print(f'합집합(중복X) : {tempHap}')
    print(f'교집합\t\t : {tempGyo}')

    # case_2
    tuple1 = (1, 3, 2, 6, 12, 5, 7, 8)
    tuple2 = (0, 5, 2, 9, 8, 6, 17, 3)

    tempHap = tuple1 + tuple2
    print(f'tuple1 + tuple2 : {tempHap}')
    tempHap = list(tempHap)
    print(f'list(tempHap)  : {tempHap}')

    tempGyo = list()

    for n in tempHap:
        if tempHap.count(n) > 1:
            tempGyo.append(n)
            tempHap.remove(n)

    print(f'tempHap : {tempHap}')
    print(f'tempGyo : {tempGyo}')

    print(f'합집합 : {tuple(sorted(tempHap))}')
    print(f'교집합 : {tuple(sorted(tempGyo))}')





elif exe_no == 4:
# <Q4> ---------------------------------------------------------------------------------------------
# 다음 요구 사항에 맞춰 아이템을 슬라이스
# index 0부터 3까지
# index 2부터 4까지
# index 3부터 끝까지
# index 2부터 뒤에서 -2까지
# index 0부터 끝까지 3단계

    numbers = (8.7, 9.0, 9.1, 9.2, 8.6, 9.3, 7.9, 8.1, 8.3)

    #index: 0 ~ 3
    print(f'numbers[:4] : {numbers[0:4]}')

    #index: 2 ~ 4
    print(f'numbers[2:5] : {numbers[2:5]}')

    #index: 3 ~ end
    print(f'numbers[3:] : {numbers[3:]}')

    #index: 2 ~ end-2
    print(f'numbers[2:-1] : {numbers[2:-1]}')

    #index: 0 ~ end, step = 3
    print(f'numbers[::3] : {numbers[::3]}')


    # 최솟값
    print(f'최솟값 : {min(numbers)}')
    print(f'최솟값 인덱스 : {numbers.index(min(numbers))}')

    # 최댓값
    print(f'최댓값 : {max(numbers)}')
    print(f'최댓값 인덱스 : {numbers.index(max(numbers))}')



elif exe_no == 5:
# <Q5> ---------------------------------------------------------------------------------------------
# 시험 점수를 입력한 후 튜플에 저장하고 과목별 학점을 출력

    korScore = int(input('국어 점수 입력: '))
    engScore = int(input('영어 점수 입력: '))
    matScore = int(input('수학 점수 입력: '))
    sciScore = int(input('과학 점수 입력: '))
    hisScore = int(input('국사 점수 입력: '))

    scores = ({'kor':korScore},
              {'eng':engScore},
              {'mat':matScore},
              {'sci':sciScore},
              {'his':hisScore})

    print(f'scores: {scores}')

    for item in scores:
        for key in item.keys():
            if item[key] >= 90:
                item[key] = 'A'
            elif item[key] >= 80:
                item[key] = 'B'
            elif item[key] >= 70:
                item[key] = 'C'
            elif item[key] >= 60:
                item[key] = 'D'
            else:
                item[key] = 'F'

    print(f'scores: {scores}')



elif exe_no == 6:
# <Q6> ---------------------------------------------------------------------------------------------
# 튜플의 과일 개수에 대해 오름차순 및 내림차순으로 정렬 : 버블정렬 사용

    fruits = ({'수박':8}, {'포도':13}, {'참외':12}, {'사과':17}, {'자두':19}, {'자몽':15})
    fruits = list(fruits)

    cIdx = 0 # current index 현재 인덱스
    nIdx = 1 # next index 다음 인덱스
    eIdx = len(fruits) - 1 # end index 마지막 인덱스

    flag = True
    while flag:
        curDic = fruits[cIdx] # {'수박':8}
        nextDic = fruits[nIdx] # {'포도':13}

        curDicCnt = list(curDic.values())[0] # 8
        nextDicCnt = list(nextDic.values())[0] # 13

        # 오름차순 정렬 : nextDicCnt < curDicCnt
        # 내림차순 정렬 : nextDicCnt > curDicCnt
        if nextDicCnt < curDicCnt:
            fruits.insert(cIdx, fruits.pop(nIdx))
            nIdx = cIdx + 1
            continue

        nIdx += 1
        if nIdx > eIdx:
            cIdx += 1
            nIdx = cIdx + 1

            if cIdx == eIdx:
                flag = False

    print(tuple(fruits))



elif exe_no == 7:
# <Q7> ---------------------------------------------------------------------------------------------
# 학급별 학생 수를 나타낸 튜플을 이용해 요구 사항에 맞는 데이터를 출력하는 프로그램
# - 전체 학생 수, 평균 학생 수, 학생 수가 가장 적은 학급, 학생 수가 가장 많은 학급, 학급별 학생 편차

    studentCnt = ({'cls01':18},
                  {'cls02':21},
                  {'cls03':20},
                  {'cls04':19},
                  {'cls05':22},
                  {'cls06':20},
                  {'cls07':23},
                  {'cls08':17})

    totalCnt = 0
    minStdCnt = 0; minCls = ''
    maxStdCnt = 0; maxCls = ''
    deviation = [] # 편차

    for idx, dic in enumerate(studentCnt):
        for k, v in dic.items():
            # 전체 학생 수
            totalCnt += v

            # 가장 작은 학생수와 학급
            if idx == 0 or minStdCnt > v:
                minStdCnt = v
                minCls = k

            # 가장 많은 학생수와 학급
            if maxStdCnt < v:
                maxStdCnt = v
                maxCls = k

    print(f'전체 학생 수: {totalCnt}명')

    avgCnt = totalCnt/len(studentCnt)
    print(f'평균 학생 수: {round(avgCnt, 2)}명')

    print(f'학생 수가 가장 적은 학급: {minCls}({minStdCnt}명)')
    print(f'학생 수가 가장 많은 학급: {maxCls}({maxStdCnt}명)')

    for idx, dic in enumerate(studentCnt):
        for k, v in dic.items():
            deviation.append({k:round(v-avgCnt, 2)})

    print(f'학급별 학생 편차: {deviation}')


