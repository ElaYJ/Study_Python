# <Q> -------------------------------------------------------------------------------
# 정수 num과 n이 매개 변수로 주어질 때,
# num이 n의 배수이면 1을 return n의 배수가 아니라면 0을 return하도록 solution 함수를 완성

def my_solution1(num, n):
    answer = 1 if num % n == 0 else 0
    return answer

# num%n은 int 값이지만, 이를 not() 함수 안에 넣으면 int가 bool로 해석되어서
# num%n이 0이면 False로, 0이 아니면 True로 해석
def solution1(num, n):
    return int(not(num % n))

def solution2(num, n):
    return int(num % n == 0)

def solution3(num, n):
    return 1 if not num % n else 0


# <Q> -------------------------------------------------------------------------------
# 정수 number와 n, m이 주어집니다.
# number가 n의 배수이면서 m의 배수이면 1을 아니라면 0을 return하도록 solution 함수를 완성

def my_solution2(number, n, m):
    answer = 1 if number % n == 0 and number % m == 0 else 0
    return answer

def solution4(number, n, m):
    return int((number % n == 0) & (number % m == 0))


# <Q> -------------------------------------------------------------------------------
# 양의 정수 n이 매개변수로 주어질 때, n이 홀수라면 n 이하의 홀수인 모든 양의 정수의 합을 return 하고
# n이 짝수라면 n 이하의 짝수인 모든 양의 정수의 제곱의 합을 return 하는 solution 함수를 작성

def my_solution3(n):
    answer = 0
    if n % 2 == 0:
        for i in range(n, 0, -2):
            answer += i ** 2

    else:
        for j in range(n, 0, -2):
            answer += j

    return answer

def solution5(n):
    if n % 2 == 0:
        return sum([i**2 for i in range(n, 0, -2)])
    else:
        return sum([j for j in range(n, 0, -2)])


# <Q> -------------------------------------------------------------------------------
# 문자열에 따라 다음과 같이 두 수의 크기를 비교하려고 합니다.
# 두 수가 n과 m이라면
# ">", "=" : n >= m
# "<", "=" : n <= m
# ">", "!" : n > m
# "<", "!" : n < m
# 두 문자열 ineq와 eq가 주어집니다. ineq는 "<"와 ">"중 하나고, eq는 "="와 "!"중 하나입니다.
# 그리고 두 정수 n과 m이 주어질 때, n과 m이 ineq와 eq의 조건에 맞으면 1을 아니면 0을 return하도록 solution 함수를 완성

def my_solution4(ineq, eq, n, m):
    if ineq == '>':
        if eq == '=':
            return int(n >= m)
        else: return int(n > m)
    else:
        if eq == '=':
            return int(n <= m)
        else: return int(n < m)

def solution6(ineq, eq, n, m):
    return int(eval(str(n) + ineq + eq.replace('!', '') + str(m)))

def solution7(ineq, eq, n, m):
    if eq == '!':
        eq = ''
    return int(eval(f'{n} {ineq}{eq} {m}'))


# <Q> -------------------------------------------------------------------------------
# 두 정수 a, b와 boolean 변수 flag가 매개변수로 주어질 때,
# flag가 true면 a + b를 false면 a - b를 return 하는 solution 함수를 작성

def my_solution5(a, b, flag):
    answer = a + b if flag else a - b
    return answer

def solution8(a, b, flag):
    return a + b * (2 * int(flag) - 1)


solution9 = lambda a, b, f: [a-b, a+b][f]
