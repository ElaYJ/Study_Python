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

# print(f'staIdx: {staIdx}, endIdx: {endIdx}')
# print(f'midIdx: {midIdx}, midVal: {midVal}')
print(f'0> staIdx: {staIdx},  midIdx: {midIdx}({midVal}),  endIdx: {endIdx}')


# 찾으려는 데이터가 자료 범위를 벗어나면 while문을 돌 필요가 없다.
while searchData >= datas[0] and searchData <= datas[len(datas)-1]:

    if searchData == datas[len(datas)-1]:
        print(f'1> staIdx: {staIdx},  midIdx: {midIdx}({midVal}),  endIdx: {endIdx}')
        searchResultIdx = len(datas)-1
        break

    if searchData > midVal:
        staIdx = midIdx
        midIdx = (staIdx +  endIdx) // 2
        midVal = datas[midIdx]
        print(f'3>+staIdx: {staIdx}, +midIdx: {midIdx}({midVal}),  endIdx: {endIdx}')

    elif searchData < midVal:
        endIdx = midIdx
        midIdx = (staIdx + endIdx) // 2
        midVal = datas[midIdx]
        print(f'4> staIdx: {staIdx}, -midIdx: {midIdx}({midVal}), -endIdx: {endIdx}')

    elif searchData == midVal:
        print(f'5> midVal({midVal}) == srchVal({searchData})')
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

print(f'0> staIdx: {staIdx},  midIdx: {midIdx}({midVal}),  endIdx: {endIdx}')

'''
nums: [0, 4, 5, 7, 9, 10, 11, 17, 22, 61, 88]에서 찾는 수가 다음
{(0, 4), 6, 8, (12, 16), (18, 21), (23, 60), (62, 87)} 범위 내에 있다면
무한루프에 빠지게 된다.
만약 '8'을 검색하게 되면...
 8 > mid_val(7)로 start_idx = mid_idx 해야하는데 둘 다 3으로 같은 값이므로 변화가 없고, 
 mid_idx에 {(start + end) // 2 = 3} 값을 대입하므로 mid_idx 값eh 변하지 않는다.
 결국 오른쪽으로 이동해야 할 start_idx값과 mid_idx값이 변하지 않아 무한루프에 빠지게 된다.
+staIdx: 3, +midIdx: 3, endIdx: 4
midVal: 7
+staIdx: 3, +midIdx: 3, endIdx: 4
midVal: 7
+staIdx: 3, +midIdx: 3, endIdx: 4
midVal: 7
+staIdx: 3, +midIdx: 3, endIdx: 4
midVal: 7
+staIdx: 3, +midIdx: 3, endIdx: 4
midVal: 7
.................무한반복
만약 '62'를 검색하면, 62 > mid_val(61)
+staIdx: 9, +midIdx: 9, endIdx: 10
midVal: 61
+staIdx: 9, +midIdx: 9, endIdx: 10
midVal: 61
+staIdx: 9, +midIdx: 9, endIdx: 10
midVal: 61
+staIdx: 9, +midIdx: 9, endIdx: 10
midVal: 61
+staIdx: 9, +midIdx: 9, endIdx: 10

'''
# 찾으려는 값이 4보다 작거나 88보다 크면 검색할 의미가 없다.
# while문을 pass하고 '-1'을 출력하게 된다.
while searchData <= nums[len(nums)-1] and searchData >= nums[0]:

    if searchData == nums[len(nums)-1]:
        print(f'1> staIdx: {staIdx},  midIdx: {midIdx}({midVal}),  endIdx: {endIdx}')
        searchResultIdx = len(nums)-1
        break

    # 2진으로 나눠가다 start_idx와 end_idx가 나란히 존해했을 때
    # 찾는 값이 없으면 무한 루프에 빠지게 된다.
    if staIdx + 1 == endIdx:
        print(f'2> staIdx: {staIdx},  midIdx: {midIdx}({midVal}),  endIdx: {endIdx}')
        if nums[staIdx] != searchData and nums[endIdx] != searchData: break

    if searchData > midVal:
        staIdx = midIdx
        midIdx = (staIdx +  endIdx) // 2
        midVal = nums[midIdx]
        print(f'3>+staIdx: {staIdx}, +midIdx: {midIdx}({midVal}),  endIdx: {endIdx}')

    elif searchData < midVal:
        endIdx = midIdx
        midIdx = (staIdx + endIdx) // 2
        midVal = nums[midIdx]
        print(f'4> staIdx: {staIdx}, -midIdx: {midIdx}({midVal}), -endIdx: {endIdx}')

    elif searchData == midVal:
        print(f'5> midVal({midVal}) == srchVal({searchData})')
        searchResultIdx = midIdx
        break

print(f'searchResultIdx: [{searchResultIdx}]')



# <EX> ---------------------------------------------------------------------
# 숫자로 이루어진 리스트에서 사용자가 입력한 숫자를 검색하는 모듈을 다음 요건에 따라 만들기
# 1. 검색 모듈은 이진 검색 알고리즘을 이용한다.
# 2. 리스트는 [1,2,4,6,7,8,10,11,13,15,16,17,20,21,23,24,27,28]을 이용한다.
# 3. 검색 과정을 로그로 출력한다.
# 4. 검색에 성공하면 해당 정수의 인덱스를 출력하고, 검색 결과가 없으면 -1을 출력한다.

import module_binary_srch as bins
#import random

if __name__ == '__main__':

    nums = [1, 2, 4, 6, 7, 8, 10, 11, 13, 15, 16, 17, 20, 21, 23, 24, 27, 28]
    print(f'nums: {nums}')

    searchNum = int(input('input search number: '))

    resultIdx = bins.searchNumberByBinaryAlgorithm(nums, searchNum)

    if resultIdx == -1:
        print('No results found.')
        print(f'search result index: {resultIdx}')

    else:
        print('>>> Search Results <<<')
        print(f'search result index: {resultIdx}')
        print(f'search result number: {nums[resultIdx]}')


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

# print(f'staIdx: {staIdx}, endIdx: {endIdx}')
# print(f'midIdx: {midIdx}, midVal: {midVal}')
print(f'0> staIdx: {staIdx},  midIdx: {midIdx}({midVal}),  endIdx: {endIdx}')


# 찾으려는 데이터가 자료 범위를 벗어나면 while문을 돌 필요가 없다.
while searchData >= datas[0] and searchData <= datas[len(datas)-1]:

    if searchData == datas[len(datas)-1]:
        print(f'1> staIdx: {staIdx},  midIdx: {midIdx}({midVal}),  endIdx: {endIdx}')
        searchResultIdx = len(datas)-1
        break

    if searchData > midVal:
        staIdx = midIdx
        midIdx = (staIdx +  endIdx) // 2
        midVal = datas[midIdx]
        print(f'3>+staIdx: {staIdx}, +midIdx: {midIdx}({midVal}),  endIdx: {endIdx}')

    elif searchData < midVal:
        endIdx = midIdx
        midIdx = (staIdx + endIdx) // 2
        midVal = datas[midIdx]
        print(f'4> staIdx: {staIdx}, -midIdx: {midIdx}({midVal}), -endIdx: {endIdx}')

    elif searchData == midVal:
        print(f'5> midVal({midVal}) == srchVal({searchData})')
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

print(f'0> staIdx: {staIdx},  midIdx: {midIdx}({midVal}),  endIdx: {endIdx}')

'''
nums: [0, 4, 5, 7, 9, 10, 11, 17, 22, 61, 88]에서 찾는 수가 다음
{(0, 4), 6, 8, (12, 16), (18, 21), (23, 60), (62, 87)} 범위 내에 있다면
무한루프에 빠지게 된다.
만약 '8'을 검색하게 되면...
 8 > mid_val(7)로 start_idx = mid_idx 해야하는데 둘 다 3으로 같은 값이므로 변화가 없고, 
 mid_idx에 {(start + end) // 2 = 3} 값을 대입하므로 mid_idx 값eh 변하지 않는다.
 결국 오른쪽으로 이동해야 할 start_idx값과 mid_idx값이 변하지 않아 무한루프에 빠지게 된다.
+staIdx: 3, +midIdx: 3, endIdx: 4
midVal: 7
+staIdx: 3, +midIdx: 3, endIdx: 4
midVal: 7
+staIdx: 3, +midIdx: 3, endIdx: 4
midVal: 7
+staIdx: 3, +midIdx: 3, endIdx: 4
midVal: 7
+staIdx: 3, +midIdx: 3, endIdx: 4
midVal: 7
.................무한반복
만약 '62'를 검색하면, 62 > mid_val(61)
+staIdx: 9, +midIdx: 9, endIdx: 10
midVal: 61
+staIdx: 9, +midIdx: 9, endIdx: 10
midVal: 61
+staIdx: 9, +midIdx: 9, endIdx: 10
midVal: 61
+staIdx: 9, +midIdx: 9, endIdx: 10
midVal: 61
+staIdx: 9, +midIdx: 9, endIdx: 10

'''
# 찾으려는 값이 4보다 작거나 88보다 크면 검색할 의미가 없다.
# while문을 pass하고 '-1'을 출력하게 된다.
while searchData <= nums[len(nums)-1] and searchData >= nums[0]:

    if searchData == nums[len(nums)-1]:
        print(f'1> staIdx: {staIdx},  midIdx: {midIdx}({midVal}),  endIdx: {endIdx}')
        searchResultIdx = len(nums)-1
        break

    # 2진으로 나눠가다 start_idx와 end_idx가 나란히 존해했을 때
    # 찾는 값이 없으면 무한 루프에 빠지게 된다.
    if staIdx + 1 == endIdx:
        print(f'2> staIdx: {staIdx},  midIdx: {midIdx}({midVal}),  endIdx: {endIdx}')
        if nums[staIdx] != searchData and nums[endIdx] != searchData: break

    if searchData > midVal:
        staIdx = midIdx
        midIdx = (staIdx +  endIdx) // 2
        midVal = nums[midIdx]
        print(f'3>+staIdx: {staIdx}, +midIdx: {midIdx}({midVal}),  endIdx: {endIdx}')

    elif searchData < midVal:
        endIdx = midIdx
        midIdx = (staIdx + endIdx) // 2
        midVal = nums[midIdx]
        print(f'4> staIdx: {staIdx}, -midIdx: {midIdx}({midVal}), -endIdx: {endIdx}')

    elif searchData == midVal:
        print(f'5> midVal({midVal}) == srchVal({searchData})')
        searchResultIdx = midIdx
        break

print(f'searchResultIdx: [{searchResultIdx}]')



# <EX> ---------------------------------------------------------------------
# 숫자로 이루어진 리스트에서 사용자가 입력한 숫자를 검색하는 모듈을 다음 요건에 따라 만들기
# 1. 검색 모듈은 이진 검색 알고리즘을 이용한다.
# 2. 리스트는 [1,2,4,6,7,8,10,11,13,15,16,17,20,21,23,24,27,28]을 이용한다.
# 3. 검색 과정을 로그로 출력한다.
# 4. 검색에 성공하면 해당 정수의 인덱스를 출력하고, 검색 결과가 없으면 -1을 출력한다.

import module_binary_srch as bins
import random

if __name__ == '__main__':

    nums = [1, 2, 4, 6, 7, 8, 10, 11, 13, 15, 16, 17, 20, 21, 23, 24, 27, 28]
    print(f'nums: {nums}')

    searchNum = random.randint(1, 28)

    resultIdx = bins.searchNumberByBinaryAlgorithm(nums, searchNum)

    if resultIdx == -1:
        print('No results found.')
        print(f'search result index: {resultIdx}')

    else:
        print('>>> Search Results <<<')
        print(f'search result index: {resultIdx}')
        print(f'search result number: {nums[resultIdx]}')
