'''
 # [소수]
'''

#inputNumber = int(input("0보다 큰 정수 입력: "))

def PrimeNumber(inputNum):
    for number in range(2, (inputNum + 1)):
        flag = True
        for n in range(2, number):
            # 약수를 가지는 수는 합성수!
            if number % n == 0:
                flag = False
                break

        if (flag):
            print(' {} : 소수!!'.format(number))
        else:
            print(' {} : \t\t 합성수!!'.format(number))


print('== 소수 출력 ==')

input_data = [10, 30]
for i in input_data:
    PrimeNumber(i)
    print('-' * 25)