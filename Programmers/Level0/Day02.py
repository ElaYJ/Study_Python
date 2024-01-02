# <Q> -------------------------------------------------------------------------------
# 길이가 같은 두 문자열 str1과 str2가 주어집니다.
# 두 문자열의 각 문자가 앞에서부터 서로 번갈아가면서 한 번씩 등장하는 문자열을 만들어 return 하는 함수
#  str1	     str2	     result
# "aaaaa"	"bbbbb"	    "ababababab"

def my_solution(str1, str2):
    answer = ''
    for i in range(len(str1)):
        answer += (str1[i] + str2[i])

    return answer


def solution1(str1, str2):
    answer = ''.join([str1[i] + str2[i] for i in range(len(str1))])
    return answer


def solution2(str1, str2):
    answer = []
    for i in range(len(str1)):
        answer.append(str1[i])
        answer.append(str2[i])
    return ''.join(answer)


def solution3(str1, str2):
    answer = ''
    for s1, s2 in zip(str1, str2):
        answer += s1 + s2
    return answer


def solution4(str1, str2):
    return ''.join(i+j for i, j in zip(str1, str2))


# <Q> -------------------------------------------------------------------------------
# 문자들이 담겨있는 배열 arr가 주어집니다. arr의 원소들을 순서대로 이어 붙인 문자열을 return 하는 solution함수

def my_solution2(arr):
    answer = ''.join(arr[i] for i in range(len(arr)))
    return answer

def solution5(arr):
    return ''.join(arr)


solution6 = lambda arr: ''.join(arr)


# <Q> -------------------------------------------------------------------------------
# 연산 ⊕는 두 정수에 대한 연산으로 두 정수를 붙여서 쓴 값을 반환합니다. 예를 들면 다음과 같습니다.
# 12 ⊕ 3 = 123
# 3 ⊕ 12 = 312
# 양의 정수 a와 b가 주어졌을 때, a ⊕ b와 b ⊕ a 중 더 큰 값을 return 하는 solution 함수를 완성해 주세요.
# 단, a ⊕ b와 b ⊕ a가 같다면 a ⊕ b를 return 합니다.

def my_solution3(a, b):
    ab = int(str(a) + str(b))
    ba = int(str(b) + str(a))

    return ba if ab < ba else ab


def solution7(a, b):
    return max(f"{a}{b}", f"{b}{a}")  # return type -> str


def solution8(a, b):
    a, b = str(a), str(b)
    return max((a+b), (b+a))  # return type -> str


# <Q> -------------------------------------------------------------------------------
# 연산 ⊕는 두 정수에 대한 연산으로 두 정수를 붙여서 쓴 값을 반환합니다. 예를 들면 다음과 같습니다.
# 12 ⊕ 3 = 123
# 3 ⊕ 12 = 312
# 양의 정수 a와 b가 주어졌을 때, a ⊕ b와 2 * a * b 중 더 큰 값을 return하는 solution 함수를 완성해 주세요.
# 단, a ⊕ b와 2 * a * b가 같으면 a ⊕ b를 return 합니다.

def my_solution4(a, b):
    sa, sb = str(a), str(b)
    answer = max(int(sa+sb), (2*a*b))
    return answer


def solution9(a, b):
    return max(int(str(a) + str(b)), 2 * a * b)




