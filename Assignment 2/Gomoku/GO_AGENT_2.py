
import random
import numpy as np
import math

##################################################################################################################
def agent_2(board, turn_id):
    ########################################################################## DEFINE
    # Khởi tạo các thông số:
    ROW_COUNT = len(board)
    COL_COUNT = len(board[0])
    depth = 2
    piece = -1
    if turn_id==0:
        piece =1
    else:
        piece =2
    ########################################################################## FUNCTION

    # hàm who_wins để kiểm tra nếu piece có phải đã chiến thắng bàn cờ này
    def who_wins(board, piece):
        # check for horizontal win
        for c in range(COL_COUNT - 4):
            for r in range(ROW_COUNT):
                if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][
                    c + 3] == piece \
                        and board[r][c + 4] == piece:
                    return True

        # check for vertical win
        for c in range(COL_COUNT):
            for r in range(ROW_COUNT - 4):
                if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][
                    c] == piece \
                        and board[r + 4][c] == piece:
                    return True

        # check for positively sloped diagonal wih
        for c in range(COL_COUNT - 4):
            for r in range(4, ROW_COUNT):
                if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and \
                        board[r - 3][c + 3] == piece \
                        and board[r - 4][c + 4] == piece:
                    return True

        # check for negatively sloped diagonal win
        for c in range(COL_COUNT - 4):
            for r in range(ROW_COUNT - 4):
                if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and \
                        board[r + 3][c + 3] == piece \
                        and board[r + 4][c + 4] == piece:
                    return True

    # hàm check_type để xác định chuỗi liên tiếp các quân "piece" theo các phương R,C,X1,X2, và có bị chặn đầu nào không
    # nếu hình thành chuỗi, có khả năng hình thành chuỗi 5 và bị chặn 1 đầu => True, Type B;
    # nếu hình thành chuỗi, có khả năng hình thành chuỗi 5 và không bị chặn => True, Type A;
    # còn lại trả về False, "notice"
    def check_type(board, idx, piece, number, kind):
        size = len(board)
        dif_piece = piece % 2 + 1
        mini_board = []
        new_idx = -1
        if kind == "C":
            mini_board = board[:, idx[1]]
            new_idx = idx[0]
        elif kind == "R":
            mini_board = board[idx[0], :]
            new_idx = idx[1]
        elif kind == "X1":
            mini_board = [board[idx[0] + i][idx[1] + i] for i in range(-size, size + 1) if
                          idx[0] + i >= 0 and idx[0] + i < size and idx[1] + i >= 0 and idx[1] + i < size]
            new_idx = idx[1]
        elif kind == "X2":
            mini_board = [board[idx[0] - i][idx[1] + i] for i in range(-size, size + 1) if
                          idx[0] - i >= 0 and idx[0] - i < size and idx[1] + i >= 0 and idx[1] + i < size]
            new_idx = idx[1]
        else:
            return False, "error, miss code"
        # update size do đang xét mini_board
        size = len(mini_board)
        if size < 5:
            return False, "Not enough len"
        left = new_idx - 5
        right = new_idx + 5  #
        if left < 0:
            left = 0
        if right > size:
            right = size
        if new_idx + 5 > size:
            return False, "Not enough space"
        for i in range(number):
            if mini_board[new_idx + i] != piece:
                return False, "Have dif_turn in number"
        # kiểm tra nếu indx đang ở mép trái => không cần kiểm tra đk trái
        if new_idx == 0:
            for j in range(number + 1, right):
                if mini_board[j] == dif_piece:
                    return False, '0'
            return True, 'A'
        # kiểm tra nếu indx đang ở mép phải => không cần kiểm tra đk phải
        if new_idx + number - 1 == size - 1:
            for j in range(left, new_idx):
                if mini_board[j] == dif_piece:
                    return False, '0'
            return True, 'A'
        idx_left = left
        idx_right = right  # idx[1] = 4=> right= 9, do right chỉ lấy ) => xét 4-8
        lst_left_iter = [i for i in range(left, new_idx)]
        lst_left_iter.reverse()
        for j in lst_left_iter:
            if mini_board[j] == dif_piece:
                idx_left = j
                break
        for j in range(new_idx + 1, right):
            if mini_board[j] == dif_piece:
                idx_right = j
                break
        # nếu không đủ khoảng cách, return false
        if idx_right - idx_left < 5:
            return False, '0'
        # đủ khoảng cách, kiểm tra xem điều kiện type nào và return
        if mini_board[new_idx - 1] == dif_piece or mini_board[new_idx + number] == dif_piece:
            return True, 'B'
        return True, 'A'

    # hàm count_continues_all sẽ đếm số chuỗi và type của quân piece đang có trên bàn
    # Với agent_1: do hàm count_continues_all này có thể đếm trùng, tức là chuỗi 4 có các chuỗi con là chuỗi 3, chuỗi 2
    # thì hàm count_continues_all này vẫn tính vào
    def count_continues_all(board, piece, number):
        # đếm số lượng dãi liên tục của "turn" có số quân bằng "number"
        # return: (A-m,B-n) với A: số lượng chuỗi free 2 đầu đủ hình thành 5; B: số lượng chuỗi bị chặn 1 đầu đủ hình thành 5

        count_A = 0
        count_B = 0
        lst_turn = np.where(board == piece)
        # lst_non_turn = np.where(board == piece % 2 + 1)
        # danh sách index quân của "turn"
        idx_lst = [(lst_turn[0][i], lst_turn[1][i]) for i in range(len(lst_turn[0]))]

        for i in idx_lst:
            check_C = check_type(board, i, piece, number, "C")
            check_R = check_type(board, i, piece, number, "R")
            check_X1 = check_type(board, i, piece, number, "X1")
            check_X2 = check_type(board, i, piece, number, "X2")
            if check_C[0]:
                if check_C[1] == 'A':
                    count_A += 1
                else:
                    count_B += 1
            if check_R[0]:
                if check_R[1] == 'A':
                    count_A += 1
                else:
                    count_B += 1
            if check_X1[0]:
                if check_X1[1] == 'A':
                    count_A += 1
                else:
                    count_B += 1
            if check_X2[0]:
                if check_X2[1] == 'A':
                    count_A += 1
                else:
                    count_B += 1
        return count_A, count_B

    # hàm tinhdiem sẽ tính điểm số cho trạng thái hiện tại của quân piece theo ý đồ của người lập trình
    def tinhdiem(board, piece):
        dif_piece = piece % 2 + 1
        # tính điểm cho điểm
        count_main_2 = count_continues_all(board, piece, 2)
        count_dif_2 = count_continues_all(board, dif_piece, 2)
        count_main_3 = count_continues_all(board, piece, 3)
        count_dif_3 = count_continues_all(board, dif_piece, 3)
        count_main_4 = count_continues_all(board, piece, 4)
        count_dif_4 = count_continues_all(board, dif_piece, 4)
        mark_2 = 2 * (count_main_2[0] - count_dif_2[0]) + 1 * (count_main_2[1] - count_dif_2[1])
        mark_3 = 100 * count_main_3[0] - 500*count_dif_3[0] + 20 * (count_main_3[1] - count_dif_3[1])
        mark_4 = 1000 * count_main_4[0] - 1500*count_dif_4[0] + 100 * count_main_4[1] - 1000*count_dif_4[1]
        mark = mark_2 + mark_3 + mark_4
        return mark

    # hàm check_idx_valid_pick để xác định index có hợp lệ và đang =0 (có thể chọn) hay không
    def check_idx_valid_pick(board,idx):
        size = len(board)
        row = idx[0]
        col = idx[1]
        if row<0 or col <0:
            return False
        if row >=size or col>=size:
            return False
        if board[row][col]== 0:
            return True
        return False

    # hàm minimax: có cài thuật toán alpha-beta bên trong, xác định index tieps theo được chọn để đi
    def minimax(board, piece, depth, alpha=-math.inf, beta=math.inf,step=(-1,-1)):
        result =(-1,-1)
        dif_piece = piece % 2 + 1
        size = len(board)
        if who_wins(board,piece):
            return step,10000
        if depth == 0:
            k = tinhdiem(board, piece)
            return step, k
        picked_pos = np.where(board == piece)
        picked_lst = [(picked_pos[0][i], picked_pos[1][i]) for i in range(len(picked_pos[0]))]
        dif_picked_pos = np.where(board == dif_piece)
        dif_picked_lst = [(dif_picked_pos[0][i], dif_picked_pos[1][i]) for i in range(len(dif_picked_pos[0]))]
        lst_idx_available = set()
        k = 2
        for idx in picked_lst: # các ô cùng piece
            row = idx[0]
            col = idx[1]
            ################# k là hệ số bao quanh vị trí điểm đang xét =>block size: row-2:col-2, row+2: col+2
            for i in range(-k,k+1):
                for j in range(-k,k+1):
                    cell = (row+i,col+j)
                    if check_idx_valid_pick(board,cell):
                        lst_idx_available.add(cell)
        for idx in dif_picked_lst: # các ô khác piece để xem xét chặn
            row = idx[0]
            col = idx[1]
            ################# k là hệ số bao quanh vị trí điểm đang xét =>block size: row-2:col-2, row+2: col+2
            for i in range(-k,k+1):
                for j in range(-k,k+1):
                    cell = (row+i,col+j)
                    if check_idx_valid_pick(board,cell):
                        lst_idx_available.add(cell)
        lst_idx_available = tuple(lst_idx_available)

        if len(lst_idx_available) == 0:
            return step, tinhdiem(board, piece)
        for step in lst_idx_available:
            board[step[0]][step[1]] = piece
            result_op = -minimax(board, dif_piece, depth - 1, -beta, -alpha,step)[1]
            board[step[0]][step[1]] = 0
            if result_op > alpha:
                result = step
                alpha = result_op
            if alpha >= beta:
                return (step, alpha)
        return result, alpha

    # hàm gen_init dùng để khi quân piece chưa có quân nào => chọn 1 vị trí theo ý đồ chời lập trình
    def gen_init(board, piece):
        dif_piece = piece % 2 + 1
        size = len(board)

        if dif_piece not in board:
            row = random.randrange(5,10)
            col = random.randrange(5,10)
            return (row, col)
        else:
            temp = np.where(board == dif_piece)
            id_dif = temp[0][0], temp[1][0]
            while True:
                id_row = id_dif[0] + random.randint(-2, 2)
                id_col = id_dif[1] + random.randint(-2, 2)
                if id_row >= 0 and id_row < size and id_col >= 0 and id_col < size:
                    if id_row != id_dif[0] and id_col != id_dif[1]:
                        return id_row, id_col

    ########################################################################## MAIN FUNCTION OF AGENT_1
    if piece not in board:
        return gen_init(board,piece)
    else:
        return minimax(board, piece, depth, alpha=-math.inf, beta=math.inf,)[0]

