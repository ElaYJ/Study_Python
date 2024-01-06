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









# <PCCP 기출 1번 [Lv.1] 붕대 감기> ------------------------------------------------------------







# <PCCP 기출 2번 [Lv.2] 석유 시추> ------------------------------------------------------------







# <PCCP 기출 3번 [Lv.2] 수레 움직이기> ---------------------------------------------------------











# <PCCP 기출 4번 [Lv.3] 아날로그 시계> ---------------------------------------------------------




