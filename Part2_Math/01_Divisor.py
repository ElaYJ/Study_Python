'''
 # [약수] 어떤 수를 나누어 떨어지게 하는 수!
'''

#inputNumber = int(input("0보다 큰 정수 입력: "))

def Divisor(inputNum):
    divisors = []
    for number in range(1, (inputNum + 1)):
        # 나머지가 0인 숫자 찾기
        if inputNum % number == 0:
            divisors.append(number)

    return divisors


print('== 약수 출력 ==')
print('-' * 50)

input = [30, 7, 100]
for i in input:
    print(' {: >3}의 약수: {}'.format(i, Divisor(i)))
    print('-' * 50)