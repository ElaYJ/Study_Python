# <Q1> --------------------------------------------------------------------------------------
# 정수 배열 arr와 2차원 정수 배열 queries이 주어집니다. queries의 원소는 각각 하나의 query를 나타내며,
# [s, e, k] 꼴입니다. 각 query마다 순서대로 s ≤ i ≤ e인 모든 i에 대해 i가 k의 배수이면 arr[i]에 1을
# 더합니다. 위 규칙에 따라 queries를 처리한 이후의 arr를 return 하는 solution 함수

def my_solution1(arr, queries):
    for query in queries:
        s, e, k = query
        for i in range(s, e + 1):
            if i % k == 0:
                arr[i] += 1

    return arr


def solution1(arr, queries):
    for s, e, k in queries:
        for i in range(s, e+1):
            if i%k == 0:
                arr[i] += 1
    return arr


def solution2(arr, queries):
    answer = arr.copy()
    for (s, e, k) in queries:
        for i in range(s, e + 1):
            if i % k == 0:
                answer[i] += 1
    return answer



# <Q2> --------------------------------------------------------------------------------------
# 정수 start_num와 end_num가 주어질 때, start_num부터 end_num까지의 숫자를 차례로 담은 리스트를
# return하도록 solution 함수를 완성해주세요.


def my_solution2(start_num, end_num):
    answer = []
    for i in range(start_num, end_num + 1):
        answer.append(i)

    return answer


def solution3(start, end):
    return list(range(start, end + 1))


def solution4(start, end):
    return [i for i in range(start,end+1)]



# <Q3> --------------------------------------------------------------------------------------
# 모든 자연수 x에 대해서 현재 값이 x이면 x가 짝수일 때는 2로 나누고, x가 홀수일 때는 3 * x + 1로 바꾸는
# 계산을 계속해서 반복하면 언젠가는 반드시 x가 1이 되는지 묻는 문제를 콜라츠 문제라고 부릅니다.
# 그리고 위 과정에서 거쳐간 모든 수를 기록한 수열을 콜라츠 수열이라고 부릅니다.
# 계산 결과 1,000 보다 작거나 같은 수에 대해서는 전부 언젠가 1에 도달한다는 것이 알려져 있습니다.
# 임의의 1,000 보다 작거나 같은 양의 정수 n이 주어질 때 초기값이 n인 콜라츠 수열을 return 하는 solution 함수


def my_solution3(n):
    answer = [n]

    x = n
    while x > 0:
        if x == 1:
            break
        elif x % 2 == 0:
            x //= 2
            answer.append(x)
        else:
            x = 3 * x + 1
            answer.append(x)

    return answer


def solution5(n):
    answer = [n]
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        answer.append(n)
    return answer


def solution6(n):
    answer = [n]
    while n!=1:
        if n % 2:
            n = 3 * n + 1
        else:
            n //= 2
        answer.append(n)

    return answer



# <Q4> --------------------------------------------------------------------------------------
#

import re

def my_solution4(l, r):
    answer = []
    for n in range(l, r + 1):
        result = re.sub(r'[05]', "", str(n))
        if not result:
            answer.append(n)

    if not answer:
        answer.append(-1)

    return answer


def solution7(l, r):
    answer = []
    for num in range(l, r + 1):
        if not set(str(num)) - set(['0', '5']):
            answer.append(num)
    return answer if answer else [-1]

print(set(str(555)))
print(set(['0', '5']))
print(set(str('555')) - set(['0', '5']))

def solution8(l, r):
    answer = []
    for x in range(l,r+1):
        if set(str(x)).issubset({'5', '0'}):
            answer.append(x)
    return answer if answer else [-1]


num = 12
print(f'{num:#b}', f'{num:b}')
print([bin(x) for x in range(1, 65)])
print([bin(x)[2:] for x in range(1,65)])
print([int(bin(x)[2:])*5 for x in range(1,65)])
print([f'{x:b}' for x in range(1, 65)])
print([int(f'{x:b}')*5 for x in range(1, 65)])


def solution9(l, r):
    answer = []

    n = l
    for i in range(1, 65):
        if n > r: break

        n = int(f'{i:b}') * 5
        if l <= n <= r:
            answer.append(n)

    return [-1] if len(answer) == 0 else answer

print(solution9(5, 555))


def solution10(l, r):
    answer = list(filter(lambda x: l<=x and x<=r, [int(bin(i)[2:])*5 for i in range(1, 65)]))
    return answer if any(answer) else [-1]


def solution11(l, r):
    ret = []
    def f(lim, val):
        if lim == 0:
            ret.append(val)
            return

        f(lim - 1, val * 10 + 5)
        f(lim - 1, val * 10)

    f(6, 0)

    return list(i for i in ret if l <= i <= r)[::-1] or [-1]



# <Q5> --------------------------------------------------------------------------------------
# 정수 배열 arr가 주어집니다. arr를 이용해 새로운 배열 stk를 만드려고 합니다.
# 변수 i를 만들어 초기값을 0으로 설정한 후 i가 arr의 길이보다 작으면 다음 작업을 반복합니다.
#
# 만약 stk가 빈 배열이라면 arr[i]를 stk에 추가하고 i에 1을 더합니다.
# stk에 원소가 있고, stk의 마지막 원소가 arr[i]보다 작으면 arr[i]를 stk의 뒤에 추가하고 i에 1을 더합니다.
# stk에 원소가 있는데 stk의 마지막 원소가 arr[i]보다 크거나 같으면 stk의 마지막 원소를 stk에서 제거합니다.
# 위 작업을 마친 후 만들어진 stk를 return 하는 solution 함수를 완성


def my_solution5(arr):
    stk = []
    i = 0
    while i < len(arr):
        if not stk:
            stk.append(arr[i])
            i += 1
        else:
            end = stk.pop()
            if end < arr[i]:
                stk.extend([end, arr[i]])
                i += 1

    return stk

print(my_solution5([1, 4, 2, 5, 3]))


def solution12(arr):
    stk = []
    for i in range(len(arr)):
        while stk and stk[-1] >= arr[i]:
            stk.pop()
        stk.append(arr[i])
    return stk