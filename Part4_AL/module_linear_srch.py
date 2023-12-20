# <EX> ---------------------------------------------------------------------
# 숫자로 이루어진 리스트에서 사용자가 입력한 숫자를 검색하는 모듈을 다음 요건에 따라 만들기
# 1. 검색 모듈은 선형 검색 알고리즘을 이용한다.
# 2. 리스트는 1부터 20까지의 정수 중에서 난수 10개를 이용한다.
# 3. 검색 과정을 로그로 출력한다.
# 4. 검색에 성공하면 해당 정수의 인덱스를 출력하고, 검색 결과가 없으면 -1을 출력한다.

def searchNumberByLineAlgorithm(ns, sn):

    searchResultIdx = -1

    print(f'Numbers: {ns}')
    print(f'Search Numbers: {sn}')

    n = 0
    while True:

        if n == len(ns):
            print('Search FAIL!!')
            break

        if ns[n] == sn:
            searchResultIdx = n
            print('Search SUCCESS!!')
            print(f'Search result INDEX: {searchResultIdx}')
            break

        n += 1

    return searchResultIdx


# <MyCode> -------------------------------------------------------------------
# 함수화 하기

from copy import deepcopy


# 가변객체(list, dict, set)의 복사는 디폴트: 얕은 복사!!
# 가변 객체를 복사하는 방법은 생성자,[:], .copy()함수를 사용하는 것이다. 모두다 얕은 복사이다.
def linearSearch(nums, search_num):
    sentinel_idx = len(nums)
    search_idxes = []

    copied_nums = deepcopy(nums)
    # add sentinel: +연산자는 nums가 List든 Tuple이든 상관없이 끝에 이어붙인다.
    copied_nums += (search_num,)
    print(copied_nums, type(copied_nums))

    i = 0
    while True:
        if copied_nums[i] == search_num:
            if i == sentinel_idx:
                break

            search_idxes.append(i)

        i += 1

    return search_idxes

'''
data: [3, 2, 5, 7, 9, 1, 0, 8, 6, 4], data_length: 10
[3, 2, 5, 7, 9, 1, 0, 8, 6, 4, 7] <class 'list'>
찾는 7 데이터의 위치(인덱스)는 [3]입니다.

data: (4, 7, 10, 2, 4, 7, 0, 2, 7, 3, 9), data_length: 11
(4, 7, 10, 2, 4, 7, 0, 2, 7, 3, 9, 7) <class 'tuple'>
찾는 7 데이터의 위치(인덱스)는 [1, 5, 8]입니다.

data: [15, 11, 3, 9, 19, 18, 1, 17, 5, 10], data_length: 10
[15, 11, 3, 9, 19, 18, 1, 17, 5, 10, 7] <class 'list'>
7 데이터를 찾을 수 없습니다.

 l_nums: [3, 2, 5, 7, 9, 1, 0, 8, 6, 4, 7]
 t_nums: (4, 7, 10, 2, 4, 7, 0, 2, 7, 3, 9)
 r_nums: [15, 11, 3, 9, 19, 18, 1, 17, 5, 10, 7]


data: [3, 2, 5, 7, 9, 1, 0, 8, 6, 4, 7], data_length: 11
찾는 7 데이터의 최초 위치(인덱스)는 [3]입니다.

data: (4, 7, 10, 2, 4, 7, 0, 2, 7, 3, 9), data_length: 11
찾는 7 데이터의 최초 위치(인덱스)는 [1]입니다.

data: [15, 11, 3, 9, 19, 18, 1, 17, 5, 10, 7], data_length: 11
찾는 7 데이터의 최초 위치(인덱스)는 [10]입니다.

 l_nums: [3, 2, 5, 7, 9, 1, 0, 8, 6, 4, 7, 7]
 t_nums: (4, 7, 10, 2, 4, 7, 0, 2, 7, 3, 9)
 r_nums: [15, 11, 3, 9, 19, 18, 1, 17, 5, 10, 7, 7]
'''

# 함수를 한 번 실행하고 나니 리스트 가변 객체가 함수로 얕은 복사가 되어 sentinel 값이 붙어
# 다음 함수를 실행했을 때 sentinel 값이 붙은 변한 자료형으로 검색을 하게 되었다.
# 튜플은 가변형 객체가 아니여서 그런지 데이터가 변하지 않았다.
# 깊은 복사 대신 tuple로 Casting해서 새 변수로 받아도 깊은 복사가 이루어진다.


# 중복되는 데이터가 있는 경우 최초의 데이터 인덱스만 반환한다.
def sequencialSearch(data, key):
    sentinel_idx = len(data)

    # copied_data = deepcopy(data)
    local_data = tuple(data)
    local_data += (key,)
    print(f'temp_id: {id(local_data)}, data_id: {id(data)}')

    search_idx = 0
    while True:
        if local_data[search_idx] == key:
            break

        search_idx += 1

    return (-1 if search_idx == sentinel_idx else search_idx)

'''
data: [3, 2, 5, 7, 9, 1, 0, 8, 6, 4], data_length: 10
(3, 2, 5, 7, 9, 1, 0, 8, 6, 4, 7) <class 'tuple'>
찾는 7 데이터의 위치(인덱스)는 [3]입니다.

data: (4, 7, 10, 2, 4, 7, 0, 2, 7, 3, 9), data_length: 11
(4, 7, 10, 2, 4, 7, 0, 2, 7, 3, 9, 7) <class 'tuple'>
찾는 7 데이터의 위치(인덱스)는 [1, 5, 8]입니다.

data: [15, 14, 6, 12, 4, 20, 17, 5, 19, 13], data_length: 10
(15, 14, 6, 12, 4, 20, 17, 5, 19, 13, 7) <class 'tuple'>
7 데이터를 찾을 수 없습니다.

 l_nums: [3, 2, 5, 7, 9, 1, 0, 8, 6, 4]
 t_nums: (4, 7, 10, 2, 4, 7, 0, 2, 7, 3, 9)
 r_nums: [15, 14, 6, 12, 4, 20, 17, 5, 19, 13]

data: [3, 2, 5, 7, 9, 1, 0, 8, 6, 4], data_id: 1937617703168
temp_id: 1937619155008, data_id1937617703168
찾는 7 데이터의 최초 위치(인덱스)는 [3]입니다.

data: (4, 7, 10, 2, 4, 7, 0, 2, 7, 3, 9), data_id: 1937619144000
temp_id: 1937617348368, data_id1937619144000
찾는 7 데이터의 최초 위치(인덱스)는 [1]입니다.

data: [15, 14, 6, 12, 4, 20, 17, 5, 19, 13], data_id: 1937619553792
temp_id: 1937619155008, data_id1937619553792
7 데이터를 찾을 수 없습니다.

 l_nums: [3, 2, 5, 7, 9, 1, 0, 8, 6, 4]
 t_nums: (4, 7, 10, 2, 4, 7, 0, 2, 7, 3, 9)
 r_nums: [15, 14, 6, 12, 4, 20, 17, 5, 19, 13]
'''

