n_str = input("N = (1~999,999)")

# 숫자로 이루어진 문자열에서 리스트로 변환 ----------------------------
s = "123456"
# Case_1. list() 함수 사용
result = list(s)
# print(result)  # ['1', '2', '3', '4', '5', '6']
# Case_2. list comprehension 사용
result = [char for char in s]
# print(result)  # ['1', '2', '3', '4', '5', '6']
# Case_3. map() 함수 사용
result = list(map(str, s))
# print(result)  # ['1', '2', '3', '4', '5', '6']
#----------------------------------------------------------------

n_list = list(map(int, n_str)) # [int(x) for x in n_str]
print(n_list)

first_n = n_list[0]
print(first_n)

# 리스트 정렬 -------------------------------------------------------------------------
# 1. sort() 메소드 --> sort() 메소드는 리스트 자체를 정렬하여 리스트를 변경하며, 반환값은 None
lst = [4, 2, 6, 1, 3, 5]
lst.sort()
# print(lst)  # [1, 2, 3, 4, 5, 6]
lst.sort(reverse=True)
# print(lst)  # [6, 5, 4, 3, 2, 1]
# 2. sorted() 함수 --> sorted() 함수는 원래 리스트를 변경하지 않고, 정렬된 새로운 리스트를 반환
lst = [4, 2, 6, 1, 3, 5]
sorted_lst = sorted(lst)
# print(sorted_lst)  # [1, 2, 3, 4, 5, 6]
# print(lst)  # [4, 2, 6, 1, 3, 5]  # 원래 리스트는 변경되지 않음
sorted_lst = sorted(lst, reverse=True)
# print(sorted_lst)  # [6, 5, 4, 3, 2, 1]
#------------------------------------------------------------------------------------
print(lst)
print(set(lst))

n_list.sort()
print(n_list)

first_idx = n_list.index(first_n)
next_n = n_list.pop(first_idx+1)
print(next_n)
print(n_list)

print(str(next_n)+''.join(map(str,n_list)))

# 제출 코드 ==============================================================
n_str = input()
n_list = [int(x) for x in n_str]
n_sort = sorted(n_list)
n_only = list(set(n_sort))
first_n = n_list[0]
result = ''

rlt_idx = n_only.index(first_n) + 1
if rlt_idx == len(n_only):
    for _ in range(n_list.count(first_n)):
        if n_list.index(first_n) == 0:
            result += str(n_list.pop(0))
            n_sort.remove(first_n)
    next_n = n_only[rlt_idx-2]
else:
    next_n = n_only[rlt_idx]
n_sort.remove(next_n)

result += str(next_n) + "".join(map(str, n_sort))
print(result)
# 60점 ==================================================================

# 정답 코드
s = list(input())

for i in range(len(s)-2, -1, -1):
    if s[i] < s[i+1]:
        break
else:
    print(0)
    exit()

for j in range(len(s)-1, i, -1):
    if s[j] > s[i]:
        break

s[i], s[j] = s[j], s[i]
s[i+1:] = s[:i:-1]
print("".join(s))

# ChatGPT
def next_greater_number_with_same_digits(n):
    digits = list(str(n))
    length = len(digits)

    # Step 1: Find the first decreasing element from the end
    for i in range(length - 2, -1, -1):
        if digits[i] < digits[i + 1]:
            break
    else:
        # If no such element is found, the digits are in descending order
        return -1

    # Step 2: Find the smallest element greater than digits[i] from the end
    for j in range(length - 1, i, -1):
        if digits[j] > digits[i]:
            # Step 3: Swap them
            digits[i], digits[j] = digits[j], digits[i]
            break

    # Step 4: Reverse the digits after the position i
    digits = digits[:i + 1] + sorted(digits[i + 1:])

    return int("".join(digits))

# 테스트 케이스
print(next_greater_number_with_same_digits(67))  # 출력: 76
print(next_greater_number_with_same_digits(1234))  # 출력: 1243
print(next_greater_number_with_same_digits(4321))  # 출력: -1 (없음)
print(next_greater_number_with_same_digits(534976))  # 출력: 536479
