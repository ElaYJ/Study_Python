'''
 # [딕셔너리]
'''

exe_no = int(input('EXE NO. '))

if exe_no == 1:
# Dic 선언 ==========================================================================================

    students = {'s1':'홍길동', 's2':'박찬호', 's3':'이용규', 's4':'박승철', 's5':'김지은'}
    print('students: {}'.format(students))
    print('students type: {}'.format(type(students)))

    # 다양한 자료형 사용 가능
    memInfo = {'이름':'홍길동', '메일':'gildong@gmail.com', '학년':3, '취미':['농구', '게임']}
    print('memInfo: {}'.format(memInfo))
    print('memInfo type: {}'.format(type(memInfo)))

    # Value값으로 Dic 자료형 사용
    student1 = {'이름':'홍길동', '메일':'gildong@gmail.com', '학년':3}
    student2 = {'이름':'박찬호', '메일':'chanho@gmail.com', '학년':2}
    student3 = {'이름':'이용규', '메일':'yonggyu@gmail.com', '학년':1}

    studentInfo = {1:student1, 2:student2, 3:student3}
    print('studentInfo: {}'.format(studentInfo))
    print('studentInfo type: {}'.format(type(studentInfo)))

    # Key로 mutable값 사용 불가!!
    # studentInfo = {(1, 2):3, [1, 2]:3}
    # Key <- immutable값
    studentInfo = {(1, 2):3, (1, 2):3, (2, 3):4}
    print(studentInfo)

    # <Q> 나의 정보 Dictionary에 저장하고 출력
    myInfo = {'이름':'박경진',
              '전공':'computer',
              '메일':'jin@naver.com',
              '학년':3,
              '주소':'대한민국 서울',
              '취미':['요리', '여행']}
    print('myInfo: {}'.format(myInfo))



elif exe_no == 2:
# Dic 조회 ==========================================================================================

    students = {'s1':'홍길동', 's2':'박찬호', 's3':'이용규', 's4':'박승철', 's5':'김지은'}

    print('students[\'s1\']:{}'.format(students['s1']))
    print('students[\'s2\']:{}'.format(students['s2']))
    print('students[\'s3\']:{}'.format(students['s3']))
    print('students[\'s4\']:{}'.format(students['s4']))
    print('students[\'s5\']:{}'.format(students['s5']))
    # 존재하지 않는 키를 사용한 조회 시 Error 발생
    # print('students[\'s6\']:{}'.format(students['s6']))


    memInfo = {'이름':'홍길동', '취미':['농구', '게임', '여행']}
    print('memInfo[\'이름\']:{}'.format(memInfo['이름']))
    print('memInfo[\'취미\']:{}'.format(memInfo['취미']))
    print('memInfo[\'취미[0]\']:{}'.format(memInfo['취미'][0]))
    print('memInfo[\'취미[1]\']:{}'.format(memInfo['취미'][1]))
    print('memInfo[\'취미[2]\']:{}'.format(memInfo['취미'][2]))

    for h in memInfo['취미']:
        print(h)

    for i, h in enumerate(memInfo['취미']):
        print('index:{} --> {}'.format(i, h))



    # students = {'s1':'홍길동', 's2':'박찬호', 's3':'이용규', 's4':'박승철', 's5':'김지은'}
    # print('students[\'s6\']:{}'.format(students['s6']))



    students = {'s1':'홍길동', 's2':'박찬호', 's3':'이용규', 's4':'박승철', 's5':'김지은'}
    print('students.get(\'s5\'):{}'.format(students.get('s5')))
    print('students.get(\'s6\'):{}'.format(students.get('s6')))


    # <Q> 나의 정보를 Dictionary에 저장하고 ‘[ ]’와 'get()' 함수로 조회하고 출력
    myInfo = {'이름':'박경진',
              '전공':'computer',
              '메일':'jin@naver.com',
              '학년':3,
              '주소':'대한민국 서울',
              '취미':['요리', '여행']}

    print('myInfo[\'이름\']: {}'.format(myInfo['이름']))
    print('myInfo[\'전공\']: {}'.format(myInfo['전공']))
    print('myInfo[\'메일\']: {}'.format(myInfo['메일']))
    print('myInfo[\'학년\']: {}'.format(myInfo['학년']))
    print('myInfo[\'주소\']: {}'.format(myInfo['주소']))
    print('myInfo[\'취미\']: {}'.format(myInfo['취미']))

    print('myInfo.get(\'이름\'): {}'.format(myInfo.get('이름')))
    print('myInfo.get(\'전공\'): {}'.format(myInfo.get('전공')))
    print('myInfo.get(\'메일\'): {}'.format(myInfo.get('메일')))
    print('myInfo.get(\'학년\'): {}'.format(myInfo.get('학년')))
    print('myInfo.get(\'주소\'): {}'.format(myInfo.get('주소')))
    print('myInfo.get(\'취미\'): {}'.format(myInfo.get('취미')))

    print(f'myInfo.get(\'취미\'): {myInfo.get("취미")}')




elif exe_no == 3:
# Dic 추가 ==========================================================================================

    myInfo = {}

    myInfo['이름'] = '박경진'
    myInfo['전공'] = 'computer'
    myInfo['메일'] = 'jin@naver.com'
    myInfo['학년'] = 3
    myInfo['주소'] = '대한민국 서울'
    myInfo['취미'] = ['요리', '여행']

    print(f'myInfo : {myInfo}')


    myInfo['메일'] = 'gyeongjin@naver.com'
    print(f'myInfo : {myInfo}')


    # <Q> 학생 정보를 입력받아 딕셔너리에 추가
    studentInfo = {}

    studentInfo['name'] = input('이름 입력: ')
    studentInfo['grade'] = input('학년 입력: ')
    studentInfo['mail'] = input('메일 입력: ')
    studentInfo['addr'] = input('주소 입력: ')

    print(f'studentInfo : {studentInfo}')


    # <Q> 0부터 10까지의 각 정수에 대한 팩토리얼을 딕셔너리에 추가
    factorialDic = {}
    for i in range(11):
        if i == 0:
            factorialDic[i] = 1
        else:
            factorialDic[i] =  factorialDic[i-1] * i
            # for j in range(1, (i+1)):
            #     factorialDic[i] = factorialDic[i-1] * j

    print(f'factorialDic : {factorialDic}')



elif exe_no == 4:
# Dic 수정 ==========================================================================================

    myInfo = {}

    myInfo['이름'] = '박경진'
    myInfo['전공'] = 'computer'
    myInfo['메일'] = 'jin@naver.com'
    myInfo['학년'] = 3
    myInfo['주소'] = '대한민국 서울'
    myInfo['취미'] = ['요리', '여행']

    print(f'myInfo : {myInfo}')

    myInfo['전공'] = 'sports'
    myInfo['학년'] = '4'
    print(f'myInfo : {myInfo}')

    # <Q> 학생의 시험 점수가 60점 미만이면 ‘F(재시험)’으로 값 변경
    scores = {'kor':88, 'eng':55, 'mat':85, 'sci':57, 'his':82}
    print(f'scores : {scores}')

    minScore = 60
    fStr = 'F(재시험)'
    if scores['kor'] < minScore: scores['kor'] = fStr
    if scores['eng'] < minScore: scores['eng'] = fStr
    if scores['mat'] < minScore: scores['mat'] = fStr
    if scores['sci'] < minScore: scores['sci'] = fStr
    if scores['his'] < minScore: scores['his'] = fStr
    print(f'scores : {scores}')

    # <Q> 30일 후 몸무계와 신장의 값을 저장하고 BMI 값을 출력하는 프로그램
    # 키 / (신장 * 신장)
    myBodyInfo = {'이름':'gildong', '몸무게':83.0, '신장':1.8}
    myBMI = myBodyInfo['몸무게'] / (myBodyInfo['신장'] ** 2)
    print(f'myBodyInfo: {myBodyInfo}')
    print(f'myBMI: {round(myBMI, 2)}')

    date = 0
    while True:
        date += 1
        myBodyInfo['몸무게'] = round((myBodyInfo['몸무게'] - 0.3), 2)
        print('몸무게:\t', myBodyInfo['몸무게'])
        myBodyInfo['신장'] = round((myBodyInfo['신장'] + 0.001), 3)
        print('신장:\t\t\t', myBodyInfo['신장'])
        myBMI = myBodyInfo['몸무게'] / (myBodyInfo['신장'] ** 2)

        if date >= 30:
            break

    print(f'myBodyInfo: {myBodyInfo}')
    print(f'myBMI: {round(myBMI, 2)}')



elif exe_no == 5:
# Dic 조회 ==========================================================================================
# keys(), values(), items()

    memInfo = {'이름':'홍길동', '메일':'gildong@gmail.com', '학년':3, '취미':['농구', '게임']}

    ks = memInfo.keys()
    print(f'keys : {ks}')
    print(f'keys type : {type(ks)}')

    vs = memInfo.values()
    print(f'values : {vs}')
    print(f'values type : {type(vs)}')

    items = memInfo.items()
    print(f'items : {items}')
    print(f'items type : {type(items)}')


    ks = list(ks)
    print(f'keys : {ks}')
    print(f'keys type : {type(ks)}')

    print(f'keys[0] : {ks[0]}')
    print(f'keys[1] : {ks[1]}')
    print(f'keys[2] : {ks[2]}')
    print(f'keys[3] : {ks[3]}')


    vs = list(vs)
    print(f'values : {vs}')
    print(f'values type : {type(vs)}')

    print(f'values[0] : {vs[0]}')
    print(f'values[1] : {vs[1]}')
    print(f'values[2] : {vs[2]}')
    print(f'values[3] : {vs[3]}')


    items = list(items)
    print(f'items : {items}')
    print(f'items type : {type(items)}')

    print(f'items[0] : {items[0]}')
    print(f'items[1] : {items[1]}')
    print(f'items[2] : {items[2]}')
    print(f'items[3] : {items[3]}')


    for key in ks:
        print(f'key: {key}')

    for idx, key in enumerate(ks):
        print(f'idx, key: {idx}, {key}')

    for value in vs:
        print(f'value: {value}')

    for idx, value in enumerate(vs):
        print(f'idx, value: {idx}, {value}')

    for item in items:
        print(f'item: {item}')

    for idx, item in enumerate(items):
        print(f'idx, item: {idx}, {item}')

    for key in memInfo.keys():
        print(f'{key}: {memInfo[key]}')


    # <Q> 학생의 시험 점수가 60점 미만이면 ‘F(재시험)’으로 값을 변경하는 코드
    scores = {'kor':88, 'eng':55, 'mat':85, 'sci':57, 'his':82}
    print(f'scores: {scores}')

    minScore = 60
    fStr = 'F(재시험)'
    fDic = {}

    # for key in scores:
    #     if scores[key] < minScore:
    #         scores[key] = fStr
    #         fDic[key] = fStr

    for key, value in scores.items():
        print(key, value)
        if value < minScore:
            scores[key] = fStr
            fDic[key] = fStr

    print(f'scores: {scores}')
    print(f'fDic: {fDic}')



elif exe_no == 6:
# Dic 삭제 ==========================================================================================

    # del
    memInfo = {'이름':'홍길동', '메일':'gildong@gmail.com', '학년':3, '취미':['농구', '게임']}
    print(f'memInfo: {memInfo}')

    del memInfo['메일']
    print(f'memInfo: {memInfo}')

    del memInfo['취미']
    print(f'memInfo: {memInfo}')


    # pop()
    memInfo = {'이름':'홍길동', '메일':'gildong@gmail.com', '학년':3, '취미':['농구', '게임']}
    print(f'memInfo: {memInfo}')

    returnValue = memInfo.pop('이름')
    print(f'memInfo: {memInfo}')
    print(f'returnValue: {returnValue}')
    print(f'returnValue type: {type(returnValue)}')

    returnValue = memInfo.pop('취미')
    print(f'memInfo: {memInfo}')
    print(f'returnValue: {returnValue}')
    print(f'returnValue type: {type(returnValue)}')



    # <Q> Dic에 저장된 점수 중 최저 및 최고 점수를 삭제하는 프로그램
    scores = {'score1':8.9, 'score2':8.1, 'score3':8.5, 'score4':9.8, 'score5':8.8}
    minScore = 10; minScoreKey = ''
    maxScore = 0; maxScoreKey = ''

    for key in scores.keys():
        if scores[key] < minScore:
            minScore = scores[key]
            minScoreKey = key

        if scores[key] > maxScore:
            maxScore = scores[key]
            maxScoreKey = key

    print('minScore : {}'.format(minScore))
    print('minScoreKey : {}'.format(minScoreKey))

    print('maxScore : {}'.format(maxScore))
    print('maxScoreKey : {}'.format(maxScoreKey))

    del scores[minScoreKey]
    del scores[maxScoreKey]

    print('scores : {}'.format(scores))




elif exe_no == 7:
# Dic 그외 ==========================================================================================


    memInfo = {'이름':'홍길동', '메일':'gildong@gmail.com', '학년':3, '취미':['농구', '게임']}

    print('이름' in memInfo)
    print('메일' in memInfo)
    print('학년' in memInfo)
    print('취미' in memInfo)

    print('name' not in memInfo)
    print('mail' not in memInfo)
    print('grade' not in memInfo)
    print('hobby' not in memInfo)

    print('홍길동' in memInfo)
    print('gildong@gmail.com' in memInfo)
    print(3 in memInfo)
    # print(['농구', '게임'] in memInfo)


    print('len(memInfo) : {}'.format(len(memInfo)))

    print('memInfo: {}'.format(memInfo))

    memInfo.clear()
    print('memInfo: {}'.format(memInfo))



    # <Q> 개인 정보에 ‘연락처’와 ‘주민등록번호’가 있다면 삭제하는 코드
    myInfo = {'이름':'Hong Gildong',
              '나이':'30',
              '연락처': '010-1234-5678',
              '주민등록번호':'840315-1234567',
              '주소':'대한민국 서울'}
    print('myInfo: {}'.format(myInfo))

    deleteItems = ['연락처', '주민등록번호']

    for item in deleteItems:
        if (item in myInfo):
            del myInfo[item]

    print('myInfo: {}'.format(myInfo))



