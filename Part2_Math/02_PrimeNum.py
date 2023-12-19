'''
 # [소수] 1과 그 수 자신만을 약수로 가지는 수!  단, 1은 소수에 포함되지 않는다.
'''

#inputNumber = int(input("0보다 큰 정수 입력: "))

def Prime(inputNum):
    cnt = 0
    for number in range(2, (inputNum + 1)):
        cnt += 1
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
    print(f'count: {cnt}')


input_data = [10, 30]
for i in input_data:
    print(f'<2 ~ {i}까지 소수는? >')
    Prime(i)
    print('-' * 25)



def primeNumber(input_num):
    primes = []

    cnt = 0
    # 소수는 모두 홀수이므로 홀수만 판단한다.
    for number in range(1, (input_num + 1), 2):
        # 소수의 유일한 짝수는 2!!
        if number == 1: number += 1

        cnt += 1

        flag = True
        for i in range(2, number):
            if number % i == 0:
                flag = False
                break

        # (n-1)까지 나눠 약수가 없으면 소수!
        if flag:  primes.append(number)

    print(f'count: {cnt}')
    return primes

print('< 소수 구하기 >')

for i in input_data:
    print(f' 2 ~ {i}까지 소수:\t{primeNumber(i)}')
    print('-' * 50)
