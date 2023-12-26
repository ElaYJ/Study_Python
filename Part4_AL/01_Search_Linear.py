'''
 # [선형탐색] 선형으로 나열되어 있는 데이터를 순차적으로 스캔하면서 원하는 값을 찾는다.
'''

datas = [3, 2, 5, 7, 9, 1, 0, 8, 6, 4]
print(f'datas: {datas}')
print(f'datas length: {len(datas)}')

searchData = int(input('찾으려는 숫자 입력: '))
searchResultIdx = -1 # 존재하지 않은 인덱스로 초기화

n = 0
while True:

    # 마지막 인덱스 다음칸까지 갔으므로
    # 검색 결과 원하는 숫자가 없다.
    if n == len(datas):
        searchResultIdx = -1
        break

    elif datas[n] == searchData:
        searchResultIdx = n
        break

    n += 1

print(f'searchResultIdx: [{searchResultIdx}]')
print(f'찾으려는 숫자는 {searchResultIdx + 1}번째 데이터이다.')

# 보초법
# 마지막 인덱스에 찾으려는 값을 추가해서 찾는 과정을 간략화한다.

datas = [3, 2, 5, 7, 9, 1, 0, 8, 6, 4]
print(f'datas: {datas}')
print(f'datas length: {len(datas)}')

searchData = int(input('찾으려는 숫자 입력: '))
searchResultIdx = -1

# 마지막 인덱스에 내가 찾으려는 값을 추가한 후 검색
datas.append(searchData) # => sentinel

# 내가 찾으려는 숫자가 마지막(sentinel)까지 갔다는 것은 검색에 실패했다는 의미
# 마지막(sentinel)까지 가기 전, 검색 리스트 안에 있어야 검색 성공이다.
n = 0
while True:

    # if n == len(datas):
    #     searchResultIdx = -1
    #     break

    if datas[n] == searchData:
        if n != len(datas) - 1:
            searchResultIdx = n
        break

    n += 1

print(f'searchResultIdx: [{searchResultIdx}]')
print(f'찾으려는 숫자는 {searchResultIdx + 1}번째 데이터이다.')
print()


# <Q> -------------------------------------------------------------------
# 리스트에서 가장 앞에 있는 숫자 '7'을 검색하고 위치(인덱스)를 출력

nums = [4, 7, 10, 2, 4, 7, 0, 2, 7, 3, 9]
print(f'nums: {nums}, nums length: {len(nums)}')

searchData = int(input('찾으려는 숫자 입력: '))
searchResultIdx = -1

nums.append(searchData)

n = 0
while True:

    if nums[n] == searchData:
        if n != len(nums) - 1:
            searchResultIdx = n
        break

    n += 1

print(f'nums: {nums}, nums length: {len(nums)}')
print(f'searchResultIdx: [{searchResultIdx}]')

if searchResultIdx < 0:
    print(f'찾으려는 {searchData}가(이) 없습니다.')
else:
    print(f'찾으려는 {searchData}의 위치(인덱스)는 {searchResultIdx}입니다.')
print()


# <Q> -------------------------------------------------------------------
# 리스트에서 숫자 '7'을 모두 검색하고 각각의 위치(인덱스)와 검색 개수를 출력

nums = [4, 7, 10, 2, 4, 7, 0, 2, 7, 3, 9]
print(f'nums: {nums}, nums length: {len(nums)}')

searchData = int(input('찾으려는 숫자 입력: '))
searchResultIdxs = []

nums.append(searchData)

# 함수화하기
n = 0
while True:

    if nums[n] == searchData:
        if n != len(nums) - 1:
            searchResultIdxs.append(n)
        else:
            break

    n += 1

print(f'nums: {nums}, nums length: {len(nums)}')
print(f'searchResultIdxs: {searchResultIdxs}')
print(f'searchResultCnts: {len(searchResultIdxs)}')
print()


# <Q> My Code --------------------------------------------------------------

nums = [4, 7, 10, 2, 4, 7, 0, 2, 7, 3, 9]
print(f'nums: {nums}, nums length: {len(nums)}')

searchData = int(input('찾으려는 숫자 입력: '))
searchResultIdx = -1
searchResultIdxs = []

nums.append(searchData)

# Q1. 리스트에서 가장 앞에 있는 숫자 '7'을 검색하고 위치(인덱스)를 출력
n = 0
while True:
    if nums[n] == searchData:
        if n != len(nums) - 1:
            searchResultIdx = n
        break

    n += 1

print(f'nums: {nums}, nums length: {len(nums)}')

if searchResultIdx < 0:
    print(f'찾으려는 {searchData}가(이) 없습니다.')
else:
    print(f'찾으려는 {searchData}의 위치(인덱스)는 {searchResultIdx}입니다.')
print()


# Q2. 리스트에서 숫자 '7'을 모두 검색하고 각각의 위치(인덱스)와 검색 개수를 출력
n = 0
while True:
    if nums[n] == searchData:
        if n != len(nums) - 1:
            searchResultIdxs.append(n)
        else:
            break

    n += 1

print(f'nums: {nums}, nums length: {len(nums)}')

print(f'searchResultIdxs: {searchResultIdxs}')
print(f'searchResultCnts: {len(searchResultIdxs)}')
print()


# <EX> -----------------------------------------------------------------
# 숫자로 이루어진 리스트에서 사용자가 입력한 숫자를 검색하는 모듈을 다음 요건에 따라 만들기
# 1. 검색 모듈은 선형 검색 알고리즘을 이용한다.
# 2. 리스트는 1부터 20까지의 정수 중에서 난수 10개를 이용한다.
# 3. 검색 과정을 로그로 출력한다.
# 4. 검색에 성공하면 해당 정수의 인덱스를 출력하고, 검색 결과가 없으면 -1을 출력한다.

import module_srch_linear as lnr
import random

if __name__ == '__main__':

    rNums = random.sample(range(1, 21), 10)
    searchNum = int(input('input search number: '))

    resultIdx = lnr.searchNumberByLineAlgorithm(rNums, searchNum)

    if resultIdx == -1:
        print('No resutls found')
        print(f'search result index: {resultIdx}')
    else:
        print('>>> Search Results <<<')
        print(f'search result index: {resultIdx}')
        print(f'search result number: {rNums[resultIdx]}')

    print()


    input_num = 7

    l_nums = [3, 2, 5, 7, 9, 1, 0, 8, 6, 4]
    t_nums = (4, 7, 10, 2, 4, 7, 0, 2, 7, 3, 9)
    r_nums = random.sample(range(1, 21), 10)

    total_data = [l_nums, t_nums, r_nums]


    # linearSearch()
    for data in total_data:
        print(f'data: {data}, data_length: {len(data)}')

        result = lnr.linearSearch(data, input_num)

        if len(result) < 1:
            print(f'{input_num} 데이터를 찾을 수 없습니다.')
        else:
            print(f'찾는 {input_num} 데이터의 위치(인덱스)는 {result}입니다.')
        print()

    print(f' l_nums: {l_nums}\n t_nums: {t_nums}\n r_nums: {r_nums}\n')


    # sequencialSearch()
    for data in total_data:
        print(f'data: {data}, data_id: {id(data)}')

        result = lnr.sequencialSearch(data, input_num)

        if result == -1:
            print(f'{input_num} 데이터를 찾을 수 없습니다.')
        else:
            print(f'찾는 {input_num} 데이터의 최초 위치(인덱스)는 [{result}]입니다.')
        print()

    print(f' l_nums: {l_nums}\n t_nums: {t_nums}\n r_nums: {r_nums}\n')




'''
 # [선형탐색]
'''

datas = [3, 2, 5, 7, 9, 1, 0, 8, 6, 4]
print(f'datas: {datas}')
print(f'datas length: {len(datas)}')

searchData = int(input('찾으려는 숫자 입력: '))
searchResultIdx = -1 # 존재하지 않은 인덱스로 초기화

n = 0
while True:

    # 마지막 인덱스 다음칸까지 갔으므로
    # 검색 결과 원하는 숫자가 없다.
    if n == len(datas):
        searchResultIdx = -1
        break

    elif datas[n] == searchData:
        searchResultIdx = n
        break

    n += 1

print(f'searchResultIdx: [{searchResultIdx}]')
print(f'찾으려는 숫자는 {searchResultIdx + 1}번째 데이터이다.')

# 보초법
# 마지막 인덱스에 찾으려는 값을 추가해서 찾는 과정을 간략화한다.

datas = [3, 2, 5, 7, 9, 1, 0, 8, 6, 4]
print(f'datas: {datas}')
print(f'datas length: {len(datas)}')

searchData = int(input('찾으려는 숫자 입력: '))
searchResultIdx = -1

# 마지막 인덱스에 내가 찾으려는 값을 추가한 후 검색
datas.append(searchData) # => sentinel

# 내가 찾으려는 숫자가 마지막(sentinel)까지 갔다는 것은 검색에 실패했다는 의미
# 마지막(sentinel)까지 가기 전, 검색 리스트 안에 있어야 검색 성공이다.
n = 0
while True:

    # if n == len(datas):
    #     searchResultIdx = -1
    #     break

    if datas[n] == searchData:
        if n != len(datas) - 1:
            searchResultIdx = n
        break

    n += 1

print(f'searchResultIdx: [{searchResultIdx}]')
print(f'찾으려는 숫자는 {searchResultIdx + 1}번째 데이터이다.')
print()


# <Q> -------------------------------------------------------------------
# 리스트에서 가장 앞에 있는 숫자 '7'을 검색하고 위치(인덱스)를 출력

nums = [4, 7, 10, 2, 4, 7, 0, 2, 7, 3, 9]
print(f'nums: {nums}, nums length: {len(nums)}')

searchData = int(input('찾으려는 숫자 입력: '))
searchResultIdx = -1

nums.append(searchData)

n = 0
while True:

    if nums[n] == searchData:
        if n != len(nums) - 1:
            searchResultIdx = n
        break

    n += 1

print(f'nums: {nums}, nums length: {len(nums)}')
print(f'searchResultIdx: [{searchResultIdx}]')

if searchResultIdx < 0:
    print(f'찾으려는 {searchData}가(이) 없습니다.')
else:
    print(f'찾으려는 {searchData}의 위치(인덱스)는 {searchResultIdx}입니다.')
print()


# <Q> -------------------------------------------------------------------
# 리스트에서 숫자 '7'을 모두 검색하고 각각의 위치(인덱스)와 검색 개수를 출력

nums = [4, 7, 10, 2, 4, 7, 0, 2, 7, 3, 9]
print(f'nums: {nums}, nums length: {len(nums)}')

searchData = int(input('찾으려는 숫자 입력: '))
searchResultIdxs = []

nums.append(searchData)

# 함수화하기
n = 0
while True:

    if nums[n] == searchData:
        if n != len(nums) - 1:
            searchResultIdxs.append(n)
        else:
            break

    n += 1

print(f'nums: {nums}, nums length: {len(nums)}')
print(f'searchResultIdxs: {searchResultIdxs}')
print(f'searchResultCnts: {len(searchResultIdxs)}')
print()


# <Q> My Code --------------------------------------------------------------

nums = [4, 7, 10, 2, 4, 7, 0, 2, 7, 3, 9]
print(f'nums: {nums}, nums length: {len(nums)}')

searchData = int(input('찾으려는 숫자 입력: '))
searchResultIdx = -1
searchResultIdxs = []

nums.append(searchData)

# Q1. 리스트에서 가장 앞에 있는 숫자 '7'을 검색하고 위치(인덱스)를 출력
n = 0
while True:
    if nums[n] == searchData:
        if n != len(nums) - 1:
            searchResultIdx = n
        break

    n += 1

print(f'nums: {nums}, nums length: {len(nums)}')

if searchResultIdx < 0:
    print(f'찾으려는 {searchData}가(이) 없습니다.')
else:
    print(f'찾으려는 {searchData}의 위치(인덱스)는 {searchResultIdx}입니다.')
print()


# Q2. 리스트에서 숫자 '7'을 모두 검색하고 각각의 위치(인덱스)와 검색 개수를 출력
n = 0
while True:
    if nums[n] == searchData:
        if n != len(nums) - 1:
            searchResultIdxs.append(n)
        else:
            break

    n += 1

print(f'nums: {nums}, nums length: {len(nums)}')

print(f'searchResultIdxs: {searchResultIdxs}')
print(f'searchResultCnts: {len(searchResultIdxs)}')
print()


# <EX> -----------------------------------------------------------------
# 숫자로 이루어진 리스트에서 사용자가 입력한 숫자를 검색하는 모듈을 다음 요건에 따라 만들기
# 1. 검색 모듈은 선형 검색 알고리즘을 이용한다.
# 2. 리스트는 1부터 20까지의 정수 중에서 난수 10개를 이용한다.
# 3. 검색 과정을 로그로 출력한다.
# 4. 검색에 성공하면 해당 정수의 인덱스를 출력하고, 검색 결과가 없으면 -1을 출력한다.

import module_srch_linear as lnr
import random

if __name__ == '__main__':

    rNums = random.sample(range(1, 21), 10)
    searchNum = int(input('input search number: '))

    resultIdx = lnr.searchNumberByLineAlgorithm(rNums, searchNum)

    if resultIdx == -1:
        print('No resutls found')
        print(f'search result index: {resultIdx}')
    else:
        print('>>> Search Results <<<')
        print(f'search result index: {resultIdx}')
        print(f'search result number: {rNums[resultIdx]}')

    print()


    input_num = 7

    l_nums = [3, 2, 5, 7, 9, 1, 0, 8, 6, 4]
    t_nums = (4, 7, 10, 2, 4, 7, 0, 2, 7, 3, 9)
    r_nums = random.sample(range(1, 21), 10)

    total_data = [l_nums, t_nums, r_nums]


    # linearSearch()
    for data in total_data:
        print(f'data: {data}, data_length: {len(data)}')

        result = lnr.linearSearch(data, input_num)

        if len(result) < 1:
            print(f'{input_num} 데이터를 찾을 수 없습니다.')
        else:
            print(f'찾는 {input_num} 데이터의 위치(인덱스)는 {result}입니다.')
        print()

    print(f' l_nums: {l_nums}\n t_nums: {t_nums}\n r_nums: {r_nums}\n')


    # sequencialSearch()
    for data in total_data:
        print(f'data: {data}, data_id: {id(data)}')

        result = lnr.sequencialSearch(data, input_num)

        if result == -1:
            print(f'{input_num} 데이터를 찾을 수 없습니다.')
        else:
            print(f'찾는 {input_num} 데이터의 최초 위치(인덱스)는 [{result}]입니다.')
        print()

    print(f' l_nums: {l_nums}\n t_nums: {t_nums}\n r_nums: {r_nums}\n')
