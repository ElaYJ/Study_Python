'''
 # [튜플]
'''

exe_no = int(input('EXE NO. '))

if exe_no == 1:
# 튜플 선언 ============================================================================================

    students = ('홍길동', '박찬호', '이용규', '박승철', '김지은')
    print('students: {}'.format(students))

    numbers = (10, 20, 30, 40, 50, 60, 70)
    print('numbers: {}'.format(numbers))

    strs = (3.14, '십', 20, 'one', '3.141592')
    print('strs: {}'.format(strs))

    datas = (10, (20, 30), [40, 50, 60])
    print('datas: {}'.format(datas))

    myFamilyNames = ('홍아빠', '홍엄마', '홍길동', '홍동생')
    print(myFamilyNames)

    todaySchedule = ('10시-업무회의',
                     '12시-친구와점심약속',
                     '3시-자료정리',
                     '6시-운동', '9시-TV시청')
    print(todaySchedule)



elif exe_no == 2:
# Item 조회 ===========================================================================================
# Index

    students = ('홍길동', '박찬호', '이용규', '박승철', '김지은')

    print('students[0]: {}'.format(students[0]))
    print('students[1]: {}'.format(students[1]))
    print('students[2]: {}'.format(students[2]))
    print('students[3]: {}'.format(students[3]))
    print('students[4]: {}'.format(students[4]))

    # print('students[5]: {}'.format(students[5]))


    numbers = (10, 20, 30, 40, 50, 60, 70)

    print('numbers[0]: {}'.format(numbers[0]))
    print('numbers[1]: {}'.format(numbers[1]))
    print('numbers[2]: {}'.format(numbers[2]))
    print('numbers[3]: {}'.format(numbers[3]))
    print('numbers[4]: {}'.format(numbers[4]))
    print('numbers[5]: {}'.format(numbers[5]))
    print('numbers[6]: {}'.format(numbers[6]))

    # print('numbers[7]: {}'.format(numbers[7]))

    strs = (3.14, '십', 20, 'one', '3.141592')

    print('strs[0]: {}'.format(strs[0]))
    print('strs[1]: {}'.format(strs[1]))
    print('strs[2]: {}'.format(strs[2]))
    print('strs[3]: {}'.format(strs[3]))
    print('strs[4]: {}'.format(strs[4]))

    # print('strs[5]: {}'.format(strs[5]))


    datas = (10, [20, 30], (40, 50, 60))

    print('datas[0]: {}'.format(datas[0]))
    print('datas[1]: {}'.format(datas[1]))
    print('datas[1][0]: {}'.format(datas[1][0]))
    print('datas[1][1]: {}'.format(datas[1][1]))
    print('datas[2]: {}'.format(datas[2]))
    print('datas[2][0]: {}'.format(datas[2][0]))
    print('datas[2][1]: {}'.format(datas[2][1]))
    print('datas[2][2]: {}'.format(datas[2][2]))


# <Q> ------------------------------------------------------------------------------------------------
# 5명의 학생 이름을 리스트에 저장하고 인덱스가 홀수인 학생과 짝수(0포함)인 학생을 구분해서 인덱스와 학생 이름을 출력

    students = ('김성예', '신경도', '박기준', '최승철', '황동석')
    print('-- 인덱스가 짝수인 학생 --')
    print('students[0] : {}'.format(students[0]))
    print('students[2] : {}'.format(students[2]))
    print('students[4] : {}'.format(students[4]))
    print('-- 인덱스가 홀수인 학생 --')
    print('students[1] : {}'.format(students[1]))
    print('students[3] : {}'.format(students[3]))


    for i in range(5):
        if i % 2 ==0:
            print('인덱스 짝수 : students[{}] : {}'.format(i, students[i]))
        else:
            print('인덱스 홀수 : students[{}] : {}'.format(i, students[i]))



elif exe_no == 3:
# Item 조회 ===========================================================================================
# in, not in Keyword

    studentsTuple = ('홍길동', '박찬호', '이용규', '박승철', '김지은')

    searchName = '홍길동' # input('학생 이름 입력: ')
    if searchName in studentsTuple:
        print('{} 학생은 우리반 학생입니다.'.format(searchName))
    else:
        print('{} 학생은 우리반 학생이 아닙니다.'.format(searchName))



    studentsList = ['홍길동', '박찬호', '이용규', '박승철', '김지은']

    searchName = '강호동' # input('학생 이름 입력: ')
    if searchName not in studentsList:
        print('{} 학생은 우리반 학생이 아닙니다.'.format(searchName))
    else:
        print('{} 학생은 우리반 학생입니다.'.format(searchName))



    pythonStr = '파이썬(영어: Python)은 1991년 프로그래머인 귀도 반 로섬이 발표한 고급 프로그래밍 언어로, ' \
                '플랫폼에 독립적이며 인터프리터식, 객체지향적, 동적 타이핑(dynamically typed) 대화형 언어이다. ' \
                '파이썬이라는 이름은 귀도가 좋아하는 코미디 〈Monty Python\'s Flying Circus〉에서 따온 것이다.'

    print('{} : {}'.format('Python', 'Python' in pythonStr))        # True
    print('{} : {}'.format('python', 'python' in pythonStr))        # False

    print('{} : {}'.format('파이썬', '파이썬' in pythonStr))          # True
    print('{} : {}'.format('파이선', '파이선' in pythonStr))          # False

    print('{} : {}'.format('귀도', '귀도' in pythonStr))              # True
    print('{} : {}'.format('객체지향적', '객체지향적' in pythonStr))    # True


# <Q> 컴퓨터가 1부터 10까지 5개의 난수를 생성한 후,
# 사용자가 입력한 숫자가 있는지 없는지를 출력하는 프로그램

    import random

    randomNumbers = random.sample(range(1, 11), 5)

    userNumber = int(input('숫자 입력(확율 50%): '))
    if userNumber in randomNumbers:
        print('빙고!')
    else:
        print('다음 기회에~')

    print('randomNumbers: {}'.format(randomNumbers))
    print('userNumber: {}'.format(userNumber))


# <Q> 문장에 비속어가 있는지 알아내는 프로그램

    wrongWord = ['쩔었다', '짭새', '꼽사리', '먹튀', '지린', '쪼개다', '뒷담 까다']
    sentence = '짭새 등장에 강도들은 모두 쩔었다. 그리고 강도 들은 지린 듯 도망갔다.'

    for word in wrongWord:
        if word in sentence:
            print('비속어: {}'.format(word))

# Item 조회 ===========================================================================================
# len()

    students = ('홍길동', '박찬호', '이용규', '박승철', '김지은')

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


    myFavoriteSports = ('수영', '배구', '야구', '조깅')

    for i in range(len(myFavoriteSports)):
        print('myFavoriteSports[{}]: {}'.format(i, myFavoriteSports[i]))

    n = 0
    while n < len(myFavoriteSports):
        print('myFavoriteSports[{}]: {}'.format(n, myFavoriteSports[n]))
        n += 1



elif exe_no == 4:
# Tuple 확장 ==========================================================================================

    studentTuple1 = ('홍길동', '박찬호', '이용규')
    studentTuple2 = ('박승철', '김지은', '강호동')

    studentTuple3 = studentTuple1 + studentTuple2
    print('studentTuple3: {}'.format(studentTuple3))

    studentTuple3 += ('ElaYJ',)
    print('studentTuple3: {}'.format(studentTuple3))


    studentList1 = ['홍길동', '박찬호', '이용규']
    studentList2 = ['박승철', '김지은', '강호동']

    studentList1.extend(studentList2)
    print('studentList1: {}'.format(studentList1))


    # studentTuple1 = ('홍길동', '박찬호', '이용규')
    # studentTuple2 = ('박승철', '김지은', '강호동')
    #
    # studentTuple1.extend(studentTuple2)
    # print('studentTuple1: {}'.format(studentTuple1))


# <Q> -----------------------------------------------------------------------
# 나와 내 친구가 좋아하는 번호를 합치되 번호가 중복되지 않게 하는 프로그램

    myFavoriteNumbers = (1, 3, 5, 6, 7)
    friendFavoriteNumbers = (2, 3, 5, 8, 10)

    print('myFavoriteNumbers: {}'.format(myFavoriteNumbers))
    print('friendFavoriteNumbers: {}'.format(friendFavoriteNumbers))

    for number in friendFavoriteNumbers:
        if number not in myFavoriteNumbers:
            # number는 int형이므로 tuple과 더하기 위해 tuple로 Castind한다.
            myFavoriteNumbers = myFavoriteNumbers + (number,)

    print('myFavoriteNumbers: {}'.format(myFavoriteNumbers))



elif exe_no == 5:
# Tuple Slicing ======================================================================================

    students = ('홍길동', '박찬호', '이용규', '강호동', '박승철', '김지은')
    print('students: {}'.format(students))
    print('students: {}'.format(students[2:4]))
    print('students: {}'.format(students[:4]))
    print('students: {}'.format(students[2:]))
    print('students: {}'.format(students[2:-2]))
    print('students: {}'.format(students[-5:-2]))



    numbers = (2, 50, 0.12, 1, 9, 7, 17, 35, 100, 3.14)
    print('numbers: {}'.format(numbers))
    print('numbers: {}'.format(numbers[2:4]))
    print('numbers: {}'.format(numbers[:4]))
    print('numbers: {}'.format(numbers[2:]))
    print('numbers: {}'.format(numbers[2:-2]))
    print('numbers: {}'.format(numbers[-5:-2]))




    numbers = (2, 50, 0.12, 1, 9, 7, 17, 35, 100, 3.14)
    print('numbers: {}'.format(numbers[2:-2]))
    print('numbers: {}'.format(numbers[2:-2:2]))
    print('numbers: {}'.format(numbers[:-2:2]))
    print('numbers: {}'.format(numbers[::2]))




    # students = ('홍길동', '박찬호', '이용규', '강호동', '박승철', '김지은')
    #
    # students[1:4] = ('park chanho', 'lee yonggyu', 'gang hodong')
    # print('students : {}'.format(students))



    students = ['홍길동', '박찬호', '이용규', '강호동', '박승철', '김지은']

    students[1:4] = ('park chanho', 'lee yonggyu', 'gang hodong')
    print('students : {}'.format(students))
    print(type(students))


    students = ('홍길동', '박찬호', '이용규', '강호동', '박승철', '김지은')
    print('students: {}'.format(students))
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




elif exe_no == 6:
# Tuple vs List ======================================================================================


    students = ['홍길동', '박찬호', '이용규', '강호동', '박승철', '김지은']
    print('students: {}'.format(students))

    # 아이템 추가
    students.append('강호동')
    print('students: {}'.format(students))

    # 아이템 변경
    students[3] = '유재석'
    print('students: {}'.format(students))

    # 아이템 삭제
    students.pop()
    print('students: {}'.format(students))


    students = ('홍길동', '박찬호', '이용규', '강호동', '박승철', '김지은')
    print('students: {}'.format(students))

    # 아이템 추가
    # students.append('강호동')
    # print('students: {}'.format(students))

    # 아이템 변경
    # students[3] = '유재석'
    # print('students: {}'.format(students))

    # 아이템 삭제
    # students.pop()
    # print('students: {}'.format(students))


    students = ['홍길동', '박찬호', '이용규', '강호동']
    print(students)
    print(type(students))

    students = ('홍길동', '박찬호', '이용규', '강호동')
    print(students)
    print(type(students))

    students = '홍길동', '박찬호', '이용규', '강호동'
    print(students)
    print(type(students))



    students = ['홍길동', '박찬호', '이용규', '강호동']
    print(students)
    print(type(students))

    students = tuple(students)
    print(students)
    print(type(students))

    students = list(students)
    print(students)
    print(type(students))


    # <Q> 튜플을 이용한 점수표에서 최저 및 최고 점수를 삭제한 후 총점과 평균을 출력

    playerScore = (9.5, 8.9, 9.2, 9.8, 8.8, 9.0)
    print('playerScore: {}'.format(playerScore))
    print(type(playerScore))

    playerScore = list(playerScore)
    print(type(playerScore))

    playerScore.sort()
    print('playerScore: {}'.format(playerScore))
    playerScore.pop(0)
    playerScore.pop(len(playerScore) - 1)

    playerScore = tuple(playerScore)
    print('playerScore: {}'.format(playerScore))
    print(type(playerScore))

    sum = 0
    avg = 0
    for score in playerScore:
        sum += score

    avg = sum / len(playerScore)

    print('총점: %.2f' % sum)
    print('평점: %.2f' % avg)




elif exe_no == 7:
# Tuple 정렬 ======================================================================================

    students = ('홍길동', '박찬호', '이용규', '강호동', '박승철', '김지은')
    print('students type: {}'.format(type(students)))
    print('students: {}'.format(students))

    students = list(students)
    students.sort()
    print('students type: {}'.format(type(students)))
    print('students: {}'.format(students))

    students = tuple(students)
    print('students type: {}'.format(type(students)))
    print('students: {}'.format(students))

    students = list(students)
    students.sort(reverse=True)
    print('students: {}'.format(students))

    students = tuple(students)
    print('students type: {}'.format(type(students)))
    print('students: {}'.format(students))



    numbers = (2, 50, 0.12, 1, 9, 7, 17, 35, 100, 3.14)
    print('numbers: {}'.format(numbers))

    numbers = list(numbers)
    numbers.sort()
    print('numbers: {}'.format(numbers))

    numbers.sort(reverse=True)
    print('numbers: {}'.format(numbers))

    numbers = tuple(numbers)
    print('numbers: {}'.format(numbers))



    students = ('홍길동', '박찬호', '이용규', '강호동', '박승철', '김지은')
    sortedStudents = sorted(students)

    print('sortedStudents type: {}'.format(type(sortedStudents)))
    print('sortedStudents: {}'.format(sortedStudents))

    print('students type: {}'.format(type(students)))
    print('students: {}'.format(students))

    sortedStudents = sorted(students, reverse=True)
    print('sortedStudents type: {}'.format(type(sortedStudents)))
    print('sortedStudents: {}'.format(sortedStudents))


    # <Q> 튜플을 이용한 점수표에서 최저 및 최고 점수를 삭제한 후 총점과 평균을 출력
    playerScore = (9.5, 8.9, 9.2, 9.8, 8.8, 9.0)
    print('playerScore: {}'.format(playerScore))

    playerScore = list(playerScore)
    playerScore.sort()
    print('playerScore: {}'.format(playerScore))

    playerScore.pop(0)
    playerScore.pop(len(playerScore) - 1)

    playerScore = tuple(playerScore)
    print('playerScore: {}'.format(playerScore))


    sum = 0
    avg = 0
    for score in playerScore:
        sum += score

    avg = sum / len(playerScore)

    print('총점: %.2f' % sum)
    print('평점: %.2f' % avg)




elif exe_no == 8:
# for문 조회 ======================================================================================

    cars = '그랜저', '소나타', '말리부', '카니발', '쏘렌토'

    for i in range(len(cars)):
        print(cars[i])

    for car in cars:
        print(car)


    studentCnts = (1, 19), (2, 20), (3, 22), (4, 18), (5, 21)

    for i in range(len(studentCnts)):
        print('{}학급 학생수: {} '.format(studentCnts[i][0], studentCnts[i][1]))

    for classNo, cnt in studentCnts:
        print('{}학급 학생수: {}'.format(classNo, cnt))



    # 학급 학생수
    studentCnts = (1, 18), (2, 19), (3, 23), (4, 21), (5, 20), (6, 22), (7, 17)
    sum = 0
    avg = 0
    for classNo, cnt in studentCnts:
        print('{}학급 학생수: {}명'.format(classNo, cnt))
        sum += cnt

    print('전체 학생 수: {}명'.format(sum))
    print('평균 학생 수: {}명'.format(sum / len(studentCnts)))



    minScore = 60
    scores = (
        ('국어', 58),
        ('영어', 77),
        ('수학', 89),
        ('과학', 99),
        ('국사', 50))

    for item in scores:
        if item[1] < minScore:
            print('과락 과목: {}, 점수: {}'.format(item[0], item[1]))

    for subject, score in scores:
        if score < minScore:
            print('과락 과목: {}, 점수: {}'.format(subject, score))

    for subject, score in scores:
        if score >= minScore: continue
        print('과락 과목: {}, 점수: {}'.format(subject, score))

    # 과락 과목 출력
    # minScore = 60
    #
    # korScore = int(input('국어 점수: '))
    # engScore = int(input('영어 점수: '))
    # matScore = int(input('수학 점수: '))
    # sciScore = int(input('과학 점수: '))
    # hisScore = int(input('국사 점수: '))
    #
    # scores = (
    #     ('국어', korScore),
    #     ('영어', engScore),
    #     ('수학', matScore),
    #     ('과학', sciScore),
    #     ('국사', hisScore))
    #
    # for subject, score in scores:
    #     if score < minScore:
    #         print('과락 과목: {}, 점수: {}'.format(subject, score))


    # 학급 학생수가 가장 작은 학급과 가장 많은 학급 출력
    studentCnts = (1, 18), (2, 19), (3, 23), (4, 21), (5, 20), (6, 22), (7, 17)
    minclassNo = 0; maxclassNo = 0
    minCnt = 0; maxCnt = 0
    for classNo, cnt in studentCnts:
        if minCnt == 0 or minCnt > cnt:
            minclassNo = classNo
            minCnt = cnt

        if maxCnt < cnt:
            maxclassNo = classNo
            maxCnt = cnt

    print('학생 수가 가장 적은 학급(학생수): {}학급({}명)'.format(minclassNo, minCnt))
    print('학생 수가 가장 많은 학급(학생수): {}학급({}명)'.format(maxclassNo, maxCnt))




elif exe_no == 9:
# while문 조회 ======================================================================================

    cars = ('그랜저', '소나타', '말리부', '카니발', '쏘렌토')

    n = 0
    while n < len(cars):
        print(cars[n])
        n += 1


    n = 0
    flag = True
    while flag:
        print(cars[n])
        n += 1

        if n == len(cars):
            flag = False


    n = 0
    while True:
        print(cars[n])
        n += 1

        if n == len(cars):
            break


    studentCnts = (1, 19), (2, 20), (3, 22), (4, 18), (5, 21)

    n = 0
    while n < len(studentCnts):
        print('{}학급 학생수: {} '.format(studentCnts[n][0], studentCnts[n][1]))
        n += 1


    # 학급 학생수
    studentCnts = (1, 18), (2, 19), (3, 23), (4, 21), (5, 20), (6, 22), (7, 17)
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



    minScore = 60
    scores = (
        ('국어', 58),
        ('영어', 77),
        ('수학', 89),
        ('과학', 99),
        ('국사', 50))

    n = 0
    while n < len(scores):
        if scores[n][1] < minScore:
            print('과락 과목: {}, 점수: {}'.format(scores[n][0], scores[n][1]))
        n += 1

    # continue 이용
    n = 0
    while n < len(scores):
        if scores[n][1] >= minScore:
            n += 1
            continue
        print('과락 과목: {}, 점수: {}'.format(scores[n][0], scores[n][1]))
        n += 1


    # 과락 과목 출력
    # minScore = 60
    #
    # korScore = int(input('국어 점수: '))
    # engScore = int(input('영어 점수: '))
    # matScore = int(input('수학 점수: '))
    # sciScore = int(input('과학 점수: '))
    # hisScore = int(input('국사 점수: '))
    #
    # scores = (
    #     ('국어', korScore),
    #     ('영어', engScore),
    #     ('수학', matScore),
    #     ('과학', sciScore),
    #     ('국사', hisScore))
    #
    # n = 0
    # while n < len(scores):
    #     if scores[n][1] < minScore:
    #         print('과락 과목: {}, 점수: {}'.format(scores[n][0], scores[n][1]))
    #
    #     n += 1



    # 학급 학생수가 가장 작은 학급과 가장 많은 학급 출력
    studentCnts = (1, 18), (2, 19), (3, 23), (4, 21), (5, 20), (6, 22), (7, 17)
    minclassNo = 0; maxclassNo = 0
    minCnt = 0; maxCnt = 0

    n = 0
    while n < len(studentCnts):
        if minCnt == 0 or minCnt > studentCnts[n][1]:
            minclassNo = studentCnts[n][0]
            minCnt = studentCnts[n][1]

        if maxCnt < studentCnts[n][1]:
            maxclassNo = studentCnts[n][0]
            maxCnt = studentCnts[n][1]

        n += 1

    print('학생 수가 가장 적은 학급(학생수): {}학급({}명)'.format(minclassNo, minCnt))
    print('학생 수가 가장 많은 학급(학생수): {}학급({}명)'.format(maxclassNo, maxCnt))
