n, m = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))
result = []

for _ in range(m):
    i, j, k = map(int, input().split(" "))
    arr_sort = sorted(arr[i - 1:j])
    result.append(arr_sort[k - 1])

for i in range(m):
    print(result[i])
