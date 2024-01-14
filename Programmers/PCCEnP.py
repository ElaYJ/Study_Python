# <PCCE 기출 9번 [Lv.1] 이웃한 칸> ------------------------------------------------------------

def my_solution1(board, h, w):
    n = len(board)
    count = 0
    dh, dw = [0, 1, -1, 0], [1, 0, 0, -1]
    print(dh, dw)

    for i in range(4):
        h_check, w_check = h + dh[i], w + dw[i]
        print(h_check, w_check)
        if 0 <= h_check < n and 0 <= w_check < n:
            print(board[h][w], board[h_check][w_check])
            if board[h][w] == board[h_check][w_check]:
                count += 1

    return count


def solution1(board, h, w):
    n = len(board)
    count = 0 # board[h][w]와 이웃한 칸(상, 하, 좌, 우)들 중 같은 색의 수
    color = board[h][w] # board[h][w]의 색

    # 상, 하, 좌, 우
    directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]

    # directions 순회 (상 -> 하 -> 좌 -> 우)
    for dir_h, dir_w in directions:

         # 이동할 인덱스 생성
         mov_h = h + dir_h
         mov_w = w + dir_w

         # 이동한 인덱스가 유효할 시
         if (0 <= mov_h < n) and (0 <= mov_w < n):

              # 이동한 칸의 색과 board[h][w]의 색이 같을 시 count += 1
              count += int(color == board[mov_h][mov_w])

    return count

#print(solution([
# ["blue", "red", "orange", "red"],
# ["red", "red", "blue", "orange"],
# ["blue", "orange", "red", "red"],
# ["orange", "orange", "red", "blue"]], 1, 1))




# <PCCE 기출 10번 [Lv.1] 데이터 분석> ---------------------------------------------------------


data = [[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]]
for row in data:
    data.remove(row)
    print(data)
    break

print(sorted(data, key=lambda row: row[3]))

# 런타임 에러 --------------------------------------------------
# 변수를 2개 더 선언한 차이밖에 없음
# 찾았다.!! 에러 이유: 젠장~!!!!! 'maximum'을 'maximun'으로 썼다. 아~ 놔~
def my_solution2(data, ext, val_ext, sort_by):
    answer = []
    columns = ['code', 'date', 'maximun', 'remain']
    idx = columns.index(ext)
    sort_idx = columns.index(sort_by)
    for row in data:
        if row[idx] < val_ext:
            answer.append(row)
    answer = sorted(answer, key=lambda row: row[sort_idx])
    return answer
# -------------------------------------------------------------

def solution3(data, ext, val_ext, sort_by):
    answer = []
    columns = ['code', 'date', 'maximum', 'remain']

    for row in data:
        if row[columns.index(ext)] < val_ext:
            answer.append(row)

    answer.sort(key=lambda row: row[columns.index(sort_by)])
    return answer


def solution4(data, ext, val_ext, sort_by):
    columns = {
        'code': 0, 'date': 1, 'maximum': 2, 'remain': 3
    }
    answer = [row for row in data if row[columns[ext]] < val_ext]
    answer.sort(key=lambda row: row[columns[sort_by]])
    return answer


def solution5(data, ext, val_ext, sort_by):
    columns = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    answer = sorted(filter(lambda row: row[columns[ext]] < val_ext, data),
                    key=lambda row: row[columns[sort_by]])
    return answer


data = [[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]]
print(solution5(data, "date", 20300501, "remain"))




# <PCCP 기출 1번 [Lv.1] 붕대 감기> ------------------------------------------------------------







# <PCCP 기출 2번 [Lv.2] 석유 시추> ------------------------------------------------------------







# <PCCP 기출 3번 [Lv.2] 수레 움직이기> ---------------------------------------------------------











# <PCCP 기출 4번 [Lv.3] 아날로그 시계> ---------------------------------------------------------




