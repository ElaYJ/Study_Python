'''
 # [with ~ as] 구문을 사용하면 close()가 자동으로 사용된다.
    ▶ 내가 따로 close()하지 않아도 된다.
'''


exeOption = int(input('Execute Option: '))
uri = 'D:/pythonTxt/'

if exeOption == 1:

    file = open(uri + '5_037.txt', 'a')
    file.write('python study!!')
    file.close()

    file = open(uri + '5_037.txt', 'r')
    print(file.read())
    file.close()

elif exeOption == 2:

    with open(uri + '5_037.txt', 'a') as f:
        f.write('python study!!')

    with open(uri + '5_037.txt', 'r') as f:
        print(f.read())


elif exeOption == 3:
# <Q> -------------------------------------------------------------------------------------
# 로또 번호 생성기 프로그램을 만들고 파일에 번호 출력

    import random

    def writeNumbers(nums):
        for idx, num in enumerate(nums):
            with open(uri + 'lotto.txt', 'a') as f:
                if idx < (len(nums) - 2):
                    f.write(str(num) + ', ')
                elif idx == (len(nums) - 2):
                    f.write(str(num))
                elif idx == (len(nums) - 1):
                    f.write('\n')
                    f.write('bonus: ' + str(num))
                    f.write('\n')


    rNums = random.sample(range(1, 46), 7)
    print(f'rNums: {rNums}')

    writeNumbers(rNums)

elif exeOption == 4:
# writelines() ==============================================================================
# writelines()는 list나 tuple 데이터를 파일에 쓰기 위한 함수이다.

    languages = ['c/c++', 'java', 'c#', 'python', 'javascript']

    #uri = 'C:/pythonTxt/'
    for item in languages:
        with open(uri + 'languages.txt', 'a') as f:
            f.write(item)
            f.write('\n')
    # 반복 가능한 객체가 어차피 for문을 이용해야 한다면
    # 파이썬은 내부적으로 이런 기능을 가진 함수를 하나 제공해준다. -> writelines()

elif exeOption == 5:

    languages = ('c/c++', 'java', 'c#', 'python', 'javascript')
    print(type(languages))

    #uri = 'C:/pythonTxt/'
    with open(uri + 'languages.txt', 'w') as f:
        f.writelines(languages)
        f.writelines(item + '\n' for item in languages)

    with open(uri + 'languages.txt', 'r') as f:
        print(f.read())

elif exeOption == 6:
# <Q> ----------------------------------------------------------------------------------------
# 딕셔너리에 저장된 과목별 점수를 파일에 저장하는 코드 작성

    scoreDic = {'kor': 85, 'eng': 90, 'mat': 92, 'sci': 79, 'his': 82}

    for key in scoreDic.keys():
        with open(uri + 'scoreDic.txt', 'a') as f:
            f.write(key + '\t: ' + str(scoreDic[key]) + '\n')


    with open(uri + 'scoreDic.txt', 'a') as f:
        f.writelines(key +'\t: '+str(scoreDic[key])+'\n' for key in scoreDic.keys())

    with open(uri + 'scoreDic.txt', 'a') as f:
        for key in scoreDic.keys():
            f.write(key + '\t: ' + str(scoreDic[key]) + '\n')

# 딕셔너리나 리스트 형태의 정렬 방식을 그대로 출력하겠다면...

    #uri = 'C:/pythonTxt/'
    dic = {'s1': 90, 's2': 85, 's3': 95}

    with open(uri + 'scores.txt', 'a') as f:
        print(dic, file=f)

    list = [90, 85, 95]

    with open(uri + 'scores.txt', 'a') as f:
        print(list, file=f)


elif exeOption == 8:
# readlines() : 여러줄 읽기 ========================================================================
# 파일의 모든 데이터를 읽어서 리스트 형태로 반환
# 개행을 list item 구분자로 사용한다. -> 개행이 되어 있다면 개행 문자까지 그대로 가져온다.

    with open(uri + 'lans.txt', 'r') as f:
        lanList = f.readlines()

    print(f'lanList: {lanList}')
    print(f'lanList type: {type(lanList)}')


# readline() : 한줄 읽기 ===========================================================================
# 한 행을 읽어서 문자열로 반환

    with open(uri + 'lans.txt', 'r') as f:
        line = f.readline() # 한줄 읽음(눈에 보이지는 않지만 개행 문자도 같이 읽음)

        while line != '':
            print(f'line: {line}', end='') # print()도 자동 개행되므로 이중 개행이 이루어진다.
            line = f.readline()


elif exeOption == 9:
# <Q> -------------------------------------------------------------------------------------------
# 파일에 저장된 과목별 점수를 파이썬에서 읽어, 딕셔너리에 저장하는 코드
# 과목 문자열과 점수 정수형을 구분해야 하고, 개행 문자도 날려주어야 한다.
#  scores_data.txt
#   kor:85
#   eng:90
#   mat:92
#   sic:79
#   his:82

    scoreDic = {}

    with open(uri + 'scores_data.txt', 'r') as f:
        line = f.readline()

        while line != '':
            print(f'line: {line}', end='')

            tempList = line.split(':') # 구분자를 기준으로 문자열을 나누어 리스트 형태로 반환
            print(f'temp{type(tempList)}: {tempList}')

            scoreDic[tempList[0]] = int(tempList[1].strip('\n'))
            # strip()으로 개행 문자를 잘라내고 문자열인 점수를 숫자로 Casting
            # strip('\n') 함수는 인수로 주어진 개행 문자를 잘라낸다.

            line = f.readline()

    print(f'scoreDic: {scoreDic}')
