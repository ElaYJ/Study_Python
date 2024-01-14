# <Q1> --------------------------------------------------------------------------------------
# boolean 변수 x1, x2, x3, x4가 매개변수로 주어질 때, 다음의 식의 true/false를 return 하는
# solution 함수를 작성해 주세요.
#
# (x1 ∨ x2) ∧ (x3 ∨ x4) --> ∨는 or 연산, ∧는 and 연산


def my_solution1(x1, x2, x3, x4):
    answer = (x1 or x2) and (x3 or x4)
    return answer


def solution1(x1, x2, x3, x4):
    return (x1 | x2) & (x3 | x4)




# <Q2> --------------------------------------------------------------------------------------
# 1부터 6까지 숫자가 적힌 주사위가 네 개 있습니다. 네 주사위를 굴렸을 때 나온 숫자에 따라 다음과 같은 점수를 얻습니다.
# 네 주사위에서 나온 숫자가 모두 p로 같다면 1111 × p점을 얻습니다.
# 세 주사위에서 나온 숫자가 p로 같고 나머지 다른 주사위에서 나온 숫자가 q(p ≠ q)라면 (10 × p + q)2 점을 얻습니다.
# 주사위가 두 개씩 같은 값이 나오고, 나온 숫자를 각각 p, q(p ≠ q)라고 한다면 (p + q) × |p - q|점을 얻습니다.
# 어느 두 주사위에서 나온 숫자가 p로 같고 나머지 두 주사위에서 나온 숫자가 각각 p와 다른 q, r(q ≠ r)이라면 q × r점을 얻습니다.
# 네 주사위에 적힌 숫자가 모두 다르다면 나온 숫자 중 가장 작은 숫자 만큼의 점수를 얻습니다.
# 네 주사위를 굴렸을 때 나온 숫자가 정수 매개변수 a, b, c, d로 주어질 때, 얻는 점수를 return 하는 solution 함수를 작성해 주세요.

a, b, c = set([1, 2, 3, 2])
print(a, b, c)
p, q, r = {1, 2, 3, 2}
print(p, q, r)
print({4, 1, 4, 4} - {4})

def my_solution2(a, b, c, d):
    answer = 0
    set_num = {a, b, c, d}
    set_len = len(set_num)

    if set_len == 1:
        answer = 1111 * a
    elif set_len == 2:
        if a == b == c or a == b == d or a == c == d:
            q = list(set_num - {a})[0]
            answer = (10 * a + q) ** 2
        elif b == c == d:
            answer = (10 * b + a) ** 2
        else:
            p, q = set_num
            answer = (p + q) * abs(p - q)
    elif set_len == 3:
        if a == b:
            answer = c * d
        elif a == c:
            answer = b * d
        elif a == d:
            answer = b * c
        elif b == c:
            answer = a * d
        elif b == d:
            answer = a * c
        elif c == d:
            answer = a * b
    elif set_len == 4:
        answer = min(a, b, c, d)

    return answer


def solution2(a, b, c, d):
    l = [a,b,c,d]
    c = [l.count(x) for x in l]
    if max(c) == 4:
        return 1111*a
    elif max(c) == 3:
        return (10 * l[c.index(3)] + l[c.index(1)]) ** 2
    elif max(c) == 2:
        if min(c) == 1:
            return eval('*'.join([str(l[i]) for i, x in enumerate(c) if x == 1]))
        else:
            return (max(l) + min(l)) * abs(max(l) - min(l))
    else:
        return min(l)


def solution3(a, b, c, d):
    nums = [a, b, c, d]
    counts = [nums.count(i) for i in nums]
    if max(counts) == 4:
        return a * 1111
    elif max(counts) == 3:
        p = nums[counts.index(3)]
        q = nums[counts.index(1)]
        return (10 * p + q) ** 2
    elif max(counts) == 2:
        if min(counts) == 2:
            return (a + c) * abs(a - c) if a == b else (a + b) * abs(a - b)
        else:
            p = nums[counts.index(2)]
            return (a * b * c * d) / p**2
    else:
        return min(nums)


def solution(a, b, c, d):
    nums = [a, b, c, d]
    counts = [nums.count(i) for i in nums]
    print(nums, counts)
    print(counts.index(3), counts.index(1))

solution(4, 1, 4, 4)



# <Q3> --------------------------------------------------------------------------------------
# 문자열 my_string과 정수 배열 index_list가 매개변수로 주어집니다. my_string의 index_list의 원소들에
# 해당하는 인덱스의 글자들을 순서대로 이어 붙인 문자열을 return 하는 solution 함수

def my_solution3(my_string, index_list):
    answer = ''
    for idx in index_list:
        answer += my_string[idx]
    return answer


def solution4(my_string, index_list):
    return ''.join([my_string[idx] for idx in index_list])


def solution5(my_string, index_list):
    return ''.join(map(lambda x: my_string[x], index_list))


def test_sol(str, idx):
    print(map(lambda x: str[x], idx))
    print(''.join(map(lambda x: str[x], idx)))
test_sol('cvsgiorszzzmrpaqpe', [16, 6, 5, 3, 12, 14, 11, 11, 17, 12, 7])




# <Q4> --------------------------------------------------------------------------------------
# 음이 아닌 정수를 9로 나눈 나머지는 그 정수의 각 자리 숫자의 합을 9로 나눈 나머지와 같은 것이 알려져 있습니다.
# 이 사실을 이용하여 음이 아닌 정수가 문자열 number로 주어질 때, 이 정수를 9로 나눈 나머지를 return

print("+".join("78720646226947352489"))
print(eval("+".join("78720646226947352489")))

def my_solution4(number):
    sum_num = eval("+".join(number))
    answer = sum_num % 9
    return answer


def solution6(number):
    return sum(list(map(int, number))) % 9


def solution7(number):
    answer = sum(int(x) for x in number)
    return answer%9





# <Q5> --------------------------------------------------------------------------------------
# 문자열 my_string과 이차원 정수 배열 queries가 매개변수로 주어집니다. queries의 원소는 [s, e] 형태로,
# my_string의 인덱스 s부터 인덱스 e까지를 뒤집으라는 의미입니다. my_string에 queries의 명령을 순서대로
# 처리한 후의 문자열을 return 하는 solution 함수를 작성

str = "remrgorpsam"
print("".join(reversed(str[0:8]))+str[8:])
print(str[8:0:-1], str[0:8][::-1], str[0:1])

original_string = "Hello, World!"
reversed_string = original_string[::-1]
print(reversed_string)


def my_solution5(my_string, queries):
    answer = my_string
    for s, e in queries:
        answer = answer[:s] + "".join(reversed(answer[s:e+1])) + answer[e+1:]

    return answer


def solution8(my_string, queries):
    for (s, e) in queries:
        my_string = my_string[:s] + my_string[s:e+1][::-1] + my_string[e+1:]
    return my_string


def solution9(my_string, queries):
    answer = [*my_string] #--> answer=list(my_string)과 동일
    for s,e in queries:
        answer[s:e+1]=answer[s:e+1][::-1]
    return ''.join(answer)

print(solution9("rermgorpsam", [[2, 3], [0, 7], [5, 9], [6, 10]]))

print(list("string"), [*"string"])

dic = {'k1': 'val1', 'k2': 'val2', 'k3': 'val3'}
#print(**dic)

keys = ['a', 'b', 'c']
values = [1, 2, 3]

# 딕셔너리 생성 시 **를 사용하여 언패킹
my_dict = {**dict(zip(keys, values))}
print(my_dict)