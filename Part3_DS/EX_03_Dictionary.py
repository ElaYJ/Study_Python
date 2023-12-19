'''
 # [연습문제]
'''

exe_no = int(input('EXE NO. '))

if exe_no == 1:
# <Q1> ---------------------------------------------------------------------------------------------
# 과목별 점수를 딕셔너리에 저장하고 출력하는 프로그램

    subject = ['국어', '영어', '수학', '과학', '국사']
    scores = {}

    for s in subject:
        score = input(s + ' 점수 입력: ')
        scores[s] = score

    print(f'과목별 점수 : {scores}')



elif exe_no == 2:
# <Q2> ---------------------------------------------------------------------------------------------
# 사용자 아이디와 비밀번호를 이용해서 로그인 프로그램 만들기

    members = {'urkpo':'0928^7$',
               'xxayv':'%2*9$91',
               'lsqvx':'!0%)&&4',
               'heums':'%@3^0%3',
               'uwcmc':'85236(&',
               'iemwv':')8!36^&',
               'sqblx':')^2)9!(',
               'jbbpy':'67269*3',
               'hjkwu':'$&@@#64',
               'fvwwy':'82$%)31'}

    memID = input('ID 입력: ')
    memPW = input('PW 입력: ')

    if memID in members:
        if members[memID] == memPW:
            print('로그인 성공!!')
        else:
            print('비밀번호 확인!!')
    else:
        print('아이디 확인!!')



elif exe_no == 3:
# <Q3> ---------------------------------------------------------------------------------------------
# 삼각형부터 십각형까지의 내각의 합과 내각을 딕셔너리에 저장하는 프로그램
# n각형의 내각의 합 = 180 × (n-2)

    dic = {}

    for n in range(3, 11):
        hap = 180 * (n - 2)
        ang = int(hap / n)
        dic[n] = [hap, ang]

    print(dic)




elif exe_no == 4:
# <Q4> ---------------------------------------------------------------------------------------------
# 1부터 10까지 각 정수에 대한 약수를 저장하는 딕셔너리를 만들고 출력하는 프로그램

    dic = {}

    for n1 in range(2, 11):
        tempList = []
        for n2 in range(1, n1+1):
            if n1 % n2 == 0:
                tempList.append(n2)
        dic[n1] = tempList

    print(dic)




elif exe_no == 5:
# <Q5> ---------------------------------------------------------------------------------------------
# 다음 문구를 공백으로 구분하여 리스트에 저장한 후, 인덱스와 단어를 이용해서 딕셔너리에 저장

    aboutPython = '파이썬은 1991년 프로그래머인 귀도 반 로섬이 발표한 고급 프로그래밍 언어이다.'

    splitList = aboutPython.split()
    print(splitList)

    dic = {}
    for idx, v in enumerate(splitList):
        dic[idx] = v

    print(dic)




elif exe_no == 6:
# <Q6> ---------------------------------------------------------------------------------------------
# 다음 문장에서 비속어를 찾고 비속어를 표준어로 변경하는 프로그램

    words = {'꺼지다':'가다',
             '쩔다':'엄청나다',
             '짭새':'경찰관',
             '꼽사리':'중간에 낀 사람',
             '먹튀':'먹고 도망',
             '지린다':'겁을 먹다',
             '쪼개다':'웃다',
             '뒷담 까다':'험담하다'}

    txt = '강도는 서로 쪼개다, 짭새를 보고 빠르게 따돌리며 먹튀했다.'

    keys = list(words.keys())

    txtMod = ''
    for key in keys:
        if key in txt:
            print('key: {}'.format(key))
            print('words[{}]: {}'.format(key, words[key]))
            txt = txt.replace(key, words[key])

    print(txt)



elif exe_no == 7:
# <Q7> ---------------------------------------------------------------------------------------------
# 딕셔너리를 이용해 5명의 회원을 가입 받고 전체 회원 정보를 출력하고
# 특정 회원 계정을 삭제하는 프로그램

    members = {}

    # 회원 등록
    n = 1
    while n < 6:
        mail = input('메일 입력: ')
        pw = input('비번 입력: ')

        if mail in members:
            print('이미 사용 중인 메일 계정입니다.')
            continue
        else:
            members[mail] = pw
            n+= 1

    for key, value in members.items():
        print(f'{key} : {value}')


    # 회원 삭제
    while True:
        delMail = input('삭제할 계정 입력: ')

        if delMail in members:
            delPw = input('비번 입력: ')
            if members[delMail] == delPw:
                del members[delMail]
                print(f'{delMail}님 삭제 완료!')
                break
            else:
                print('비번 확인 요망!')
        else:
            print('계정 확인 요망!')


    for key in members.keys():
        print(f'{key} : {members[key]}')




elif exe_no == 8:
# <Q8> ---------------------------------------------------------------------------------------------
# 다음 학생 정보 테이블로 가장 효율적으로 학생 정보를 저장하고 관리할 수 있는 자료구조 선택

    students = {'S21-0001':{'이름':'최성훈',
                            '성구분':'M',
                            '전공':'디자인',
                            '연락처':'010-1234-5678',
                            '메일':'hun@gmail.com',
                            '취미':['농구', '음악']},
                'S21-0002': {'이름': '탁영우',
                             '성구분': 'M',
                             '전공': '바리스타',
                             '연락처': '010-5678-9012',
                             '메일': 'yeong@gmail.com',
                             '취미': ['축구']},
                'S21-0003': {'이름': '황진영',
                             '성구분': 'W',
                             '전공': '음악',
                             '연락처': '010-9012-3456',
                             '메일': 'jin@gmail.com',
                             '취미': ['수영', '코딩']}
                }

    for k1 in students.keys():
        print('-' * 40)
        print(' 회원번호 : {}'.format(k1))

        student = students[k1]
        for k2 in student.keys():
            print(' {} : {}'.format(k2, student[k2]))
    print('-' * 40)

    memNo = input(' 조회할 회원번호를 입력하세요.: ')
    print(' {} : {}'.format(memNo, students.get(memNo)))




