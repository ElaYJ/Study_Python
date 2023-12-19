'''
 # [파일 입출력]
    ▶ 텍스트 파일을 다루는 기본 함수 : open(), read(), write(), close()
'''


# 파일 열기 : open() ==========================================================================
# open할 파일의 경로를 알고 있어야 한다.
# open() 함수의 인수는 2가지 : 열 파일의 경로와 파일 사용 모드[w:쓰기, r:읽기 모드]
# 경로를 쓸때는 역슬래시(\)를 슬래시(/)로 바꿔준다.
# open() 함수에 쓴 파일 경로에 해당 파일이 없으면 새파일을 생성하고 열어준다.

# 파일 닫기 : close() ==========================================================================
#

# 파일 쓰기 : write() ==========================================================================
# write() 함수를 이용해 파일에 문자열을 쓸 수 있다.
# write() 함수가 반환하는 값은 int로 쓰려는 문자열의 길이를 반환한다.

option = int(input('option NO : '))
uri = 'D:/pythonTxt/'

if option == 1:

    #file = open('C:/pythonTxt/test.txt', 'w')
    file = open(uri + 'test.txt', 'w') # 쓰기 모드 : 기존 파일에 덮어써서 다시 쓰기

    strCnt = file.write('Hello world~')
    print(f'strCnt: {strCnt}')

    file.close()

elif option == 2:

    file = open(uri + 'test.txt', 'w')

    strCnt = file.write('Hello Python~')
    print(f'strCnt: {strCnt}')

    file.close()

elif option == 3:

    import time

    lt = time.localtime()
    dateStr = '[' + str(lt.tm_year) + '년 ' + \
              str(lt.tm_mon) + '월 ' +\
              str(lt.tm_mday) + '일] '

    todaySchedule = input('오늘 일정: ')

    file = open(uri + 'test.txt', 'w')
    file.write(dateStr + todaySchedule)
    file.close()

elif option == 4:

    import time

    lt = time.localtime()
    # dateStr = time.strftime('%Y-%m-%d %H:%M:%S %p', lt)
    dateStr = ('[' +
               time.strftime('%Y-%m-%d %I:%M:%S %p', lt) + ']\n')

    todaySchedule = '스터디 노트 쓰기 영상 강의 완료 설거지 하기' # input('오늘 일정: ')

    file = open(uri + 'test.txt', 'w')
    file.write(dateStr + todaySchedule)
    file.close()

elif option == 7:

    #uri = 'C:/pythonTxt/'

    # 'w'(write) 파일 모드 : 덮어쓰기 모드(기존 파일 내용 위에 새로 쓰여진다.)
    file = open(uri + 'hello.txt', 'w')

    strCnt = file.write('Hello world!!')
    print(f'strCnt: {strCnt}')

    file.close()

    file = open(uri + 'hello.txt', 'w')

    strCnt = file.write('Hello Python!!')
    print(f'strCnt: {strCnt}')

    file.close()

    # 'a'(append) 파일 모드 : 덧붙이기 모드(파일의 기존 내용 뒤에 덧붙여 이어 쓴다.)
    file = open(uri + 'hello.txt', 'a')

    file.write('\n')
    file.write('Hello data science!!')

    file.close()

    # 'x' 파일 모드 : 새 파일에 쓰기 모드(파일을 새로 만들고 쓴다.)
    # 파일이 이미 존재하면 Error 발생
    # file = open(uri + 'hello.txt', 'x')
    import random
    file_name = 'hello_' + str(random.randint(1, 99)) + '.txt'
    file = open(uri + file_name, 'x')

    file.write('Hello Python~\n')
    file.write('Nice to meet you!!')

    file.close()



elif option == 5:
# 파일 읽기 : read() ==========================================================================
# 읽기 모드로 파일을 열고 데이터를 문자열로 받는다.
# 'r'(read) 파일 모드 : 읽기 전용 모드

    file = open(uri + 'hello.txt', 'r')

    str = file.read()
    print(f'str: {str}')

    file.close()


    file = open(uri + 'test.txt', 'r') # 읽기모드로 파일 열기

    str_data = file.read()
    print(f'str_data:\n{str_data}')

    file.close()


elif option == 6:

    file = open(uri + 'about_python.txt', 'r')
    # UnicodeDecodeError : 'cp949' 오류는 인코딩이 맞지 않아서 나므로
    # encoding='utf8'을 써준다.

    str_data = file.read()
    print(f'str_data:\n{str_data}')

    file.close()

    # replace(_old:, _new:, _count:)
    # str = str.replace('Python', '파이썬') # 총 3개가 다 바뀐다.
    str_data = str_data.replace('Python', '파이썬', 2) # 2개만 바꾼다.
    print(f'str_data:\n{str_data}')

    file = open(uri + 'about_python.txt', 'w')
    file.write(str_data)
    file.close()


elif option == 8:
# <Q> -------------------------------------------------------------------------------------------
# 사용자가 입력한 숫자에 대한 소수를 구하고 이를 파일에 작성

    def writePrimeNumber(n):
        file = open(uri + 'prime_number.txt', 'a')
        #print(f'file_a: {file}')
        file.write(str(n))
        file.write('\t')
        file.close()

    in_num = int(input('0보다 큰 정수 입력: '))
    for num in range(2, in_num + 1):
        flag = True
        for i in range(2, num):
            if num % i == 0:
                flag = False
                break

        if (flag):
            writePrimeNumber(num)







