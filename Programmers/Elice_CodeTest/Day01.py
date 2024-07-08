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