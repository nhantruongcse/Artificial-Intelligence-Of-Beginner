import random
import numpy as np
import math

# board=  [ [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#           [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
#           [0,0,0,0,0,2,0,1,0,0,0,0,0,0,0],
#           [0,0,0,0,0,2,0,1,0,0,0,0,0,0,0],
#           [0,0,0,0,0,0,2,0,0,0,0,0,0,0,0],
#           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
# board = np.asarray(board)

##################################################################################################################


def agent_3(board, turn_id):
########################################################################## DEFINE

    ROW_COUNT = len(board)
    COL_COUNT = len(board[0])
    depth = 2
    piece = -1

    if turn_id==0:
        piece =1
    else:
        piece =2
    def full_play(board):
        if len(np.where(board == 0)) == 0:
            return True
        return False

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
        # print(f"kind {kind}: {mini_board} newidx {new_idx}")
        # update size
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
        # print(f"dif {dif_turn}")
        # print(mini_board)
        # print(f"new_idx {new_idx}")
        # trường hợp tổng quát:

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
        # print(f" left {idx_left}, right {idx_right}")
        # nếu không đủ khoảng cách, return false
        if idx_right - idx_left < 5:
            return False, '0'
        # đủ khoảng cách, kiểm tra xem điều kiện type nào và return
        if mini_board[new_idx - 1] == dif_piece or mini_board[new_idx + number] == dif_piece:
            return True, 'B'
        return True, 'A'

    def potential_step(board, piece):
        dif_piece = piece % 2 + 1
        result = []
        lst_turn = np.where(board == piece)
        dif_lst_turn = np.where(board == dif_piece)
        # danh sách index quân
        idx_lst = [(lst_turn[0][i], lst_turn[1][i]) for i in range(len(lst_turn[0]))]
        kind_lst = [[] for _ in range(len(idx_lst))]

        dif_idx_lst = [(dif_lst_turn[0][i], dif_lst_turn[1][i]) for i in range(len(dif_lst_turn[0]))]
        dif_kind_lst = [[] for _ in range(len(dif_idx_lst))]
        #print(idx_lst)
        ##################### xét các quân đã đạt 3, 4 của đối phương (để chặn) nếu cần:
        for j in range(len(dif_idx_lst)):
            temp = [[], [], [], []]
            idx = dif_idx_lst[j]
            #print(idx)
            check1, check2, check3, check4 = False, False, False, False
            n1, n2, n3, n4 = 4, 4, 4, 4
            i1, i2, i3, i4 = 0, 0, 0, 0
            while check1 == False:
                t1 = get_set_index_by_C(board, idx, dif_piece, n1 - i1)
                if t1 is not None:
                    check1 = True
                    temp[i1] += t1
                    break
                i1 += 1
                if (n1 - i1) <= 2:
                    break
            while check2 == False:
                t2 = get_set_index_by_R(board, idx, dif_piece, n2 - i2)
                if t2 is not None:
                    check2 = True
                    temp[i2] += t2
                    break
                i2 += 1
                if (n2 - i2) <= 2:
                    break
            while check3 == False:
                t3 = get_set_index_by_X1(board, idx, dif_piece, n3 - i3)
                if t3 is not None:
                    check3 = True
                    temp[i3] += t3
                    break
                i3 += 1
                if (n3 - i3) <= 2:
                    break
            while check4 == False:
                t4 = get_set_index_by_X2(board, idx, dif_piece, n4 - i4)
                if t4 is not None:
                    check4 = True
                    temp[i4] += t4
                    break
                i4 += 1
                if (n4 - i4) <= 2:
                    break
            dif_kind_lst[j] = temp
        for j in range(len(dif_idx_lst)):
            if dif_kind_lst[j]:
                for n in dif_kind_lst[j]:
                    result += n
        ################################# xét quân của mình - xét tập 4,3,2
        # ưu tiên xét tuyển tập hợp bước đã có 4 bước
        for j in range(len(idx_lst)):
            temp = [[], [], [], []]
            idx = idx_lst[j]
            #print(idx)
            check1, check2, check3, check4 = False, False, False, False
            n1, n2, n3, n4 = 4, 4, 4, 4
            i1, i2, i3, i4 = 0, 0, 0, 0
            while check1 == False:
                t1 = get_set_index_by_C(board, idx, piece, n1 - i1)
                if t1 is not None:
                    check1 = True
                    temp[i1] += t1
                    break
                i1 += 1
                if (n1 - i1) <= 1:
                    break
            while check2 == False:
                t2 = get_set_index_by_R(board, idx, piece, n2 - i2)
                if t2 is not None:
                    check2 = True
                    temp[i2] += t2
                    break
                i2 += 1
                if (n2 - i2) <= 1:
                    break
            while check3 == False:
                t3 = get_set_index_by_X1(board, idx, piece, n3 - i3)
                if t3 is not None:
                    check3 = True
                    temp[i3] += t3
                    break
                i3 += 1
                if (n3 - i3) <= 1:
                    break
            while check4 == False:
                t4 = get_set_index_by_X2(board, idx, piece, n4 - i4)
                if t4 is not None:
                    check4 = True
                    temp[i4] += t4
                    break
                i4 += 1
                if (n4 - i4) <= 1:
                    break
            kind_lst[j] = temp
        for j in range(len(idx_lst)):
            if kind_lst[j]:
                for n in kind_lst[j]:
                    result += n
        return result

    def potential_step_for_1_piece(board,piece):
        result = []
        lst_turn = np.where(board == piece)
        # danh sách index quân
        idx_lst = [(lst_turn[0][i], lst_turn[1][i]) for i in range(len(lst_turn[0]))]
        kind_lst = [[] for _ in range(len(idx_lst))]
        for j in range(len(idx_lst)):
            temp = []
            idx = idx_lst[j]
            t1 = get_set_index_by_C(board, idx, piece, 1)
            t2 = get_set_index_by_R(board, idx, piece, 1)
            t3 = get_set_index_by_X1(board, idx, piece, 1)
            t4 = get_set_index_by_X2(board, idx, piece, 1)

            if not t1 is None:
                kind_lst[j] += t1
            if not t2 is None:
                kind_lst[j] += t2
            if not t3 is None:
                kind_lst[j] += t3
            if not t4 is None:
                kind_lst[j] += t4
        for j in range(len(idx_lst)):
            if kind_lst[j]:
                result += kind_lst[j]
        return result

    def get_set_index_by_R(board, idx, piece, number):
        if number >= 4: vision = 6
        else: vision =5
        size = len(board)
        dif_piece = piece % 2 + 1
        start = (idx[0], 0)
        end = (idx[0], size - 1)
        if end[1] - idx[1] < number - 1: return None
        # kiểm tra phải chuỗi liên tục piece
        for i in range(number):
            if board[idx[0]][idx[1] + i] != piece:
                return None
        # xác định khoảng không gian bị vướng (nếu có)
        back_lengh = idx[1] - start[1]
        forward_lengh = end[1] - idx[1]
        extend_back = back_lengh
        extend_forward = forward_lengh - (number - 1)
        lst_back_iter = [-i for i in range(back_lengh + 1)]
        for j in lst_back_iter:
            if board[idx[0]][idx[1] + j] == dif_piece:
                extend_back = -j - 1
                break
        for j in range(number, forward_lengh + 1):
            if board[idx[0]][idx[1] + j] == dif_piece:
                extend_forward = j - number
                break
        # nếu không đủ khoảng cách, return false
        if extend_back + extend_forward + number < 5:
            return None
        # đủ khoảng cách, kiểm tra xem điều kiện type nào và return
        else:
            # trả về 1 tupler có "number" index:
            # return {(idx[0], idx[1] + i) for i in range(number)}
            pos = [-i for i in range(1, min(vision - number, extend_back) + 1)] + [i for i in range(number, min(vision,
                                                                                                                forward_lengh) + 1)]
            temp = [(idx[0], idx[1] + i) for i in pos if board[idx[0]][idx[1] + i] == 0]
            return temp

    def get_set_index_by_X1(board, idx, piece, number):
        if number >= 4: vision = 6
        else: vision =5
        size = len(board)
        dif_piece = piece % 2 + 1
        start = ()
        end = ()
        for i in range(size):
            if idx[0] + i == 14 or idx[1] + i == 14:
                end = idx[0] + i, idx[1] + i
                break
        for i in range(size):
            if idx[0] - i == 0 or idx[1] - i == 0:
                start = idx[0] - i, idx[1] - i
                break
        # print(f" {start} {end}")
        if end[1] - idx[1] < number - 1: return None
        # kiểm tra phải chuỗi liên tục piece
        for i in range(number):
            if board[idx[0] + i][idx[1] + i] != piece:
                return None
        # xác định khoảng không gian bị vướng (nếu có)
        back_lengh = abs(idx[1] - start[1])
        forward_lengh = abs(end[1] - idx[1])
        lst_back_iter = [-i for i in range(back_lengh + 1)]
        extend_back = back_lengh
        extend_forward = forward_lengh - (number - 1)
        for j in lst_back_iter:
            if board[idx[0] + j][idx[1] + j] == dif_piece:
                extend_back = -j - 1
                break
        for j in range(number, forward_lengh + 1):
            if board[idx[0] + j][idx[1] + j] == dif_piece:
                extend_forward = j - number
                break

        # nếu không đủ khoảng cách, return false
        if extend_back + extend_forward + number < 5:
            return None
        # đủ khoảng cách, kiểm tra xem điều kiện type nào và return
        else:
            # trả về 1 tupler có "number" index:
            # return {(idx[0] + i, idx[1] + i) for i in range(number)}
            pos = [-i for i in range(1, min(vision - number, extend_back) + 1)] + [i for i in range(number, min(vision,
                                                                                                                forward_lengh) + 1)]
            temp = [(idx[0] + i, idx[1] + i) for i in pos if board[idx[0] + i][idx[1] + i] == 0]
            return temp

    def get_set_index_by_X2(board, idx, piece, number):
        if number>=4: vision =6
        else: vision =5
        size = len(board)
        # print(idx)
        dif_piece = piece % 2 + 1
        for i in range(size):
            if (idx[0] - i == 0) or (idx[1] + i == 14) or (idx[0] + i == 14) or (idx[1] - i == 0):
                if idx[0] - i == 0:
                    start = idx[0] - i, idx[1] + i
                    end = (start[1], start[0])
                    break
                if idx[0] + i == 14:
                    end = idx[0] + i, idx[1] - i
                    start = (end[1], end[0])
                    break
                if idx[1] - i == 0:
                    end = idx[0] + i, idx[1] - i
                    start = (end[1], end[0])
                    break
                if idx[1] + i == 14:
                    start = idx[0] - i, idx[1] + i
                    end = (start[1], start[0])
                    break
        # print(f" {start} {end}")
        if idx[1] - end[1] < number - 1: return None
        # kiểm tra phải chuỗi liên tục piece
        for i in range(number):
            if board[idx[0] + i][idx[1] - i] != piece:
                return None
        # xác định khoảng không gian bị vướng (nếu có)
        back_lengh = abs(idx[1] - start[1])
        forward_lengh = abs(idx[1] - end[1])
        lst_back_iter = [-i for i in range(back_lengh + 1)]
        extend_back = back_lengh
        extend_forward = forward_lengh - (number - 1)
        for j in lst_back_iter:
            if board[idx[0] + j][idx[1] - j] == dif_piece:
                extend_back = -j - 1
                break
        for j in range(number, forward_lengh + 1):
            if board[idx[0] + j][idx[1] - j] == dif_piece:
                extend_forward = j - number
                break
        # print(f" after sau {extend_back} truoc {extend_forward}")
        # nếu không đủ khoảng cách, return false
        if extend_back + extend_forward + number < 5:
            return None
        # đủ khoảng cách, kiểm tra xem điều kiện type nào và return
        else:
            # trả về 1 tupler có "number" index:
            # return {(idx[0] + i, idx[1] - i) for i in range(number)}
            pos = [-i for i in range(1, min(vision - number, extend_back) + 1)] + [i for i in range(number, min(vision,
                                                                                                                forward_lengh) + 1)]
            temp = [(idx[0] + i, idx[1] - i) for i in pos if board[idx[0] + i][idx[1] - i] == 0]
            return temp

    def get_set_index_by_C(board, idx, piece, number):
        if number >= 4: vision = 6
        else: vision =5
        size = len(board)
        dif_piece = piece % 2 + 1
        start = (0, idx[1])
        end = (size - 1, idx[1])
        if end[0] - idx[0] < number - 1: return None
        # kiểm tra phải chuỗi liên tục piece
        for i in range(number):
            if board[idx[0] + i][idx[1]] != piece:
                return None
        # xác định khoảng không gian bị vướng (nếu có)
        back_lengh = idx[0] - start[0]
        forward_lengh = end[0] - idx[0]
        extend_back = back_lengh
        extend_forward = forward_lengh - (number - 1)
        lst_back_iter = [-i for i in range(back_lengh + 1)]
        for j in lst_back_iter:
            if board[idx[0] + j][idx[1]] == dif_piece:
                extend_back = -j - 1
                break
        for j in range(number, forward_lengh + 1):
            if board[idx[0] + j][idx[1]] == dif_piece:
                extend_forward = j - number
                break
        # print(f" after {extend_back} {extend_forward}")
        # nếu không đủ khoảng cách, return false
        if extend_back + extend_forward + number < 5:
            return None
        # đủ khoảng cách, kiểm tra xem điều kiện type nào và return
        else:
            # trả về 1 tupler có "number" index:
            # return {(idx[0] + i, idx[1]) for i in range(number)}
            pos = [-i for i in range(1, min(vision - number, extend_back) + 1)] + [i for i in range(number, min(vision,
                                                                                                                forward_lengh) + 1)]
            temp = [(idx[0] + i, idx[1]) for i in pos if board[idx[0] + i][idx[1]] == 0]
            return temp

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
#################################################################### IMPORTANT
    def tinhdiem(board, piece):
        dif_piece = piece % 2 + 1
        # tính điểm cho điểm
        count_main_2 = count_continues_all(board, piece, 2)
        count_dif_2 = count_continues_all(board, dif_piece, 2)
        count_main_3 = count_continues_all(board, piece, 3)
        count_dif_3 = count_continues_all(board, dif_piece, 3)
        count_main_4 = count_continues_all(board, piece, 4)
        count_dif_4 = count_continues_all(board, dif_piece, 4)
        #
        # mark_2 = 2 * (count_main_2[0] - count_dif_2[0]) + 1 * (count_main_2[1] - count_dif_2[1])
        # mark_3 = 100 * count_main_3[0] - 500*count_dif_3[0] + 20 * (count_main_3[1] - count_dif_3[1])
        # mark_4 = 1000 * (count_main_4[0] - count_dif_4[0]) + 200 * count_main_4[1] -500* count_dif_4[1]

        mark_2 = 50 * (count_main_2[0] - count_dif_2[0]) + 10 * (count_main_2[1] - count_dif_2[1])
        mark_3 = 100 * count_main_3[0] - 200*count_dif_3[0] + 50 * (count_main_3[1] - count_dif_3[1])
        mark_4 = 1000 * count_main_4[0] - 1500* count_dif_4[0] + 500 * count_main_4[1] -1500* count_dif_4[1]
        mark = mark_2 + mark_3 + mark_4
        return mark

    def minimax(board, piece, depth, alpha=-math.inf, beta=math.inf,step=(-1,-1)):
        result = (-1, -1)
        dif_piece = piece % 2 + 1
        if who_wins(board,piece):
            return (-1,-1),10000
        if depth == 0:
            k = tinhdiem(board, piece)
            return (-1, -1), k

        lst_idx_available = set(potential_step(board,piece))
        lst_idx_available = tuple(lst_idx_available)
        if not lst_idx_available:
            lst_idx_available = set(potential_step_for_1_piece(board,piece))
        if len(lst_idx_available) == 0:
            return (-1, -1), tinhdiem(board, piece)
        # step = (-1, -1)
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
                id_row = id_dif[0] + random.randint(-1, 1)
                id_col = id_dif[1] + random.randint(-1, 1)
                if id_row >= 0 and id_row < size and id_col >= 0 and id_col < size:
                    if id_row != id_dif[0] and id_col != id_dif[1]:
                        return id_row, id_col
########################################################################## MAIN FUNCTION
    if piece not in board:
        return gen_init(board,piece)
    else:
        return minimax(board, piece, depth, alpha=-math.inf, beta=math.inf)[0]


# print(agent_1(board,1))
