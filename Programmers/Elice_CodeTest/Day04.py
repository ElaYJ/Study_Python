def tree_game(N, edges):
    from collections import defaultdict, deque

    # 트리 구조 저장
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)

    # 게임 결과를 저장하는 배열 (-1: 아직 결정되지 않음, 0: 후공 승, 1: 선공 승)
    result = [-1] * (N + 1)

    def dfs(node):
        # 리프 노드인지 확인
        if not tree[node]: # leaf node면 빈 리스트([])를 반환
            result[node] = 1  # 리프 노드에서 시작하면 선공이 승리
            return result[node]

        # 자식 노드 결과 확인
        child_results = []
        for child in tree[node]:
            child_results.append(dfs(child))

        # 자식 노드 중 하나라도 후공 승이면 현재 노드에서는 선공이 이길 수 없다.
        if 0 in child_results:
            result[node] = 1  # 선공 승
        else:
            result[node] = 0  # 후공 승

        return result[node]

    # 루트 노드에서 시작하여 DFS 실행
    dfs(1)

    return result[1:]


# 테스트 예제
N = 5
# edges = [(1, 2), (1, 3), (2, 4), (3, 5)]
edges1 = [(1, 3), (1, 2), (3, 4), (1, 5)]
edges2 = [(1,3),(1,2),(3,5),(3,6),(2,4)]
print(tree_game(N, edges1))  # 각 노드에서 선공이 이기는지 후공이 이기는지 출력
print(tree_game(6, edges2))


