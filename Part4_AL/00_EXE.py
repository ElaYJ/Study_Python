# datas = [3, 2, 5, 7, 9, 1, 0, 8, 6, 4]
# nums = (4, 7, 10, 2, 4, 7, 0, 2, 7, 3, 9)
#
# result1 = datas + [127,]
# result2 = nums + (127,)
# print(result1)
# print(result2)
#
# datas += (127,)
# nums += (127,)
# print(datas)
# print(result2)

import random
from copy import deepcopy


# 가변객체(list, dict, set)의 복사는 디폴트: 얕은 복사
# 가변 객체를 복사하는 방법은 생성자,[:], .copy()함수를 사용하는 것이다. 모두다 얕은 복사이다.
def linearSearch(nums, search_num):
    sentinel_idx = len(nums)
    search_idxes = []

    # nums += (search_num,)
    # print(nums, type(nums))
    #
    # copied_nums = deepcopy(nums)
    # copied_nums += (search_num,)
    # print(copied_nums, type(copied_nums))

    temp_nums = tuple(nums)
    temp_nums += (search_num,)
    print(temp_nums, type(temp_nums))

    i = 0
    while True:
        if temp_nums[i] == search_num:
            if i == sentinel_idx:
                break

            search_idxes.append(i)

        i += 1

    return search_idxes


input_num = 7
l_nums = [3, 2, 5, 7, 9, 1, 0, 8, 6, 4]
t_nums = (4, 7, 10, 2, 4, 7, 0, 2, 7, 3, 9)
r_nums = random.sample(range(1, 21), 10)

total_data = [l_nums, t_nums, r_nums]
for data in total_data:
    print(f'data: {data}, data_length: {len(data)}')

    result = linearSearch(data, input_num)

    if len(result) < 1:
        print(f'{input_num} 데이터를 찾을 수 없습니다.')
    else:
        print(f'찾는 {input_num} 데이터의 위치(인덱스)는 {result}입니다.')
    print()

print(f' l_nums: {l_nums}\n t_nums: {t_nums}\n r_nums: {r_nums}\n')


def sequencialSearch(data, key):
    sentinel_idx = len(data)

    # copied_data = deepcopy(data)
    temp_data = tuple(data)
    temp_data += (key,)
    print(f'temp_id: {id(temp_data)}, data_id: {id(data)}')

    search_idx = 0
    while True:
        if temp_data[search_idx] == key:
            break

        search_idx += 1

    return (-1 if search_idx == sentinel_idx else search_idx)


for data in total_data:
    print(f'data: {data}, data_id: {id(data)}')

    result = sequencialSearch(data, input_num)

    if result == -1:
        print(f'{input_num} 데이터를 찾을 수 없습니다.')
    else:
        print(f'찾는 {input_num} 데이터의 최초 위치(인덱스)는 [{result}]입니다.')
    print()

print(f' l_nums: {l_nums}\n t_nums: {t_nums}\n r_nums: {r_nums}\n')

