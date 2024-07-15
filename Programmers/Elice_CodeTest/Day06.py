class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            return True
        return False


def minimize_red_edges(n, colors):
    uf = UnionFind(n)
    red_edge_count = 0

    for color in colors:
        for u in range(n):
            for v in range(u + 1, n):
                if uf.find(u) != uf.find(v):
                    if color == 0:
                        red_edge_count += 1
                    uf.union(u, v)
                    break
            else:
                continue
            break

    return red_edge_count


# 입력 받기
n = int(input())
colors = list(map(int, input().split()))

# 결과 출력
print(minimize_red_edges(n, colors))
