# <Q1> -------------------------------------------------------------------------------
# 정수 리스트 num_list가 주어질 때,
# 마지막 원소가 그전 원소보다 크면 마지막 원소에서 그전 원소를 뺀 값을
# 마지막 원소가 그전 원소보다 크지 않다면 마지막 원소를 두 배한 값을 추가하여 return

def my_solution1(num_list):
    answer = num_list
    idx = len(num_list) - 1
    last_num = num_list[idx]
    befo_num = num_list[idx - 1]

    if last_num > befo_num:
        answer.append(last_num - befo_num)
    else:
        answer.append(last_num * 2)

    return answer


def solution1(num_list):
    n1, n2 = num_list[-1], num_list[-2]
    if n1 > n2:
        num_list.append(n1 - n2)
    else:
        num_list.append(n1 * 2)
    return num_list


def solution2(num_list):
    num_list.append(num_list[-1] - num_list[-2] if num_list[-1] > num_list[-2] else num_list[-1] * 2)
    return num_list


def solution3(num_list):
    if num_list[-1]>num_list[-2]:
        return num_list+[num_list[-1]-num_list[-2]]
    return num_list+[num_list[-1]*2]



# <Q2> -------------------------------------------------------------------------------
# 정수 n과 문자열 control이 주어집니다. control은 "w", "a", "s", "d"의 4개의 문자로 이루어져 있으며,
# control의 앞에서부터 순서대로 문자에 따라 n의 값을 바꿉니다.#
# "w" : n이 1 커집니다.
# "s" : n이 1 작아집니다.
# "d" : n이 10 커집니다.
# "a" : n이 10 작아집니다.
# 위 규칙에 따라 n을 바꿨을 때 가장 마지막에 나오는 n의 값을 return 하는 solution 함수

def my_solution2(n, control):
    answer = [n]
    for i in range(len(control)):
        if control[i] == "w":
            answer.append(+1)
        elif control[i] == "s":
            answer.append(-1)
        elif control[i] == "d":
            answer.append(+10)
        elif control[i] == "a":
            answer.append(-10)

    return sum(answer)


def solution4(n, control):
    answer = n
    c = { 'w':1, 's':-1, 'd':10, 'a':-10}
    for i in control:
        answer += c[i]
    return answer

def solution5(n, control):

    control_dict = {'w' : "1" , 's' : "-1", 'd' : "10", 'a' : "-10"}

    return eval("+".join(control_dict[letter] for letter in control)) + n


def solution6(n, control):
    key = dict(zip(['w','s','d','a'], [1,-1,10,-10]))
    return n + sum([key[c] for c in control])


def solution7(n, control):
    return n + 10*(control.count('d')-control.count('a')) + (control.count('w')-control.count('s'))



# <Q3> -------------------------------------------------------------------------------
# 정수 배열 numLog가 주어집니다. 처음에 numLog[0]에서 부터 시작해 "w", "a", "s", "d"로 이루어진
# 문자열을 입력으로 받아 순서대로 다음과 같은 조작을 했다고 합시다.#
# "w" : 수에 1을 더한다.
# "s" : 수에 1을 뺀다.
# "d" : 수에 10을 더한다.
# "a" : 수에 10을 뺀다.
# 그리고 매번 조작을 할 때마다 결괏값을 기록한 정수 배열이 numLog입니다.
# 즉, numLog[i]는 numLog[0]로부터 총 i번의 조작을 가한 결과가 저장되어 있습니다.#
# 주어진 정수 배열 numLog에 대해 조작을 위해 입력받은 문자열을 return 하는 solution 함수

def my_solution3(numLog):
    answer = ''
    dic = {1: "w", -1: "s", 10: "d", -10: "a"}
    for i in range(len(numLog)-1):
        answer += dic[numLog[i + 1] - numLog[i]]

    return answer

#print(solution([0, 1, 0, 10, 0, 1, 0, 10, 0, -1, -2, -1])) # wsdawsdassw

def solution8(log):
    res=''
    joystick=dict(zip([1,-1,10,-10],['w','s','d','a']))
    for i in range(1,len(log)):
        res+=joystick[log[i]-log[i-1]]
    return res



# <Q4> -------------------------------------------------------------------------------
# 정수 배열 arr와 2차원 정수 배열 queries이 주어집니다.
# queries의 원소는 각각 하나의 query를 나타내며, [i, j] 꼴입니다.
# 각 query마다 순서대로 arr[i]의 값과 arr[j]의 값을 서로 바꿉니다.
# 위 규칙에 따라 queries를 처리한 이후의 arr를 return 하는 solution 함수


def my_solution4(arr, queries):
    answer = arr
    for q in queries:
        answer[q[0]], answer[q[1]] = answer[q[1]], answer[q[0]]

    return answer


def solution9(arr, queries):
    for i, j in queries:
        arr[i], arr[j] = arr[j], arr[i]
    return arr


# <Q5> -------------------------------------------------------------------------------
# 정수 배열 arr와 2차원 정수 배열 queries이 주어집니다.
# queries의 원소는 각각 하나의 query를 나타내며, [s, e, k] 꼴입니다.
# 각 query마다 순서대로 s ≤ i ≤ e인 모든 i에 대해 k보다 크면서 가장 작은 arr[i]를 찾습니다.
# 각 쿼리의 순서에 맞게 답을 저장한 배열을 반환하는 solution 함수를 완성해 주세요.
# 단, 특정 쿼리의 답이 존재하지 않으면 -1을 저장합니다.

def my_solution5(arr, queries):
    answer = []
    for s, e, k in queries:
        temp = []
        for i in range(s, e + 1):
            if arr[i] > k:
                temp.append(arr[i])

        if len(temp) != 0:
            min = temp[0]
            if len(temp) > 1:
                for n in temp:
                    if min > n: min = n
            answer.append(min)
        else:
            answer.append(-1)

    return answer


def solution10(arr, queries):
    answer = []
    for s, e, k in queries:
        tmp = []
        for x in arr[s:e+1]:
            if x > k:
                tmp.append(x)
        answer.append(-1 if not tmp else min(tmp))
    return answer


def solution11(arr, queries):
    answer = []
    for s, e, k in queries:
        l = [i for i in arr[s:e+1] if i > k]
        answer.append(-1 if len(l) == 0 else min(l))
    return answer


# ????????????
def solution12(arr, queries):
    return list(map(lambda x: -1 if x==10**6 else x, [min(list(filter(lambda x: x > k, arr[s:e+1])) + [10**6]) for s, e, k in queries]))


