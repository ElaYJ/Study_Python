# <Q> ----------------------------------------------------------------------------------
# 몫과 나머지

a, b = 7, 5
print(*divmod(a, b))



# <Q> ----------------------------------------------------------------------------------
# n진법으로 표기된 string을 10진법 숫자로 변환하기
#
# 문제 설명
# base 진법으로 표기된 숫자를 10진법 숫자 출력해보세요.
#
# 입력 설명
# 입력으로는 공백으로 구분된 숫자가 두 개 주어집니다.
# 첫 번째 숫자는 num을 나타내며, 두 번째 숫자는 base를 나타냅니다.
#
# 출력 설명
# base 진법으로 표기된 num을 10진법 숫자로 출력해보세요.
#
# 제한 조건
# base는 10 이하인 자연수입니다.
# num은 3000 이하인 자연수입니다.

# num, base = map(int, input().strip().split(' '))
# num, base = input().strip().split(' ')
# print(num + base)
# base = int(base)

num = '3212'
base = 5

num_list = list(map(int, [*num]))[::-1]
print(num_list)

decimal = 0
for ie in range(len(num)):
    decimal += num_list[ie] * (base ** ie)
    print(decimal)

answer = 0
for idx, number in enumerate(num[::-1]):
    answer += int(number) * (base ** idx)
    print(answer)

# Like Python
# 문자열로 데이터를 입력하는 경우 Radix를 명시해준다.
print(int(num, base))



# <Q> ----------------------------------------------------------------------------------
# 2차원 리스트 뒤집기 - ⭐️zip⭐️
# - solution 함수는 이차원 리스트, mylist를 인자로 받습니다
# - solution 함수는 mylist 원소의 행과 열을 뒤집은 한 값을 리턴해야합니다.
# 예를 들어 mylist [[1, 2, 3], [4, 5, 6], [7, 8, 9]]가 주어진 경우,
# solution 함수는 [[1, 4, 7], [2, 5, 8], [3, 6, 9]] 을 리턴하면 됩니다.

answer = []
mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
tmp = {}
for ls1 in mylist:
    for idx, ele in enumerate(ls1):
        if idx not in tmp.keys():
            tmp[idx]=[]
        tmp[idx].append(ls1[idx])
answer = list(tmp.values())
print(tmp.values())
print(answer)


new_list = list(map(list, zip(*mylist)))
print(list(zip(*mylist)))
print(new_list)



# <Q> ----------------------------------------------------------------------------------
# i번째 원소와 i+1번째 원소
# 숫자를 담은 리스트 mylist가 solution 함수의 파라미터로 주어집니다.
# solution 함수가 mylist의 i번째 원소와 i+1번째 원소의 차를 담은 일차원 리스트에 차례로 담아
# 리턴하도록 코드를 작성해주세요.
# 단, 마지막에 있는 원소는 (마지막+1)번째의 원소와의 차를 구할 수 없으니, 이 값은 구하지 않습니다.

mylist = [83, 48, 13, 4, 71, 11]

answer = []
for i in range(len(mylist)-1):
    answer.append(abs(mylist[i]-mylist[i+1]))
print(answer)

answer = []
for num1, num2 in zip(mylist, mylist[1:]):
    answer.append(abs(num1-num2))
print(answer)


keys = [1, 2, 3]
values = [['a','b','c'], [4, 5], ['d', 6, 7]]
print(dict(zip(keys, values)))



# ---------------------------------------------------------------------------------------

import itertools

iterable1 = 'ABCD'
iterable2 = 'xy'
iterable3 = '1234'
print(list(itertools.product(iterable1, iterable2, iterable3)))
# [('A', 'x', '1'), ('A', 'x', '2'), ('A', 'x', '3'), ('A', 'x', '4'),
# ('A', 'y', '1'), ('A', 'y', '2'), ('A', 'y', '3'), ('A', 'y', '4'),
# ('B', 'x', '1'), ('B', 'x', '2'), ('B', 'x', '3'), ('B', 'x', '4'),
# ('B', 'y', '1'), ('B', 'y', '2'), ('B', 'y', '3'), ('B', 'y', '4'),
# ('C', 'x', '1'), ('C', 'x', '2'), ('C', 'x', '3'), ('C', 'x', '4'),
# ('C', 'y', '1'), ('C', 'y', '2'), ('C', 'y', '3'), ('C', 'y', '4'),
# ('D', 'x', '1'), ('D', 'x', '2'), ('D', 'x', '3'), ('D', 'x', '4'),
# ('D', 'y', '1'), ('D', 'y', '2'), ('D', 'y', '3'), ('D', 'y', '4')]



# <Q> ----------------------------------------------------------------------------------
# 2차원 리스트를 1차원 리스트로 만들기
# 문자열을 담은 이차원 리스트, mylist 가 solution 함수의 파라미터로 주어집니다.
# solution 함수가 mylist를 일차원 리스트로 만들어 리턴하도록 코드를 작성해주세요.

mylist = [['A', 'B'], ['X', 'Y'], ['1']]
answer = []
for ls in mylist:
    for e in ls:
        answer.append(e)
print(answer)

my_list = [[1, 2], [3, 4], [5, 6]]
answer = []
for element in my_list:
    answer += element
print(answer)


# 방법 1 - sum 함수
answer = sum(my_list, [])
print(answer)


# 방법 2 - itertools.chain
import itertools

answer = list(itertools.chain.from_iterable(my_list))
print(answer)


# 방법 3 - itertools와 unpacking
import itertools

answer = list(itertools.chain(*my_list))
print(answer)




# <Q> ----------------------------------------------------------------------------------
# 순열과 조합
# 숫자를 담은 일차원 리스트, mylist에 대해 mylist의 원소로 이루어진 모든 순열을 사전순으로
# 리턴하는 함수 solution을 완성해주세요.

import itertools

pool = ['A', 'B', 'C']

# 3개의 원소로 순열 만들기, 3P3
print(list(map(list, itertools.permutations(pool))))

# 2개의 원소로 순열 만들기, 3P2
print(list(map(''.join, itertools.permutations(pool, 2))))


mylist = [2, 1]
def solution(mylist):
    answer = list(map(list, itertools.permutations(mylist)))
    print(answer)
    return sorted(answer)
print(solution(mylist))




# <Q> ----------------------------------------------------------------------------------
# 가장 많이 등장하는 알파벳 찾기
# 이 문제에는 표준 입력으로 문자열, mystr이 주어집니다. mystr에서 가장 많이 등장하는 알파벳만을
# 사전 순으로 출력하는 코드를 작성해주세요.

my_str = 'dfdefdgf' # 'ccddd'

import collections

most_common = collections.Counter(my_str).most_common()
print(collections.Counter(my_str))
print(most_common)

max_count = most_common[0][1]
print(max_count)

# 방법1.
answer = []
for i in most_common:
    if i[1] == max_count:
        answer.append(i[0])
#--> 요즘은 위와 같은 일을 처리할 때 for문 보다는 filter 함수를 쓰는걸 좀 더 선호
print(''.join(sorted(answer)))

# 방법2. list comprehension
answer = ''.join(sorted([i[0] for i in most_common if i[1]==max_count]))
print(answer)

# 방법3. filter()
answer = [s[0] for s in list(filter(lambda x: x[1]==max_count, most_common))]
print(''.join(sorted(answer)))




# <Q> ----------------------------------------------------------------------------------
# for 문과 if문을 한번에
# 정수를 담은 리스트 mylist를 입력받아,
# 이 리스트의 원소 중 짝수인 값만을 제곱해 담은 새 리스트를 리턴하는 solution함수를 완성해주세요.
# 예를 들어, [3, 2, 6, 7]이 주어진 경우#
# 3은 홀수이므로 무시합니다.
# 2는 짝수이므로 제곱합니다.
# 6은 짝수이므로 제곱합니다.
# 7은 홀수이므로 무시합니다.
# 따라서 2의 제곱과 6의 제곱을 담은 리스트인 [4, 36]을 리턴해야합니다.

mylist = [3,4,6,7]
answer = [n**2 for n in mylist if n%2==0]
print(answer)



# <Q> ----------------------------------------------------------------------------------
# flag OR else
# 본 문제에서는 자연수 5개가 주어집니다.
# 1. 숫자를 차례로 곱해 나온 수가 제곱수[1]가 되면 found를 출력하고
# 2. 모든 수를 곱해도 제곱수가 나오지 않았다면 not found를 출력하는 코드를 작성

import math

# 2 4 2 5 1 --> found / 5 1 2 3 1 --> not found
# numbers = [int(input()) for _ in range(5)]
# print(numbers)

numbers = [5, 1, 2, 3, 1]
multi = 1
for num in numbers:
    multi *= num
    if math.sqrt(multi) == int(math.sqrt(multi)):
        print('found')
        break
else:
    print('not found')


