'''
 # [소인수(a prime factor)] 약수(인수)이면서 소수인 수
 # [소인수분해(factorization in prime factors)]
'''

#inputNumber = int(input('1보다 큰 정수 입력: '))
# 소인수분해
def Fractorization(input_num):
    prime_factors = []

    n = 2
    while n <= input_num:
        if input_num % n == 0:
            prime_factors.append(n)
            input_num /= n
        else:
            n += 1

    return prime_factors


print('== 소인수분해 출력 ==')
print('-' * 30)

input_data = [12, 15, 52, 72, 36]
for i in input_data:
    print(' {} 소인수분해: {}'.format(i, Fractorization(i)))
    print('-' * 30)



# <Q> ------------------------------------------------------------
# 72에 x를 곱하면 y의 제곱이 된다고 할 때, x에 해당하는 가장 작은 정수는?

#inputNumber = int(input('1보다 큰 정수 입력: '))
inputNumber = 72

n = 2
searchNumbers = []
while n <= inputNumber:
    if inputNumber % n == 0:
        print('소인수: {}'.format(n))
        # 리스트에 n과 동일한 숫자가 없을 때 추가
        if searchNumbers.count(n) == 0:
            searchNumbers.append(n)
        # 이미 리스트에 n과 같은 수가 있다면 지금 n과 짝수개를 만족한다.
        # 이는 우리가 찾는 수가 아니므로 지운다.
        elif searchNumbers.count(n) == 1:
            searchNumbers.remove(n)
        inputNumber /= n
    else:
        n += 1

print('searchNumbers: {}'.format(searchNumbers))

# 홀수 개인 소인수가 1개 이상일 수도 있다.
resultNumber = 1
for num in searchNumbers:
    resultNumber *= num

print('어떤 수의 제곱을 만들 수 있는 가장 작은 정수: {}'.format(resultNumber))

