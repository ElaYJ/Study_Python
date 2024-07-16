from itertools import combinations

n, k = map(int, input().split())

n_list = []
n_cnt = [0] * 10
for d in str(n):
    n_list.append(int(d))
    n_cnt[int(d)] += 1

digits = list(set(n_list))
possible = [0,1,2,3,4,5,6,7,8,9]
for num in digits:
    possible.remove(num)

def next_greater_number_with_same_digits(n):
    digits = list(str(n))
    length = len(digits)

    for i in range(length-2, -1, -1):
        if digits[i] < digits[i+1]:
            break
    else:
        print(0)

    for j in range(length-1, i, -1):
        if digits[j] > digits[i]:
            digits[i], digits[j] = digits[j], digits[i]
            break
    digits = digits[:i+1] + sorted(digits[i+1:])
    print("".join(digits))

if k == len(digits):
    next_greater_number_with_same_digits(n)
elif k > len(digits):
    new_num = n_list
    for i in range(k - len(digits) -1, -1, -1):
        new_digit = possible[i]
        for j in range(len(n_list)-1, -1, -1):
            if n_cnt[new_num[j]] > 1:
                new_num[j] = new_digit
                break
    comb_results = []
    for comb in combinations(new_num, len(new_num)):
        comb_results.append(int("".join(map(str,comb))))
    comb_results.sort()
    for result in comb_results:
        if result > n:
            print(result)