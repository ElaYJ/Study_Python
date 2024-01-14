# 주소록입니다. 이후 강의에서 모두 이 search_target을 사용합니다.
search_target = '''Luke Skywarker 02-123-4567 luke@daum.net
다스베이더 070-9999-9999 darth_vader@gmail.com
princess leia 010 2454 3457 leia@gmail.com'''

# 정규표현식과 일치하는 부분을 모두 찾아주는 파이썬 코드입니다.
import re
regex1 = r'0\d{1,2}[ -]?\d{3,4}[ -]?\d{3,4}'
result1 = re.findall(regex1, search_target)
print("\n".join(result1))

regex2 = r'\d+'
result2 = re.findall(regex2, search_target)
print(result2)

regex3 = r'[aeiou]'
result3 = re.findall(regex3, search_target)
print(result3)

regex4 = r'[a-z]+'
result4 = re.findall(regex4, search_target)
print(result4)

regex5 = r'[가-힣]+'
result5 = re.findall(regex5, search_target)
print(result5)


# 정규표현식 패턴 생성
pattern = re.compile(r'(\d{3}-\d{2}-\d{4})')

# 문자열에서 패턴 검색
text = "주민등록번호는 123-45-6789입니다."
match = pattern.search(text)
print(type(match))

if match:
    print("주민등록번호를 찾았습니다:", match.group())
else:
    print("주민등록번호를 찾지 못했습니다.")


