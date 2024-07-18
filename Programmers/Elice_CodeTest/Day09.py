import heapq


def dijkstra(grid, start):
    N = len(grid)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    pq = [(0, start[0], start[1])]  # (거리, 행, 열)
    distances = [[float('inf')] * N for _ in range(N)]
    distances[start[0]][start[1]] = 0

    while pq:
        current_distance, x, y = heapq.heappop(pq)

        # 현재 격자의 거리가 기존 거리보다 크다면 무시
        if current_distance > distances[x][y]:
            continue

        # 현재 격자의 모든 인접한 격자를 확인
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                distance = current_distance + grid[x][y] + grid[nx][ny]

                # 새로운 경로가 기존 경로보다 짧은 경우
                if distance < distances[nx][ny]:
                    distances[nx][ny] = distance
                    heapq.heappush(pq, (distance, nx, ny))

    return distances

# 예제 입력
N = 3
grid = [
    [2, 3, 4],
    [1, 4, 3],
    [1, 1, 1]
]

# 시작 지점 (1, 1)을 (0, 0)으로 조정
start = (0, 0)

# 다익스트라 알고리즘 실행
distances = dijkstra(grid, start)

# 출력 결과: (0, 0)에서 각 격자까지의 최단 거리
for row in distances:
    print(row)


# 제출 코드 =========================================================================
import heapq
import sys

def dijkstra(grid, start, target, N):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    pq = [(0, start[0], start[1])]  # (거리, 행, 열)
    distances = [[sys.maxsize] * N for _ in range(N)]
    distances[start[0]][start[1]] = 0

    while pq:  # primary queue
        current_distance, x, y = heapq.heappop(pq)
        if (x, y) == target:
            return current_distance

        if current_distance > distances[x][y]:
            continue

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                distance = current_distance + grid[x][y] + grid[nx][ny]
                if distance < distances[nx][ny]:
                    distances[nx][ny] = distance
                    heapq.heappush(pq, (distance, nx, ny))

    # return sys.maxsize

N = int(input())

grid = []
for _ in range(N):
    row = list(map(int, input().split()))
    grid.append(row)

steps = [(0, 0)]
for _ in range(5):
    r, c = map(int, input().split())
    steps.append((r - 1, c - 1))

total_time = 0
for i in range(len(steps) - 1):
    # time = dijkstra(grid, steps[i], steps[i+1], N)
    # if time == sys.maxsize:
    #     print(-1)
    #     break
    # total_time += time
    total_time += dijkstra(grid, steps[i], steps[i + 1], N)

print(total_time)
# 64점 ======================================================================================