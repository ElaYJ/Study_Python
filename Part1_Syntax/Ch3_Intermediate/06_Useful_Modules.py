# 수학 관련 내장 함수

# 합
listVar = [2, 5, 3.14, 58, 10, 2]
print(f'sum(listVar): {sum(listVar)}')

# 최댓값
listVar = [2, 5, 3.14, 58, 10, 2]
print(f'max(listVar): {max(listVar)}')

# 최솟값
listVar = [2, 5, 3.14, 58, 10, 2]
print(f'min(listVar): {min(listVar)}')

# 거듭제곱
print(f'pow(13, 2): {pow(13, 2)}')
print(f'pow(13, 3): {pow(13, 3)}')
print(f'pow(13, 4): {pow(13, 4)}')

# 반올림
print(f'round(3.141592, 1): {round(3.141592, 1)}')
print(f'round(3.141592, 2): {round(3.141592, 2)}')
print(f'round(3.141592, 3): {round(3.141592, 3)}')
print(f'round(3.141592, 4): {round(3.141592, 4)}')
print(f'round(3.141592, 5): {round(3.141592, 5)}')




# math 모듈
import math

#절댓값
print(f'math.fabs(-10): {math.fabs(-10)}')
print(f'math.fabs(-0.12895): {math.fabs(-0.12895)}')

# 올림
print(f'math.ceil(5.21): {math.ceil(5.21)}')
print(f'math.ceil(-5.21): {math.ceil(-5.21)}')

# 내림
print(f'math.floor(5.21): {math.floor(5.21)}')
print(f'math.floor(-5.21): {math.floor(-5.21)}')

# 버림
print(f'math.trunc(5.21): {math.trunc(5.21)}')
print(f'math.trunc(-5.21): {math.trunc(-5.21)}')

# 최대공약수
print(f'math.gcd(14, 21): {math.gcd(14, 21)}')

# 팩토리얼
print(f'math.factorial(10): {math.factorial(10)}')

# 제곱근
print(f'math.sqrt(4): {math.sqrt(4)}')
print(f'math.sqrt(12): {math.sqrt(12)}')


# random 모듈
import random

# 0이상 1미만 난수
print(f'random.random(): {random.random()}')

# 1이상 20이하 난수
print(f'random.randint(1, 20): {random.randint(1, 20)}')

# 1이상 20미만 난수
print(f'random.randrange(1, 20): {random.randrange(1, 20)}')

# 1이상 21미만 난수 5개
print(f'random.sample(range(1, 21), 5): {random.sample(range(1, 21), 5)}')

# 무작위 한개 추출
listVar = [0, 1, 2, 3, 4, 5, 6]
print(f'random.choice(listVar): {random.choice(listVar)}')

# 섞음
print(f'listVar: {listVar}')
random.shuffle(listVar)
print(f'shuffle listVar: {listVar}')


# time 모듈
import time

# 시스템 시간
lt = time.localtime()
print(f'time.localtime(): {lt}')

print(f'lt.tm_year: {lt.tm_year}')
print(f'lt.tm_mon: {lt.tm_mon}')
print(f'lt.tm_mday: {lt.tm_mday}')
print(f'lt.tm_hour: {lt.tm_hour}')
print(f'lt.tm_min: {lt.tm_min}')
print(f'lt.tm_sec: {lt.tm_sec}')
print(f'lt.tm_wday: {lt.tm_wday}')

