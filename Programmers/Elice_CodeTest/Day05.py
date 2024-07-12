def restore_sequence(subsequence_sums):
    # 부분 수열의 합들을 정렬합니다.
    subsequence_sums.sort()

    # 첫 번째 값은 항상 0이므로 제거합니다.
    subsequence_sums = subsequence_sums[1:]

    # 원래 수열을 저장할 리스트입니다.
    original_sequence = []

    # 현재 부분 수열의 합들을 추적할 리스트입니다.
    current_sums = []

    while subsequence_sums:
        # 가장 작은 값을 선택하고, 이를 원래 수열의 원소로 설정합니다.
        smallest = subsequence_sums[0]
        original_sequence.append(smallest)

        # 해당 값을 current_sums에 추가하고, 새로운 합들을 계산합니다.
        new_sums = []
        for s in current_sums:
            new_sums.append(s + smallest)

        # current_sums에 새로운 합들을 추가합니다.
        current_sums.append(smallest)
        current_sums.extend(new_sums)

        # current_sums에서 각각의 값을 subsequence_sums에서 제거합니다.
        remove_sums = [smallest]
        remove_sums.extend(new_sums)
        remove_sums.sort()
        # current_sums = sorted(current_sums)
        # for s in current_sums:
        for s in remove_sums:
            if s in subsequence_sums:
                subsequence_sums.remove(s)

    return original_sequence


# 예제 사용
subsequence_sums = [1, 4, 7, 3, 0, 6, 5, 2]
original_sequence = restore_sequence(subsequence_sums)
print(original_sequence)  # 출력: [1, 2, 3]


# 제출 코드 ===============================================================================
n = int(input())
S_list = list(map(int, input().split(" ")))

S_sort = sorted(S_list)[1:]
result = []

S_current = []
while S_sort:
    an = S_sort[0]
    result.append(an)
    if len(result) == n: break

    new_sums = []
    for e in S_current:
        new_sums.append(e + an)
    S_current.append(an)
    S_current.extend(new_sums)

    S_remove = [an]
    S_remove.extend(new_sums)
    for e in S_remove:
        if e in S_sort:
            S_sort.remove(e)

print(" ".join(map(str, result)))
# 100점 =================================================================================
