import sys

# input = sys.stdin.read
# data = input().strip().split()
# N, M = int(data.pop(0)), int(data.pop(0))
# board = [x for x in data]
# minModify = 0


# def print_sub_chessboard(x, y):
#     c = 0
#     temp = []
#     for i in range(8):
#         temp.append(board[x + i][y : y + 8])
#     for a in range(8):
#         for b in range(7):
#             color = temp[a][b]
#             if temp[a][b + 1] == color:
#                 c += 1
#     return c


# for i in range(N - 7):
#     for j in range(M - 7):
#         print(f"부분 체스판 (x : {i}, y : {j})")
#         minModify = print_sub_chessboard(i, j)

# # 2. 체스판 비교


def count_flips(board, start_row, start_col):
    count_B = 0
    count_W = 0
    for i in range(8):
        for j in range(8):
            expected_color_B = "B" if (i + j) % 2 == 0 else "W"
            expected_color_W = "W" if (i + j) % 2 == 0 else "B"
            if board[start_row + i][start_col + j] != expected_color_B:
                count_B += 1
            if board[start_row + i][start_col + j] != expected_color_W:
                count_W += 1
    return min(count_B, count_W)


def find_min_changes(board, N, M):
    min_changes = float("inf")
    for i in range(N - 7):
        for j in range(M - 7):
            changes = count_flips(board, i, j)
            if changes < min_changes:
                min_changes = changes
    return min_changes


input = sys.stdin.read
data = input().strip().split()
N, M = int(data.pop(0)), int(data.pop(0))
board = [x for x in data]
print(find_min_changes(board, N, M))
