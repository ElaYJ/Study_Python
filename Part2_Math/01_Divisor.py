'''
 # [약수]
'''

#inputNumber = int(input("0보다 큰 정수 입력: "))

def Divisor(inputNum):
    for number in range(1, (inputNum + 1)):
        # 나머지가 0인 숫자 찾기
        if inputNum % number == 0:
            print(' {}의 약수: {}'.format(inputNum, number))


print('== 약수 출력 ==')

input = [30, 7, 100]
for i in input:
    Divisor(i)
    print('-' * 20)