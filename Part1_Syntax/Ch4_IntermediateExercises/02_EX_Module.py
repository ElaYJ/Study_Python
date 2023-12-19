'''
 # [연습문제] 모듈
'''

ex_num = int (input('ex_num: '))

if ex_num == 1:
# <Q> --------------------------------------------------------------------------------------------
# 과목별 점수를 입력하면 합격 여부를 출력하는 모듈
# (평균 60이상이면 합격!, 과락은 40으로 한다.)

    import module_PassOrFail as pf

    if __name__ == '__main__':
        sub1 = 100 # int(input('과목1 점수 입력: '))
        sub2 = 35 # int(input('과목2 점수 입력: '))
        sub3 = 85 # int(input('과목3 점수 입력: '))
        sub4 = 45 # int(input('과목4 점수 입력: '))
        sub5 = 90 # int(input('과목5 점수 입력: '))

        #pf.examinationResult(sub1, sub2, sub3, sub4, sub5)
        pf.examinationResult_MC(sub1, sub2, sub3, sub4, sub5)



elif ex_num == 2:
# <Q> --------------------------------------------------------------------------------------------
# 상품 구매 개수에 따라 할인율이 결정되는 모듈

    import module_Discount as dc

    if __name__ == '__main__':
        flag = True
        goods = []

        while flag:
            selectNumber = int(input('상품 구매 1.YES 2.QUIT '))

            if selectNumber == 1:
                goods_price = int(input('상품 가격 입력: '))
                goods.append(goods_price)

            elif selectNumber == 2:
                result = dc.calculatorTotalPrice(goods)
                flag = False

        print(f'할인율: {result[0]}%')
        print(f'합계: {dc.formatedNumber(result[1])}원')


elif ex_num == 3:
# <Q> --------------------------------------------------------------------------------------------
# 로또 모듈을 만들고 로또 결과를 출력하는 프로그램

    import module_Lotto as lt

    lt.startLotto()


elif ex_num == 4:
# <Q> --------------------------------------------------------------------------------------------
# 순열(Permutation) 계산 모듈을 만들고 순열 계산 결과를 출력하는 프로그램
# nPr(엔피알) : n개 중에서 r개를 뽑아 한 줄로 세울 수 있는 경우의 수

    import module_Permutation as pt

    numN = int(input('numN 입력: '))
    numR = int(input('numR 입력: '))

    # print(f'{numN}P{numR}: {pt.getPermutaionCnt(numN, numR)}')
    print(f'{numN}P{numR}: {pt.getPermutationCnt(numN, numR, logPrint=False)}')
    print('-' * 70)

    listVar = [1, 2, 3, 4, 5]
    rVar = 2
    pt.getPermutations(listVar, rVar)


elif ex_num == 5:
# <Q> --------------------------------------------------------------------------------------------
# 조합 계산 모듈을 만들고 조합 계산 결과를 출력하는 프로그램
# nCr : n개 중 순서에 상관없이 r개를 뽑아내는 경우의 수

    import module_Combination as ct

    numN = int(input('numN 입력: '))
    numR = int(input('numR 입력: '))

    print(f'{numN}C{numR}: {ct.getCombinationCnt(numN, numR)}')
    #print(f'{numN}C{numR}: {ct.getCombinationCnt(numN, numR, logPrint=False)}')
    print('-' * 50)

    listVar = [1, 2, 3, 4, 5]
    rVar = 3
    ct.getCombinations(listVar, rVar)


elif ex_num == 6:
# <Q> --------------------------------------------------------------------------------------------
# 수입과 공과금을 입력하면 공과금 총액과 수입 대비 공과금 비율을 계산하는 모듈

    import module_UtilityBill as ub

    # inputIncome = int(input('수입 입력: '))
    # ub.setIncome(inputIncome)
    #
    # inputWaterPrice = int(input('수도요금 입력: '))
    # ub.setWaterPrice(inputWaterPrice)
    #
    # inputElectricPrice = int(input('전기요금 입력: '))
    # ub.setElectricPrice(inputElectricPrice)
    #
    # inputGasPrice = int(input('가스요금 입력: '))
    # ub.setGasPrice(inputGasPrice)

    ub.setIncome(int(input('수입 입력: ')))
    ub.setWaterPrice(int(input('수도요금 입력: ')))
    ub.setElectricPrice(int(input('전기요금 입력: ')))
    ub.setGasPrice(int(input('가스요금 입력: ')))

    print(f'공과금: {ub.formatedNumber(ub.getUtilityBill())}원')
    print(f'수입 대비 공과금 비율: {ub.getUtilityBillRate()}%')


elif ex_num == 7:
# <Q> --------------------------------------------------------------------------------------------
# 위와 같이 패키자와 모듈을 만들고 연산 결과를 출력하는 프로그램

    from arithmetic import basic_operator as bo
    from arithmetic import developer_oerator as do

    from shape import triangle_square_area as tsa
    from shape import circle_area as ca

    inputNum1 = float(input('숫자1 입력: '))
    inputNum2 = float(input('숫자2 입력: '))

    print(f'{inputNum1} + {inputNum2} = {bo.add(inputNum1, inputNum2)}')
    print(f'{inputNum1} - {inputNum2} = {bo.sub(inputNum1, inputNum2)}')
    print(f'{inputNum1} * {inputNum2} = {bo.mul(inputNum1, inputNum2)}')
    print(f'{inputNum1} / {inputNum2} = {bo.div(inputNum1, inputNum2)}')

    print(f'{inputNum1} % {inputNum2} = {do.mod(inputNum1, inputNum2)}')
    print(f'{inputNum1} // {inputNum2} = {do.flo(inputNum1, inputNum2)}')
    print(f'{inputNum1} ** {inputNum2} = {do.exp(inputNum1, inputNum2)}')
    print('-' * 25)

    inputWidth = float(input('가로 길이 입력: '))
    inputHeight = float(input('세로 길이 입력: '))

    print(f'삼각형 넓이: {tsa.calTriangleArea(inputWidth, inputHeight)}')
    print(f'사각형 넓이: {tsa.calSquareArea(inputWidth, inputHeight)}')
    print('-' * 25)

    inputRadius = float(input('반지름 입력: '))
    print(f'사각형 넓이: {ca.calCircleArea(inputRadius)}')

