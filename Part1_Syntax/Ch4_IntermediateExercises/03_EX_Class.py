'''
 # [연습문제] 클래스
'''

ex_num = int (input('ex_num: '))

if ex_num == 1:
# <Q> --------------------------------------------------------------------------------------------
# 회원가입 클래스와 회원정보를 관리하는 클래스를 만들고 회원가입 로그인 기능 구현

    import class_Member as mb

    mems = mb.MemberRepository()

    for i in range(3):
        mId = input('아이디 입력: ')
        mPw = input('비밀번호 입력: ')
        mem = mb.Member(mId, mPw)
        mems.addMember(mem)

    mems.printMembers()

    mems.loginMember('abc@gmail.com', '1234')
    mems.loginMember('def@gmail.com', '5678')
    mems.loginMember('ghi@gmail.com', '9012')

    mems.removeMember('abc@gmail.com', '1234')
    mems.removeMember('def@gmail.com', '1234')
    mems.removeMember('jkl@gmail.com', '1234')

    mems.printMembers()


elif ex_num == 2:
# <Q> --------------------------------------------------------------------------------------------
# TV 클래스를 상속 구조로 만들고 객체를 생성

    import class_SmartTV as st

    print('-my4KTV' + '-'*10)
    my4KTV = st.TV4k(65, 'silver', '4K')
    my4KTV.setSmartTV('on')
    my4KTV.turnOn()
    my4KTV.printTVInfo()
    my4KTV.turnOff()

    print('-friend4KTV' + '-'*5)
    friend4KTV = st.TV4k('55', 'white')
    #friend4KTV.setSmartTV('off')
    friend4KTV.turnOn()
    friend4KTV.printTVInfo()
    friend4KTV.turnOff()

    print('-my8KTV' + '-'*10)
    my8KTV = st.TV8k(75, 'black', '8K')
    my8KTV.setSmartTV('on')
    my8KTV.setAiTV('on')
    my8KTV.turnOn()
    my8KTV.printTVInfo()
    my8KTV.turnOff()

    print('-friend8KTV' + '-'*7)
    friend8KTV = st.TV8k('86', 'red')
    friend8KTV.setSmartTV('on')
    #friend8KTV.setAiTV('off')
    friend8KTV.turnOn()
    friend8KTV.printTVInfo()
    friend8KTV.turnOff()


elif ex_num == 3:
# <Q> --------------------------------------------------------------------------------------------
# 명세서를 참고해서 도서 관리 프로그램 만들기

    import class_Book as bk

    myBReposit = bk.BookRepository()

    myBReposit.registBook(bk.Book('python', 20000, '1234567890'))
    myBReposit.registBook(bk.Book('java', 25000, '852147963'))
    myBReposit.registBook(bk.Book('c/c++', 27000, '951378624'))
    myBReposit.registBook(bk.Book('javascript', 15000, '9874563254'))

    myBReposit.printBooksInfo()
    print()
    myBReposit.printBookInfo('1234567890')
    print()
    myBReposit.removeBook('1234567890')
    myBReposit.printBooksInfo()
    print()

    # friendBReposit = bk.BookRepository()
    #
    # friendBReposit.registBook(bk.Book('python', 10000, '1234567890'))
    # friendBReposit.registBook(bk.Book('java', 15000, '852147963'))
    # friendBReposit.registBook(bk.Book('c/c++', 17000, '951378624'))
    # friendBReposit.registBook(bk.Book('javascript', 5000, '9874563254'))
    #
    # friendBReposit.printBooksInfo()
    # friendBReposit.printBookInfo('1234567890')
    # friendBReposit.removeBook('1234567890')
    # friendBReposit.printBooksInfo()


elif ex_num == 4:
# <Q> --------------------------------------------------------------------------------------------
# 추상 클래스를 이용한 한/영, 한/일 사전 클래스 만들기

    import class_ADictionary as dic

    kTe = dic.KorToEng()

    # 단어 등록
    kTe.registWord('책', 'bok')
    kTe.registWord('나비', 'butterfly')
    kTe.registWord('연필', 'pencil')
    kTe.registWord('학생', 'studen')
    kTe.registWord('선생님', 'teacher')

    # 단어 수정
    kTe.updateWord('책', 'book')
    kTe.updateWord('학생', 'student')
    print()

    # 단어 검색
    print(f'책 : {kTe.searchWord("책")}')
    print(f'나비 : {kTe.searchWord("나비")}')
    print(f'연필 : {kTe.searchWord("연필")}')
    print(f'학생 : {kTe.searchWord("학생")}')
    print(f'선생님 : {kTe.searchWord("선생님")}')
    print()

    # 단어 삭제
    kTe.removeWord('책')

    # 사전 출력
    kTe.printWords()
    print('=' * 50)

    kTj = dic.KorToJpa()

    # 단어 등록
    kTj.registWord('책', '本')
    kTj.registWord('나비', '蝶')
    kTj.registWord('연필', '鉛筆')
    kTj.registWord('학생', '学生')
    kTj.registWord('선생님', '先生')

    # 단어 수정
    kTj.updateWord('책', '蝶')
    kTj.updateWord('학생', '学生')
    print()

    # 단어 검색
    print(f'책 : {kTj.searchWord("책")}')
    print(f'나비 : {kTj.searchWord("나비")}')
    print(f'연필 : {kTj.searchWord("연필")}')
    print(f'학생 : {kTj.searchWord("학생")}')
    print(f'선생님 : {kTj.searchWord("선생님")}')
    print()

    # 단어 삭제
    kTj.removeWord('책')

    # 사전 출력
    kTj.printWords()


elif ex_num == 5:
# <Q> --------------------------------------------------------------------------------------------
# 주사위 게임 클래스를 만들고 컴퓨터와 사용자의 게임 결과를 출력하는 프로그램

    import class_Dice as dice

    dc = dice.Dice()
    dc.startGame()
    dc.printResult()


elif ex_num == 6:
# <Q> --------------------------------------------------------------------------------------------
# 자동차 경주 게임 클래스를 만들기
# 자동차는 랜덤하게 이동하며, 편의상 10초 동안 주행한다고 할 떄 가장 멀리 이동한 자동차가 우승하는 게임

    from car_game import class_car as car
    from car_game import class_car_racing as rc

    carRacing = rc.CarRacing()

    car01 = car.Car('Car01', 'white', 250)
    car02 = car.Car('Car02', 'black', 200)
    car03 = car.Car('Car03', 'yellow', 220)
    car04 = car.Car('Car04', 'red', 280)
    car05 = car.Car('Car05', 'blue', 150)

    carRacing.addCar(car01)
    carRacing.addCar(car02)
    carRacing.addCar(car03)
    carRacing.addCar(car04)
    carRacing.addCar(car05)

    carRacing.startRacing()
    carRacing.printRanking()


elif ex_num == 7:
# <Q> --------------------------------------------------------------------------------------------
# mp3 플레이어 클래스를 만들고 노래 등록 후 재생하는 프로그램

    import class_Mp3Player as mp3

    s1 = mp3.Song('신호등', '이무진', 3)
    s2 = mp3.Song('Permission to Dance', '방탄소년단', 4)
    s3 = mp3.Song('Butter', '방탄소년단', 2)
    s4 = mp3.Song('Weekend', 'TAEYEON', 5)
    s5 = mp3.Song('좋아좋아', '조정석', 4)

    player = mp3.Player()
    player.addSong(s1)
    player.addSong(s2)
    player.addSong(s3)
    player.addSong(s4)
    player.addSong(s5)

    player.setIsLoop(False)
    player.suffle()
    player.play()



