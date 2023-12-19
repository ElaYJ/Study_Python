def exampleResult(s1, s2, s3, s4, s5):

    passAvgScore = 60
    limitScore = 40

    def getTotal():
        totalScore = s1 + s2 + s3 + s4 + s5
        print(f'총점: {totalScore}')
        return totalScore

    def getAverage():
        avg = getTotal() / 5
        print(f'평균: {avg}')
        return avg

    def printPassOrFail():
        print(f'{s1}: Pass') if s1 >= limitScore else print(f'{s1}: Fail')
        print(f'{s2}: Pass') if s2 >= limitScore else print(f'{s2}: Fail')
        print(f'{s3}: Pass') if s3 >= limitScore else print(f'{s3}: Fail')
        print(f'{s4}: Pass') if s4 >= limitScore else print(f'{s4}: Fail')
        print(f'{s5}: Pass') if s5 >= limitScore else print(f'{s5}: Fail')

    def printFinalPassOrFail():

        if getAverage() >= passAvgScore:
            if s1 >= limitScore and s2 >= limitScore and s3 >= limitScore and s4 >= limitScore and s5 >= limitScore:
                print('Final Pass!!')

            else:
                print('Final Fail!!')

        else:
            print('Final Fail!!')


    getAverage()
    printPassOrFail()
    printFinalPassOrFail()



if __name__ == '__main__':
    sub1 = int(input('과목1 점수 입력: '))
    sub2 = int(input('과목2 점수 입력: '))
    sub3 = int(input('과목3 점수 입력: '))
    sub4 = int(input('과목4 점수 입력: '))
    sub5 = int(input('과목5 점수 입력: '))

    exampleResult(sub1, sub2, sub3, sub4, sub5)







def examinationResult(*s): # 과목별 점수를 받아옴
    print(type(s))

    passAvgScore = 60; subLimitScore = 40

    def getTotal():
        totalScore = sum(s)
        print(f'총점: {totalScore}')
        return totalScore

    def getAverage():
        avg = getTotal() / len(s)
        print(f'평균: {avg}')
        return avg

    def printSubjetPassOrFail():
        for idx, score in enumerate(s):
            print(f'과목{idx+1}: Pass') if score >= subLimitScore else print(f'과목{idx+1}: Fail')

    def printFinalPassOrFail():

        result = 'Final Pass!!'

        if getAverage() >= passAvgScore: # 평균은 PASS인데,
            for score in s:
                if score < subLimitScore: # 과목별 과락이 있는지 확인
                    result = 'Final Fail!!'
                    break
        else:
            result = 'Final Fail!!'

        print(result)

    #getAverage()
    printSubjetPassOrFail()
    printFinalPassOrFail()


def examinationResult_MC(*s): # 과목별 점수를 받아옴
    print(type(s))

    passAvgScore = 60; subLimitScore = 40

    def getTotal():
        totalScore = sum(s)
        print(f'총점: {totalScore}')
        return totalScore

    def getAverage():
        avg = getTotal() / len(s)
        print(f'평균: {avg}')
        return avg

    def printSubjetPassOrFail():
        sub_pass_flag = True

        for idx, score in enumerate(s):
            if score >= subLimitScore:
                print(f'과목{idx + 1}: Pass')
            else:
                print(f'과목{idx + 1}: Fail')
                sub_pass_flag = False

        return sub_pass_flag


    def printFinalPassOrFail():

        result = ''

        # 왜 얘는 getAverage() 결과가 출력 안되지?????
        # if printSubjetPassOrFail() and getAverage() >= passAvgScore:
        #     result = 'Final Pass!!'

        if (getAverage() >= passAvgScore) and printSubjetPassOrFail():
            result = 'Final Pass!!'
        else:
            result = 'Final Fail!!'

        print(result)

    #getAverage()
    printFinalPassOrFail()
