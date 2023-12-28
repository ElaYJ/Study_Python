'''
 # [피보나치 수열(Fibonacci sequence/series)]
'''

inputN = 8

fibonacci = []
valueN = 0
valuePreN1 = 0
valuePreN2 = 0

sumN = 0

n = 1
while n <= inputN:
    if n == 1 or n == 2:
        valueN = 1
        valuePreN1 = valueN
        valuePreN2 = valueN
        fibonacci.append(valueN)
        sumN += valueN
        n += 1

    else:
        valueN = valuePreN1 + valuePreN2
        valuePreN1 = valuePreN2
        valuePreN2 = valueN
        fibonacci.append(valueN)
        sumN += valueN
        n += 1

print('피보나치 수: {}'.format(fibonacci))
print('{}번째 항의 값: {}'.format(inputN, valueN))
print('{}번째 항까지의 합: {}'.format(inputN, sumN))
print()

input_num = 8
fibonacci = [1, 1]
value_pre1 = 1
value_pre2 = 1
value_an = 0
sum_an = value_pre1 + value_pre2

for n in range(3, input_num + 1):
    value_an = value_pre2 + value_pre1
    value_pre2 = value_pre1
    value_pre1 = value_an
    fibonacci.append(value_an)
    sum_an += value_an

print('피보나치 수: {}'.format(fibonacci))
print('{}번째 항의 값: {}'.format(input_num, value_an))
print('{}번째 항까지의 합: {}'.format(input_num, sum_an))
print()


# 1, 1, 2, 3, 5, 8, 13, 21, ....
def fibonacciRecursion(n):
    if n <= 1: return n
    else:
        return fibonacciRecursion(n-2) + fibonacciRecursion(n-1)

print('피보나치 수: ( ', end='')
for n in range(1, inputN + 1):
    print(fibonacciRecursion(n), end=', ')
print('... )')

print('{}번째 항의 값: {}'.format(inputN, fibonacciRecursion(inputN)))
print()

# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
def fibo_recur(n):
    if n == 1: return 0
    elif n == 2: return 1
    else:
        return fibo_recur(n-2) + fibo_recur(n-1)

print('피보나치 수: ( ', end='')
for n in range(1, inputN + 1):
    print(fibo_recur(n), end=', ')
print('... )')

print('{}번째 항의 값: {}'.format(inputN, fibo_recur(inputN)))
print()