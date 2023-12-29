# 4 5
a, b = map(int, input().strip().split(' '))
print(type(a), type(b))
print(f'a = {a}\nb = {b}')



# <Q> --------------------------------------------------------------------------
# 알파벳 대소문자 변경
# aBcDeFg

print(input().swapcase())

print(''.join(x.upper() if x == x.lower() else x.lower() for x in input()))



# <Q> --------------------------------------------------------------------------
# escape 문자 활용

print('!@#$%^&*(\\\'"<>?:;')
print('''!@#$%^&*(\\'"<>?:;''')
print(r'!@#$%^&*(\'"<>?:;') # raw



# <Q> --------------------------------------------------------------------------
# 두 개의 문자열 str1, str2가 공백으로 구분되어 입력으로 주어진다.
# 입출력 예와 같이 str1과 str2을 이어서 출력하는 코드를 작성
# apple pen
# Hello World!

str1, str2 = input().strip().split(' ')
print(str1+str2)

print(input().strip().replace(' ', ''))
print(''.join(input().strip().split(' ')))
print(''.join(input().split()))



# <Q> --------------------------------------------------------------------------
# str에서 char 하나씩 아래로 출력

for a in input():
    print(a)

print('\n'.join(input()))



# <Q> ----------------------------------------------------------------------------------------------
# 자연수 n이 입력으로 주어졌을 때 만약 n이 짝수이면 "n is even"을, 홀수이면 "n is odd"를 출력하는 코드를 작성

n = int(input())
if n % 2 == 0:
    print(n, 'is even')
else:
    print(n, 'is odd')

print(f"{n} is {'even' if n % 2 == 0 else 'odd'}")
print(f"{n} is odd" if n % 2 else f"{n} is even")
print(f'{n} is', 'odd' if n % 2 else 'even')
# n&1했을 때 1이면 홀수고 0이면 짝수이니까 만약 짝수라면 0번째자리인 e부터 시작해서 2칸씩 띄워서 even이 나오게 됨
print(f"{n} is {'eovdedn'[n&1::2]}")



# <Q> ----------------------------------------------------------------------------------------------
# 문자열 my_string, overwrite_string과 정수 s가 주어집니다.
# 문자열 my_string의 인덱스 s부터 overwrite_string의 길이만큼을 문자열 overwrite_string으로 바꾼 문자열을
# return 하는 solution 함수를 작성

def solution(my_string, overwrite_string, s):
    e = s + len(overwrite_string)
    answer = my_string[:s] + overwrite_string + my_string[e:]
    return answer

print(solution("He11oWor1d", "lloWorl", 2))



