N, M, K, T = map(int, input().split())

attend_prayers = [0] * 301
for _ in range(M):
    a, b = map(int, input().split())
    attend_prayers[a:b+1] = [v+1 for v in attend_prayers[a:b+1]]
attend_prayers = attend_prayers[1:N+1]

attend_friends = 0
for i in range(N):
    current_prayers = attend_friends + attend_prayers[i]

    if attend_prayers[i] >= T and attend_friends > 0:
        K -= attend_friends
        attend_friends = 0

    if current_prayers < T:
        d = T - current_prayers
        if K >= d:
            attend_friends += d
        else:
            print(i-1)
            break
    else: continue
