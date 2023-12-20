'''
 # [이진탐색] 핵심은 정렬된 자료구조 내에서 검색이 이루어진다는 것이다.
'''

# idx   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,]
datas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# datas = [1, 3, 4, 6, 7, 8, 9, 11]

print(f'datas: {datas}')
print(f'datas length: {len(datas)}')

searchData = int(input('찾으려는 숫자 입력: '))
searchResultIdx = -1

staIdx = 0
endIdx = len(datas) - 1
midIdx = (staIdx +  endIdx) // 2
midVal = datas[midIdx]
print(f'midIdx: {midIdx}')
print(f'midVal: {midVal}')

# 찾으려는 데이터가 자료 범위를 벗어나면 while문을 돌 필요가 없다.
while searchData >= datas[0] and searchData <= datas[len(datas)-1]:

    if searchData == datas[len(datas)-1]:
        searchResultIdx = len(datas)-1
        break

    if searchData > midVal:
        staIdx = midIdx
        midIdx = (staIdx +  endIdx) // 2
        midVal = datas[midIdx]
        print(f'midIdx: {midIdx}, midVal: {midVal}')

    elif searchData < midVal:
        endIdx = midIdx
        midIdx = (staIdx + endIdx) // 2
        midVal = datas[midIdx]
        print(f'midIdx: {midIdx}, midVal: {midVal}')

    elif searchData == midVal:
        searchResultIdx = midIdx
        break

print(f'searchResultIdx: [{searchResultIdx}]')



# <Q> ---------------------------------------------------------------------------------
# 리스트를 오름차순으로 정렬한 후 '7'을 검색하고 위치(Index)를 출력

nums = [4, 10, 22, 5, 0, 17, 7, 11, 9, 61, 88]
print(f'nums: {nums}')

nums.sort()
print(f'nums: {nums}')

searchData = int(input('찾으려는 숫자 입력: '))
searchResultIdx = -1

staIdx = 0
endIdx = len(nums) - 1
midIdx = (staIdx +  endIdx) // 2
midVal = nums[midIdx]

# 찾으려는 값이 4보다 작거나 88보다 크면 검색할 의미가 없다.
# while문을 pass하고 '-1'을 출력하게 된다.
while searchData <= nums[len(nums)-1] and searchData >= nums[0]:

    if searchData == nums[len(nums)-1]:
        searchResultIdx = len(nums)-1
        break

    if searchData > midVal:
        staIdx = midIdx
        midIdx = (staIdx +  endIdx) // 2
        midVal = nums[midIdx]
        print(f'midIdx: {midIdx}')
        print(f'midVal: {midVal}')

    elif searchData < midVal:
        endIdx = midIdx
        midIdx = (staIdx + endIdx) // 2
        midVal = nums[midIdx]
        print(f'midIdx: {midIdx}')
        print(f'midVal: {midVal}')

    elif searchData == midVal:
        searchResultIdx = midIdx
        break

print(f'searchResultIdx: [{searchResultIdx}]')



# <EX> ---------------------------------------------------------------------
# 숫자로 이루어진 리스트에서 사용자가 입력한 숫자를 검색하는 모듈을 다음 요건에 따라 만들기
# 1. 검색 모듈은 이진 검색 알고리즘을 이용한다.
# 2. 리스트는 [1,2,4,6,7,8,10,11,13,15,16,17,20,21,23,24,27,28]을 이용한다.
# 3. 검색 과정을 로그로 출력한다.
# 4. 검색에 성공하면 해당 정수의 인덱스를 출력하고, 검색 결과가 없으면 -1을 출력한다.

import module_binary as bin
import random

if __name__ == '__main__':

    nums = [1, 2, 4, 6, 7, 8, 10, 11, 13, 15, 16, 17, 20, 21, 23, 24, 27, 28]
    searchNum = int(input('input search number: '))

    resultIdx = binaryMod.searchNumberByBinaryAlgorithm(nums, searchNum)
    print(f'nums: {nums}')

    if resultIdx == -1:
        print('No results found.')
        print(f'search result index: {resultIdx}')

    else:
        print('>>> Search Results <<<')
        print(f'search result index: {resultIdx}')
        print(f'search result number: {nums[resultIdx]}')
