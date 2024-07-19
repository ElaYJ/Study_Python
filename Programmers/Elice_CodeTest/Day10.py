# 제출 코드 ============================================================
N = 5 # int(input())
card_pockets = [1, 1, 2, 5, 3] # list(map(int, input().split()))

def all_numbers_in_window(window, K):
    length = len(set(window))
    if length == K:
        return True
    elif length < K:
        if window[0] > K-length:
            return True
        else: return False

def find_largest_k(card_pockets, N):
    for k in range(N, 1, -1):
        for i in range(N-k+1):
            current_window = sorted(card_pockets[i:k+i])
            if all_numbers_in_window(current_window, k):
                return k
    return 1

print(find_largest_k(card_pockets, N))
# 40점 ===============================================================
