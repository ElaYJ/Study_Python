'''
 # [리스트]
'''
import random

exe_no = int(input('EXE NO. '))
if  exe_no == 1:
# 리스트 선언 ==========================================================================================

    students = ['홍길동', '박찬호', '이용규', '박승철', '김지은']
    print('students: {}'.format(students))

    numbers = [10, 20, 30, 40, 50, 60, 70]
    print('numbers: {}'.format(numbers))

    strs = [3.14, '십', 20, 'one', '3.141592']
    print('strs: {}'.format(strs))

    datas = [10, 20, 30, [40, 50, 60]]
    print('datas: {}'.format(datas))

    myFamilyNames = ['홍아빠', '홍엄마', '홍길동', '홍동생']
    print(myFamilyNames)

    todaySchedule = ['10시-업무회의',
                     '12시-친구와점심약속',
                     '3시-자료정리',
                     '6시-운동', '9시-TV시청']
    print(todaySchedule)


# 리스트 초기화
    ranks = [0 for i in range(10)]
    print(ranks)

    indexes = [0] * 10
    print(indexes)

    import random
    scores = [random.randint(50,101) for i in range(5)]
    print(scores)


elif  exe_no == 2:
# 인덱스 ==============================================================================================
# 인덱스를 이용해 리스트의 이이템을 조회

    students = ['홍길동', '박찬호', '이용규', '박승철', '김지은']

    print('students[0]: {}'.format(students[0]))
    print('students[1]: {}'.format(students[1]))
    print('students[2]: {}'.format(students[2]))
    print('students[3]: {}'.format(students[3]))
    print('students[4]: {}'.format(students[4]))
    # 잘못된 인덱스 사용으로 인해 Error! 발생
    # print('students[5]: {}'.format(students[5]))

    numbers = [10, 20, 30, 40, 50, 60, 70]

    print('numbers[0]: {}'.format(numbers[0]))
    print('numbers[1]: {}'.format(numbers[1]))
    print('numbers[2]: {}'.format(numbers[2]))
    print('numbers[3]: {}'.format(numbers[3]))
    print('numbers[4]: {}'.format(numbers[4]))
    print('numbers[5]: {}'.format(numbers[5]))
    print('numbers[6]: {}'.format(numbers[6]))
    # print('numbers[7]: {}'.format(numbers[7]))

    strs = [3.14, '십', 20, 'one', '3.141592']

    print('strs[0]: {}'.format(strs[0]))
    print('strs[1]: {}'.format(strs[1]))
    print('strs[2]: {}'.format(strs[2]))
    print('strs[3]: {}'.format(strs[3]))
    print('strs[4]: {}'.format(strs[4]))
    # print('strs[5]: {}'.format(strs[5]))

    datas = [10, 20, 30, [40, 50, 60]]

    print('datas[0]: {}'.format(datas[0]))
    print('datas[1]: {}'.format(datas[1]))
    print('datas[2]: {}'.format(datas[2]))
    print('datas[3]: {}'.format(datas[3]))

    print('datas[3][0]: {}'.format(datas[3][0]))
    print('datas[3][1]: {}'.format(datas[3][1]))
    print('datas[3][2]: {}'.format(datas[3][2]))


# <Q> ------------------------------------------------------------------------------------------------
# 5명의 학생 이름을 리스트에 저장하고 인덱스가 홀수인 학생과 짝수(0포함)인 학생을 구분해서 인덱스와 학생 이름을 출력

    students = ['김성예', '신경도', '박기준', '최승철', '황동석']
    print('- 인덱스가 짝수인 학생 --')
    print(' students[0] : {}'.format(students[0]))
    print(' students[2] : {}'.format(students[2]))
    print(' students[4] : {}'.format(students[4]))
    print('- 인덱스가 홀수인 학생 --')
    print(' students[1] : {}'.format(students[1]))
    print(' students[3] : {}'.format(students[3]))

    # 위 출력 방법을 for문으로 변경
    for i in range(5):
        if i % 2 == 0:
            print('인덱스 짝수 : students[{}] : {}'.format(i, students[i]))
        else:
            print('인덱스 홀수 : students[{}] : {}'.format(i, students[i]))



elif  exe_no == 3:
# 리스트 길이 =========================================================================================
# 리스트의 아이템 개수를 학인 --> 내장함수 len() 사용 -> int 반환

    students = ['홍길동', '박찬호', '이용규', '박승철', '김지은']
    sLength = len(students)
    print('length of students : {}'.format(sLength))

    for i in range(len(students)):
        print('i : {}'.format(i))
        print('students[{}] : {}'.format(i, students[i]))

    n = 0
    sLength = len(students)
    while n < sLength:
        print('n : {}'.format(n))
        print('students[{}] : {}'.format(n, students[n]))
        n += 1


    for student in students:
        print('student : {}'.format(student))


    str = 'Hello python!!'
    print('\'Hello python!!\'의 길이 : {}'.format(len(str)))


# <Q> ---------------------------------------------------------------------------------------------
# 좋아하는 운동 종복을 리스트에 저장하고 반복문을 이용해 출력

    myFavoriteSports = ['수영', '배구', '야구', '조깅']

    for i in range(len(myFavoriteSports)):
        print('myFavoriteSports[{}]: {}'.format(i, myFavoriteSports[i]))

    n = 0
    while n < len(myFavoriteSports):
        print('myFavoriteSports[{}]: {}'.format(n, myFavoriteSports[n]))
        n += 1



elif exe_no == 4:
# for문을 이용한 조회 =================================================================================

    cars = ['그랜저', '소나타', '말리부', '카니발', '쏘렌토']

    for i in range(len(cars)):
        print(cars[i])

    for car in cars:
        print(car)


    studentCnts = [[1, 19], [2, 20], [3, 22], [4, 18], [5, 21]]

    for i in range(len(studentCnts)):
        print('{}학급 학생수: {} '.format(studentCnts[i][0], studentCnts[i][1]))

    for classNo, cnt in studentCnts:
        print('{}학급 학생수: {}'.format(classNo, cnt))


# <Q> ----------------------------------------------------------------------------------------------
# 학급별 학생 수와 전체 학생 수, 평균 학생 수 출력

    studentCnts = [[1, 18], [2, 19], [3, 23], [4, 21], [5, 20], [6, 22], [7, 17]]
    sum = 0
    avg = 0
    for classNo, cnt in studentCnts:
        print('{}학급 학생수: {}명'.format(classNo, cnt))
        sum += cnt

    print('전체 학생 수: {}명'.format(sum))
    print('평균 학생 수: {}명'.format(sum / len(studentCnts)))


# <Q> ----------------------------------------------------------------------------------------------
# 과락 과목과 점수를 출력하는 프로그램

    minScore = 60

    # korScore = int(input('국어 점수: '))
    # engScore = int(input('영어 점수: '))
    # matScore = int(input('수학 점수: '))
    # sciScore = int(input('과학 점수: '))
    # hisScore = int(input('국사 점수: '))
    #
    # scores = [
    #     ['국어', korScore],
    #     ['영어', engScore],
    #     ['수학', matScore],
    #     ['과학', sciScore],
    #     ['국사', hisScore]]

    scores = [
        ['국어', 58],
        ['영어', 77],
        ['수학', 89],
        ['과학', 99],
        ['국사', 50]]

    for item in scores:
        if item[1] < minScore:
            print('과락 과목: {}, 점수: {}'.format(item[0], item[1]))

    for subject, score in scores:
        if score < minScore:
            print('과락 과목: {}, 점수: {}'.format(subject, score))

    for subject, score in scores:
        if score >= minScore: continue
        print('과락 과목: {}, 점수: {}'.format(subject, score))


# <Q> ----------------------------------------------------------------------------------------------
# 학급 학생수가 가장 작은 학급과 가장 많은 학급 출력

    studentCnts = [[1, 18], [2, 19], [3, 23], [4, 21], [5, 20], [6, 22], [7, 17]]
    minClassNo = 0; maxClassNo = 0
    minCnt = 0; maxCnt = 0
    for classNo, cnt in studentCnts:
        if minCnt == 0 or minCnt > cnt:
            minClassNo = classNo
            minCnt = cnt

        if maxCnt < cnt:
            maxClassNo = classNo
            maxCnt = cnt

    print('학생 수가 가장 적은 학급(학생수): {}학급({}명)'.format(minClassNo, minCnt))
    print('학생 수가 가장 많은 학급(학생수): {}학급({}명)'.format(maxClassNo, maxCnt))



elif exe_no == 5:
# while문을 이용한 조회 ================================================================================
# while문을 이용하면 다양한 방법으로 아이템 조회가 가능하다.

    cars = ['그랜저', '소나타', '말리부', '카니발', '쏘렌토']

    # len() 함수 사용
    n = 0
    while n < len(cars):
        print(cars[n])
        n += 1

    # flag 변수 이용
    n = 0
    flag = True
    while flag:
        print(cars[n])
        n += 1

        if n == len(cars):
            flag = False

    # break Keyword 사용
    n = 0
    while True:
        print(cars[n])
        n += 1

        if n == len(cars):
            break


    # 리스트 내 리스트가 있는 구조
    studentCnts = [[1, 19], [2, 20], [3, 22], [4, 18], [5, 21]]

    n = 0
    while n < len(studentCnts):
        print('{}학급 학생수: {} '.format(studentCnts[n][0], studentCnts[n][1]))
        n += 1

# <Q> ----------------------------------------------------------------------------------------------
# 학급별  학생 수와 전체 학생 수, 평균 학생수 출력 프로그램

    studentCnts = [[1, 18], [2, 19], [3, 23], [4, 21], [5, 20], [6, 22], [7, 17]]
    sum = 0
    avg = 0

    n = 0
    while n < len(studentCnts):
        classNo = studentCnts[n][0]
        cnt = studentCnts[n][1]
        print('{}학급 학생수: {}명'.format(classNo, cnt))

        sum += cnt
        n += 1

    print('전체 학생 수: {}명'.format(sum))
    print('평균 학생 수: {}명'.format(sum / len(studentCnts)))


# <Q> ----------------------------------------------------------------------------------------------
# 과락 과목과 점수를 출력하는 프로그램

    # korScore = int(input('국어 점수: '))
    # engScore = int(input('영어 점수: '))
    # matScore = int(input('수학 점수: '))
    # sciScore = int(input('과학 점수: '))
    # hisScore = int(input('국사 점수: '))
    #
    # scores = [
    #     ['국어', korScore],
    #     ['영어', engScore],
    #     ['수학', matScore],
    #     ['과학', sciScore],
    #     ['국사', hisScore]]

    minScore = 60
    scores = [
        ['국어', 58],
        ['영어', 77],
        ['수학', 89],
        ['과학', 99],
        ['국사', 50]]

    n = 0
    while n < len(scores):

        if scores[n][1] < minScore:
            print('과락 과목: {}, 점수: {}'.format(scores[n][0], scores[n][1]))

        n += 1

    # contine 이용
    n = 0
    while n < len(scores):

        if scores[n][1] >= minScore:
            n += 1
            continue

        print('과락 과목: {}, 점수: {}'.format(scores[n][0], scores[n][1]))
        n += 1


# <Q> ----------------------------------------------------------------------------------------------
# while문을 이용해 학급 학생수가 가장 작은 학급과 가장 많은 학급 출력

    studentCnts = [[1, 18], [2, 19], [3, 23], [4, 21], [5, 20], [6, 22], [7, 17]]
    minClassNo = 0; maxClassNo = 0
    minCnt = 0; maxCnt = 0

    n = 0
    while n < len(studentCnts):
        if minCnt == 0 or minCnt > studentCnts[n][1]:
            minClassNo = studentCnts[n][0]
            minCnt = studentCnts[n][1]

        if maxCnt < studentCnts[n][1]:
            maxClassNo = studentCnts[n][0]
            maxCnt = studentCnts[n][1]

        n += 1

    print('학생 수가 가장 적은 학급(학생수): {}학급({}명)'.format(minClassNo, minCnt))
    print('학생 수가 가장 많은 학급(학생수): {}학급({}명)'.format(maxClassNo, maxCnt))



elif exe_no == 6:
# enumerate() =======================================================================================

    sports = ['농구', '수구', '축구', '마라톤', '테니스']

    for i in range(len(sports)):
        print('{} : {}'.format(i, sports[i]))

    for idx, value in enumerate(sports):
        print('{} : {}'.format(idx, value))


    str = 'Hello python.'
    for idx, value in enumerate(str):
        print('{: >2} : {}'.format(idx, value))


# <Q> ----------------------------------------------------------------------------------------------
# 가장 좋아하는 스포츠가 몇 번째에 있는지 출력하는 프로그램

    sports = ['농구', '야구', '축구', '마라톤', '테니스']
    favoriteSport = random.choice(sports) # input('가장 좋아하는 스포츠 입력: ')

    bestSportIdx = 0
    for idx, value in enumerate(sports):
        if value == favoriteSport:
            bestSportIdx = idx + 1

    print('{}(은)는 {}번째에 있습니다.'.format(favoriteSport, bestSportIdx))


# <Q> ----------------------------------------------------------------------------------------------
# 사용자가 입력한 문자열에서 공백의 개수를 출력하는 프로그램

    # message = input('메시지 입력: ')
    message = '오늘 날씨는 아주 좋습니다. 내일도 기대됩니다.'

    cnt = 0
    for idx, value in enumerate(message):
        if value == ' ':
            cnt += 1

    print('공백 개수 : {}'.format(cnt))



elif exe_no == 7:
# 아이템 추가 =========================================================================================
# append() 메서드 --> 마지막 인덱스에 아이템 추가

    students = ['홍길동', '박찬호', '이용규', '박승철', '김지은']
    print('students : {}'.format(students))
    print('students의 길이 : {}'.format(len(students)))
    print('students의 마지막 인덱스 : {}'.format(len(students) - 1))

    students.append('강호동')
    print('students : {}'.format(students))
    print('students의 길이 : {}'.format(len(students)))
    print('students의 마지막 인덱스 : {}'.format(len(students) - 1))


    scores = [['국어', 88], ['영어', 91]]
    scores.append(['수학', 96])

    print('scores : {}'.format(scores))
    for subject, score in scores:
        print('과목: {} \t 점수: {}'.format(subject, score))


# <Q> ----------------------------------------------------------------------------------------------
# 가족 구성원에 새로 태어난 동생을 리스트에 추가

    myFamilyAge = [['아빠', 40], ['엄마', 38], ['나', 9]]
    myFamilyAge.append(['동생', 1])

    for name, age in myFamilyAge:
        print('{}의 나이: {}'.format(name, age))



elif exe_no == 8:
# 아이템 추가 =========================================================================================
# insert() 메서드 --> 특정 위치(인덱스)에 아이템 추가

    students = ['홍길동', '박찬호', '이용규', '박승철', '김지은']
    print('students : {}'.format(students))
    print('students의 길이 : {}'.format(len(students)))
    print('students의 마지막 인덱스 : {}'.format(len(students) - 1))

    students.insert(3, '강호동')
    print('students : {}'.format(students))
    print('students의 길이 : {}'.format(len(students)))
    print('students의 마지막 인덱스 : {}'.format(len(students) - 1))


    words = ['I', 'a', 'boy.']
    words.insert(1, 'am')

    for word in words:
        print('{} '.format(word), end='')
    print()


# <Q> ----------------------------------------------------------------------------------------------
# 오름차순으로 정렬되어 있는 숫자들에 사용자가 입력한 정수를 추가하는 프로그램
# (단, 추가 후에도 오름차순 정렬이 유지되어야 한다.)

    numbers = [1, 3, 6, 11, 45, 54, 62, 74, 85]
    # inputNumber = int(input('숫자 입력: '))
    inputNumber = 55
    insertIdx = 0

    for idx, number in enumerate(numbers):
        print('[{}] {}'.format(idx, number))

        if insertIdx == 0 and inputNumber < number:
            insertIdx = idx

    numbers.insert(insertIdx, inputNumber)
    print(numbers)



elif exe_no == 9:
# 아이템 삭제 =========================================================================================
# pop() 메서드 -->

    students = ['홍길동', '박찬호', '이용규', '박승철', '김지은', '강호동']
    print('students : {}'.format(students))
    print('students의 길이 : {}'.format(len(students)))

    popValue = students.pop()
    print('return value: {}'.format(popValue))
    print('students : {}'.format(students))
    print('students의 길이 : {}'.format(len(students)))


    students = ['홍길동', '박찬호', '이용규', '박승철', '김지은', '강호동']
    print('students : {}'.format(students))
    print('students의 길이 : {}'.format(len(students)))

    popValue = students.pop(3)
    print('return value: {}'.format(popValue))
    print('students : {}'.format(students))
    print('students의 길이 : {}'.format(len(students)))


# <Q> ----------------------------------------------------------------------------------------------
# 체조 선수의 점수표에서 최고 및 최저 점수를 삭제

    playerScore = [9.5, 8.9, 9.2, 9.8, 8.8, 9.0]
    print('playerScore : {}'.format(playerScore))

    minScore = 0; maxScore = 0
    minScoreIdx = 0; maxScoreIdx = 0

    for idx, score in enumerate(playerScore):
        if idx == 0 or minScore > score:
            minScoreIdx = idx
            minScore = score

    print('minScore:{}, minScoreIdx : {}'.format(minScore, minScoreIdx))

    playerScore.pop(minScoreIdx)
    print('playerScore : {}'.format(playerScore))
    '''
     # pop() 이후에 index가 자동 재배열 되므로 최대, 최소값의 index를 같이 찾는 것은 의미가 없다.
     # 새롭게 재배열된 index에서 다시 최대값 index를 찾아야 한다.
    '''
    for idx, score in enumerate(playerScore):
        if maxScore < score:
            maxScoreIdx = idx
            maxScore = score

    print('maxScore:{}, maxScoreIdx : {}'.format(maxScore, maxScoreIdx))

    playerScore.pop(maxScoreIdx)
    print('playerScore : {}'.format(playerScore))



elif exe_no == 10:
# 아이템 삭제 =========================================================================================
# remove(__value) 메서드 --> 처음 나타난 인수 __value에 해당하는 값 한 개를 삭제

    students = ['홍길동', '박찬호', '이용규', '강호동', '박승철', '김지은', '강호동']
    print('students : {}'.format(students))
    print('students의 길이 : {}'.format(len(students)))

    students.remove('강호동')
    print('students : {}'.format(students))
    print('students의 길이 : {}'.format(len(students)))


    students = ['홍길동', '박찬호', '이용규', '강호동', '박승철', '김지은', '강호동']

    print('강호동' in students)
    while '강호동' in students:
        students.remove('강호동')

    print(students)


# <Q> ----------------------------------------------------------------------------------------------
# 오늘 일정표에서 사용자가 입력한 일정을 삭제하는 프로그램

    #        < 오늘 일졍표 >
    myList = [ '마케팅 회의'
             , '회의록 정리'
             , '점심 약속'
             , '월간 업무 보고'
             , '치과 방문'
             , '마트 장보기']
    print('일정 : {}'.format(myList))

    removeItem = random.choice(myList) # input('삭제 대상 입력: ')
    print(f'removeItem: {removeItem}')
    myList.remove(removeItem)
    print('일정 : {}'.format(myList))


# <Q> ----------------------------------------------------------------------------------------------
# 시험 과목표에서 사용자가 입력한 과목을 삭제하는 프로그램

    subjects = ['국어', '영어', '수학', '과학', '국사', '영어', '수학', '과학']
    print('시험 과목표 : {}'.format(subjects))

    removeSubject = random.choice(subjects) # input('삭제 과목명 입력: ')
    print(f'removeSubject: {removeSubject}')
    while removeSubject in subjects:
        subjects.remove(removeSubject)

    print('시험 과목표 : {}'.format(subjects))



elif exe_no == 11:
# 리스트 확장 =========================================================================================
# extend() 메서드 -->

    group1 = ['홍길동', '박찬호', '이용규']
    group2 = ['강호동', '박승철', '김지은']
    print('group1: {}'.format(group1))
    print('group2: {}'.format(group2))

    group1.extend(group2)
    print('group1: {}'.format(group1))
    print('group2: {}'.format(group2))


    group1 = ['홍길동', '박찬호', '이용규']
    group2 = ['강호동', '박승철', '김지은']
    print('group1: {}'.format(group1))
    print('group2: {}'.format(group2))

    result = group1 + group2
    print('group1: {}'.format(group1))
    print('group2: {}'.format(group2))
    print('result: {}'.format(result))


# <Q> ----------------------------------------------------------------------------------------------
# 나와 내 친구가 좋아하는 번호를 합치되 번호가 중복되지 않게 하는 프로그램

    myFavoriteNumbers = [1, 3, 5, 6, 7]
    friendFavoriteNumbers = [2, 3, 5, 8, 10]

    print('myFavoriteNumbers: {}'.format(myFavoriteNumbers))
    print('friendFavoriteNumbers: {}'.format(friendFavoriteNumbers))

    addList = myFavoriteNumbers + friendFavoriteNumbers
    print('addList: {}'.format(addList))

    result = []
    for number in addList:
        if number not in result:
            result.append(number)

    print('result: {}'.format(result))



elif exe_no == 12:
# 리스트 정렬 =========================================================================================
# sort() 메서드 --> 리스트를 오름차순(default)이나 내림차순(reverse=True)으로 정렬한다.

    students = ['홍길동', '박찬호', '이용규', '강호동', '박승철', '김지은']
    print('students: {}'.format(students))

    students.sort()
    print('students: {}'.format(students))

    students.sort(reverse=True)
    print('students: {}'.format(students))


    numbers = [2, 50, 0.12, 1, 9, 7, 17, 35, 100, 3.14]
    print('numbers: {}'.format(numbers))

    numbers.sort()
    print('students: {}'.format(numbers))

    numbers.sort(reverse=True)
    print('students: {}'.format(numbers))


# <Q> ----------------------------------------------------------------------------------------------
# 아래 점수표에서 최저 및 최고 점수를 삭제한 후 총점과 평균을 출력

    playerScore = [9.5, 8.9, 9.2, 9.8, 8.8, 9.0]
    print('playerScore: {}'.format(playerScore))

    playerScore.sort()
    print('playerScore: {}'.format(playerScore))
    playerScore.pop(0)
    playerScore.pop(len(playerScore) - 1)
    print('playerScore: {}'.format(playerScore))

    sum = 0
    avg = 0
    for score in playerScore:
        sum += score

    avg = sum / len(playerScore)

    print('총점: %.2f' % sum)
    print('평점: %.2f' % avg)



elif exe_no == 13:
# 리스트 뒤집기 =======================================================================================
# reverse() 메서드 --> 리스트의 순서를 뒤집어 준다. 정렬 X

    students = ['홍길동', '박찬호', '이용규', '강호동', '박승철', '김지은']
    print('students: {}'.format(students))

    students.reverse()
    print('students: {}'.format(students))



    numbers = [2, 50, 0.12, 1, 9, 7, 17, 35, 100, 3.14]
    print('numbers: {}'.format(numbers))

    numbers.reverse()
    print('numbers: {}'.format(numbers))


# <Q> ----------------------------------------------------------------------------------------------
# 암호 해독 프로그램

    secret = '27156231'
    secretList = []
    solvedList = ''

    for cha in secret:
        secretList.append(int(cha))
    print(secretList)

    secretList.reverse()
    print(secretList)

    val = secretList[0] * secretList[1]
    secretList.insert(2, val)
    print(secretList)

    val = secretList[3] * secretList[4]
    secretList.insert(5, val)
    print(secretList)

    val = secretList[6] * secretList[7]
    secretList.insert(8, val)
    print(secretList)

    val = secretList[9] * secretList[10]
    secretList.insert(11, val)
    print(secretList)



elif exe_no == 14:
# 리스트 슬라이싱 =====================================================================================

    students = ['홍길동', '박찬호', '이용규', '강호동', '박승철', '김지은']
    print('students: {}'.format(students))
    print('students: {}'.format(students[2:4]))
    print('students: {}'.format(students[:4]))
    print('students: {}'.format(students[2:]))
    print('students: {}'.format(students[2:-2]))
    print('students: {}'.format(students[-5:-2]))
    print('students: {}'.format(students))


    numbers = [2, 50, 0.12, 1, 9, 7, 17, 35, 100, 3.14]
    print('numbers: {}'.format(numbers))
    print('numbers: {}'.format(numbers[2:4]))
    print('numbers: {}'.format(numbers[:4]))
    print('numbers: {}'.format(numbers[2:]))
    print('numbers: {}'.format(numbers[2:-2]))
    print('numbers: {}'.format(numbers[-5:-2]))


    str = 'abcdefghijklmnopqrstuvwxyz'
    print('str length: {}'.format(len(str)))
    print('str: {}'.format(str))
    print('str: {}'.format(str[2:4]))
    print('str: {}'.format(str[:4]))
    print('str: {}'.format(str[2:]))
    print('str: {}'.format(str[2:-2]))
    print('str: {}'.format(str[-5:-2]))


    numbers = [2, 50, 0.12, 1, 9, 7, 17, 35, 100, 3.14]
    print('numbers: {}'.format(numbers[2:-2]))
    print('numbers: {}'.format(numbers[2:-2:2]))
    print('numbers: {}'.format(numbers[:-2:2]))
    print('numbers: {}'.format(numbers[::2]))



    students = ['홍길동', '박찬호', '이용규', '강호동', '박승철', '김지은']
    print('students : {}'.format(students))

    students[1:4] = ['park chanho', 'lee yonggyu', 'gang hodong']
    print('students : {}'.format(students))

    students[1:4] = ['박찬호', '이용규']
    print('students : {}'.format(students))

    students[1:3] = ['park chanho', 'lee yonggyu', 'gang hodong']
    print('students : {}'.format(students))


    # slice 객체 이용
    students = ['홍길동', '박찬호', '이용규', '강호동', '박승철', '김지은']
    print('students: {}'.format(students[2:4]))
    print('students: {}'.format(students[:4]))
    print('students: {}'.format(students[2:]))
    print('students: {}'.format(students[2:-2]))
    print('students: {}'.format(students[-5:-2]))

    print('students: {}'.format(students[slice(2, 4)]))
    print('students: {}'.format(students[slice(4)]))
    print('students: {}'.format(students[slice(2, len(students))]))
    print('students: {}'.format(students[slice(2, len(students)-2)]))
    print('students: {}'.format(students[slice(len(students)-5, len(students)-2)]))

    print('students: {}'.format(students))




elif exe_no == 15:
# 리스트 그 외 기능들 ==================================================================================

    # 리스트 곱셈 연산
    students = ['홍길동', '박찬호', '이용규']
    print('students: {}'.format(students))

    studentsMul = students * 2
    print('studentsMul: {}'.format(studentsMul))

    numbers = [2, 50, 0.12, 1, 9]
    print('numbers: {}'.format(numbers))

    numbersMul = numbers * 3
    print('numbersMul: {}'.format(numbersMul))


    # index() 메서드
    students = ['홍길동', '강호동', '박찬호', '이용규', '박승철', '강호동', '김지은']
    print('students: {}'.format(students))

    searchIdx = students.index('강호동')
    print('searchIdx: {}'.format(searchIdx))

    searchIdx = students.index('강호동', 2, 6)
    print('searchIdx: {}'.format(searchIdx))

    numbers = [2, 50, 0.12, 1, 9, 7, 17, 0.12, 100, 3.14]
    print('numbers: {}'.format(numbers))

    searchIdx = numbers.index(0.12)
    print('searchIdx: {}'.format(searchIdx))

    searchIdx = numbers.index(0.12, 3)
    print('searchIdx: {}'.format(searchIdx))

    str = '홍길동강호동박찬호이용규박승철강호동김지은'
    searchIdx = str.index('강호동')
    print('searchIdx: {}'.format(searchIdx))

    searchIdx = str.index('강호동', 10, 20)
    print('searchIdx: {}'.format(searchIdx))

    # searchIdx = str.index('ㅎㅎ')
    # print('searchIdx: {}'.format(searchIdx))

# <Q> ----------------------------------------------------------------------------------------------
# 1부터 10까지의 정수가 중복되지 않고 섞여 있을 때 행운의 숫자 7의 위치 찾기

    import random

    sampleList = random.sample(range(1, 11), 10)

    selectIdx = int(input('숫자 7의 위치 입력: '))
    searchIdx = sampleList.index(7)

    if searchIdx == selectIdx:
        print('빙고!!')
    else:
        print('ㅜㅜ')

    print('sampleList: {}'.format(sampleList))
    print('searchIdx: {}'.format(searchIdx))


    # count()
    students = ['홍길동', '강호동', '박찬호', '이용규', '박승철', '강호동', '김지은']
    print('students: {}'.format(students))

    searchCnt = students.count('홍길동')
    print('searchCnt: {}'.format(searchCnt))

    searchCnt = students.count('강호동')
    print('searchCnt: {}'.format(searchCnt))

    searchCnt = students.count('김아무개')
    print('searchCnt: {}'.format(searchCnt))


    # del Keyword
    students = ['홍길동', '강호동', '박찬호', '이용규', '박승철', '강호동', '김지은']
    print('students: {}'.format(students))

    del students[1]
    print('students: {}'.format(students))

    del students[1:4]
    print('students: {}'.format(students))

    del students[2:]
    print('students: {}'.format(students))


# <Q> ----------------------------------------------------------------------------------------------
# 하루 동안 헌혈을 진행한 후 혈액형 별 개수를 파악하는 프로그램

    import random

    types = ['A', 'B', 'AB', 'O']
    todayData = []
    typeCnt = []

    for i in range(100):
        type = types[random.randrange(len(types))]
        todayData.append(type)

    print('todayData : {}'.format(todayData))
    print('todayData length : {}'.format(len(todayData)))

    for type in types:
        print('{}형 \t : {}개'.format(type, todayData.count(type)))



    while True:
        if todayData.count('O') > 0:
            todayData.remove('O')
        else:
            break;

    print('todayData : {}'.format(todayData))
    print('todayData length : {}'.format(len(todayData)))

    for type in types:
        print('{}형 \t : {}개'.format(type, todayData.count(type)))









