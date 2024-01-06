# <Q1> -------------------------------------------------------------------------------
# 문자열 code가 주어집니다. code를 앞에서부터 읽으면서 만약 문자가 "1"이면 mode를 바꿉니다.
# mode에 따라 code를 읽어가면서 문자열 ret을 만들어냅니다. mode는 0과 1이 있으며,
# idx를 0 부터 code의 길이 - 1 까지 1씩 키워나가면서 code[idx]의 값에 따라 다음과 같이 행동합니다.
# mode가 0일 때
# code[idx]가 "1"이 아니면 idx가 짝수일 때만 ret의 맨 뒤에 code[idx]를 추가합니다.
# code[idx]가 "1"이면 mode를 0에서 1로 바꿉니다.
# mode가 1일 때
# code[idx]가 "1"이 아니면 idx가 홀수일 때만 ret의 맨 뒤에 code[idx]를 추가합니다.
# code[idx]가 "1"이면 mode를 1에서 0으로 바꿉니다.
# 문자열 code를 통해 만들어진 문자열 ret를 return 하는 solution 함수를 완성해 주세요.
# 단, 시작할 때 mode는 0이며, return 하려는 ret가 만약 빈 문자열이라면 대신 "EMPTY"를 return 합니다.
# "abc1abc1abc" -> "acbac"

def my_solution1(code):
    mode = False  # 0
    ret = ''
    for idx in range(len(code)):
        if code[idx] == "1":
            mode = not mode
        else:
            if mode and idx % 2 == 1:
                ret += code[idx]
            elif not mode and idx % 2 == 0:
                ret += code[idx]

    return ret if len(ret) > 0 else "EMPTY"


def solution(code):
    answer = ''

    mode = 0
    for i in range(len(code)):
        if code[i] == '1':
            mode ^= 1
        else:
            if i % 2 == mode:
                answer += code[i]

    return answer if answer else 'EMPTY'


def solution1(code):
    return "".join(code.split("1"))[::2] or "EMPTY"


# <Q2> -------------------------------------------------------------------------------
# 두 정수 a, d와 길이가 n인 boolean 배열 included가 주어집니다.
# 첫째항이 a, 공차가 d인 등차수열에서 included[i]가 i + 1항을 의미할 때,
# 이 등차수열의 1항부터 n항까지 included가 true인 항들만 더한 값을 return 하는 solution 함수를 작성
# 입출력 예
# a	d	included                                        	result
# 3	4	[true, false, false, true, true]                   	37
# 7	1	[false, false, false, true, false, false, false]	10


def my_solution2(a, d, included):
    answer = 0
    for n in range(len(included)):
        if included[n]:
            an = a + n * d
            answer += an

    return answer


def solution2(a, d, included):
    answer = 0
    for i in range(len(included)):
        answer += (a + d * i) * int(included[i])

    return answer


def solution3(a, d, included):
    return sum(a + i * d for i, f in enumerate(included) if f)


# <Q3> -------------------------------------------------------------------------------
# 1부터 6까지 숫자가 적힌 주사위가 세 개 있습니다.
# 세 주사위를 굴렸을 때 나온 숫자를 각각 a, b, c라고 했을 때 얻는 점수는 다음과 같습니다.
#
# 세 숫자가 모두 다르다면 a + b + c 점을 얻습니다.
# 세 숫자 중 어느 두 숫자는 같고 나머지 다른 숫자는 다르다면 (a + b + c) × (a2 + b2 + c2 )점을 얻습니다.
# 세 숫자가 모두 같다면 (a + b + c) × (a2 + b2 + c2 ) × (a3 + b3 + c3 )점을 얻습니다.
# 세 정수 a, b, c가 매개변수로 주어질 때, 얻는 점수를 return 하는 solution 함수

def my_solution3(a, b, c):
    answer = a + b + c

    if a == b or b == c or a == c:
        answer *= (a * a + b * b + c * c)

    if a == b == c:
        answer *= (a ** 3 + b ** 3 + c ** 3)

    return answer


def solution4(a, b, c):
    check=len(set([a,b,c]))
    if check==1:
        return 3*a * 3*(a**2) * 3*(a**3) # 3 ** 3 * a ** 6
    elif check==2:
        return (a+b+c)*(a**2+b**2+c**2)
    else:
        return (a+b+c)


def solution5(a, b, c):
    list = [a, b, c]
    answer = 1
    for i in range(4-len(set(list))):
        answer *= a**(i+1)+b**(i+1)+c**(i+1)
    return answer



# <Q4> -------------------------------------------------------------------------------
# 정수가 담긴 리스트 num_list가 주어질 때,
# 모든 원소들의 곱이 모든 원소들의 합의 제곱보다 작으면 1을 크면 0을 return하도록 solution 함수를 완성


def solution6(num_list):
    mul = 1
    for n in num_list:
        mul *= n
    return int(mul < sum(num_list) ** 2)


def solution7(num_list):
    s=sum(num_list)**2
    m=eval('*'.join([str(n) for n in num_list]))
    return 1 if s>m else 0

num_list = [3, 4, 5, 2, 1]
print("*".join([str(n) for n in num_list]))
print("".join([str(n) for n in num_list]))


import math
def solution8(num_list):
    answer = 0
    if math.prod(num_list) < (sum(num_list)**2):
        answer = 1
    return answer


from functools import reduce
def solution9(num_list):
    return 1 if (reduce(lambda x, y: x * y, num_list)) < (sum(num_list) ** 2) else 0


# <Q5> -------------------------------------------------------------------------------
# 정수가 담긴 리스트 num_list가 주어집니다.
# num_list의 홀수만 순서대로 이어 붙인 수와 짝수만 순서대로 이어 붙인 수의 합을 return하도록 solution 함수를 완성


def my_solution5(num_list):
    odd = ''
    even = ''
    for n in num_list:
        if n % 2 == 0:
            even += str(n)
        else:
            odd += str(n)

    return int(odd) + int(even)
    return eval(odd+'+'+even)



