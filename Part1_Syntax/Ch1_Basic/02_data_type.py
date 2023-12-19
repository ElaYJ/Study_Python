'''
# [자료형]
    ▶ 정수형(int) - phthon은 메모리가 허용하는 범위에서 무한정수 사용 가능하다.
    ▶ 실수형(float) - 대략 소수점 이하 17~18번 째에서 데이터 솔실이 일어난다.
    ▶ 문자형(char), 문자열(String) - 숫자도 따옴표로 묶으면 문자(열)로 인식한다.
    ▶ 논리형(bool) - True / False
'''

score = 100
pi = 3.14
wantGo = '캐나다'
isAdult = True

print("시험 성적({})".format(score))
print(type(score))
print("원주율({})".format(pi))
print(type(pi))
print("여행 가고픈 나라({})".format(wantGo))
print(type(wantGo))
print("성인 구분({})".format(isAdult))
print(type(True))
print()

# isinstance() 함수 : 한 가지 혹은 여러 가지 타입과의 일치 여부를 확인
result1 = isinstance(score, int)
result2 = isinstance(pi, float)
result3 = isinstance("hi", str)
result4 = isinstance([1, 2, 3], list)
result5 = isinstance({'name':'mario'}, dict)
result = isinstance(1, (int, float, str))
print(result1, result2, result3, result4, result5, result)


