# @title
import random
import numpy as np
import math

# board=  [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#         [0,0,1,1,1,0,0,0,0,0,0,0,0,0,0],
#         [2,0,0,2,0,0,0,0,0,0,0,0,0,0,0],
#         [0,1,2,2,2,1,0,0,0,0,0,0,0,0,0],
#         [0,2,1,2,0,2,0,2,0,0,0,0,0,0,0],
#         [2,2,1,1,0,2,1,2,0,0,0,0,0,0,0],
#         [0,1,0,1,2,1,1,1,0,0,0,0,0,0,0],
#         [1,0,2,1,1,1,2,0,1,0,0,0,0,0,0],
#         [0,0,1,2,1,1,1,2,2,2,1,0,0,0,0],
#         [0,0,0,2,1,2,2,1,2,0,0,0,0,0,0],
#         [0,0,0,1,2,0,0,0,2,1,0,0,0,0,0],
#         [0,0,2,0,0,0,0,0,2,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
# board = np.asarray(board)

##################################################################################################################


def agent_4(board, turn_id):
########################################################################## DEFINE
    ROW_COUNT = len(board)
    COL_COUNT = len(board[0])
    depth = 2
    piece = -1
    if turn_id==0:
        piece =1
    else:
        piece =2


########################################################################## SUPPORT FUNCTION
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
    # hàm trả về danh sách các node (index) cho hàm minimax
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
    # hàm trả về danh sách các node (index) cho hàm minimax khi chỉ có 1 piece
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
    # hàm trả vệ danh sách các node theo phương R
    def get_set_index_by_R(board, idx, piece, number):
        if number >= 4: vision = 7
        else: vision =6
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
    # hàm trả vệ danh sách các node theo phương X1
    def get_set_index_by_X1(board, idx, piece, number):
        if number >= 4: vision = 7
        else: vision =6
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
    # hàm trả vệ danh sách các node theo phương X2
    def get_set_index_by_X2(board, idx, piece, number):
        if number>=4: vision =7
        else: vision =6
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
    # hàm trả vệ danh sách các node theo phương C
    def get_set_index_by_C(board, idx, piece, number):
        if number >= 4: vision = 7
        else: vision =6
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


    # HÀM XÉT INDEX HIỆN TẠI THỎA CÁC TYPE NÀO
    def count_type_piece(board,idx,piece):
        # có 12 kiểu cần kiểm tra
        result = [0 for i in range(12)]
        size = len(board)
        dif_piece = piece % 2 + 1
        mini_board_C = board[:, idx[1]]
        new_idx_C = idx[0]
        mini_board_R = board[idx[0], :]
        new_idx_R = idx[1]
        mini_board_X1 = [board[idx[0] + i][idx[1] + i] for i in range(-size, size + 1) if
                      idx[0] + i >= 0 and idx[0] + i < size and idx[1] + i >= 0 and idx[1] + i < size]
        new_idx_X1=-1
        for i in range (size):
            if idx[0]+i ==14 or idx[1]+i==14:
                new_idx_X1 = len(mini_board_X1)-i-1
                break
        mini_board_X2 = [board[idx[0] - i][idx[1] + i] for i in range(-size, size + 1) if
                      idx[0] - i >= 0 and idx[0] - i < size and idx[1] + i >= 0 and idx[1] + i < size]
        new_idx_X2=-1
        for j in range(size):
            if idx[0]+j ==14 or idx[1]-j==0:
                new_idx_X2 = len(mini_board_X2)-j-1
                break

        all_board = [mini_board_C,mini_board_R,mini_board_X1,mini_board_X2]
        all_new_idx = [new_idx_C,new_idx_R,new_idx_X1, new_idx_X2]
        for id_mini_board in range(len(all_board)): # có tối đa 4 hướng
            ##### loại bỏ các board không đủ lengh
            if len(all_board[id_mini_board])<5:
                continue
            mini_board = np.array(all_board[id_mini_board]).tolist()
            new_idx = all_new_idx[id_mini_board]
            ###để dễ kiểm tra, ta đảm bảo new_idx >=2 (để khỏi sợ out of range) bằng cách chèn thêm dif_piece
            ### và chèn thêm 2 dif_piece vào sau cùng
            mini_board.append(dif_piece)
            mini_board.append(dif_piece)
            if new_idx==0:
                mini_board.insert(0,dif_piece)
                mini_board.insert(0, dif_piece)
                new_idx+=2
            elif new_idx==1:
                mini_board.insert(0,dif_piece)
                new_idx+=1

            new_size = len(mini_board)
            # xem thử chuỗi bao nhiêu piece liên tục:
            number=new_size-1
            forward = new_size-1
            for i in range(new_idx+1, new_size):
                if mini_board[i] != piece:
                    number = i-new_idx-1
                    break
            for i in range(new_idx+1, new_size):
                if mini_board[i] == dif_piece:
                    forward = i-new_idx-1
                    break
            if number==4:
                if forward + number <5:
                  continue
                if mini_board[new_idx-1] == dif_piece and mini_board[new_idx+number] == dif_piece:
                    continue
                elif mini_board[new_idx-1] == dif_piece or mini_board[new_idx+number]==dif_piece:
                    result[1]+=1
                else: result[0]+=1
            elif number==3:
                if forward + number <5:
                  continue
                if mini_board[new_idx-1]==piece: # đã xét mức cao nhất trước đó, ko xét lại
                    continue
                if mini_board[new_idx-1]==0:
                    if mini_board[new_idx+number]==0:
                        result[3]+=1
                        if mini_board[new_idx+number+1]==piece or mini_board[new_idx-2]==piece:
                            result[2]+=1
                    elif mini_board[new_idx-2]==0:
                        result[5]+=1
                else:
                    if mini_board[new_idx+number]==0:
                        if mini_board[new_idx+number+1]==0:
                            result[5]+=1
                        elif mini_board[new_idx+number+1]==piece:
                            result[4]+=1
            elif number==2:
                if mini_board[new_idx-1]==piece:
                    continue
                if mini_board[new_idx-1]==0:
                    if mini_board[new_idx+number]==0:
                        result[10]+=1
                        if  mini_board[new_idx+number+1]==piece:
                            if new_idx+number+2 <new_size:
                                if mini_board[new_idx+number+2]==piece:
                                    result[6]+=1 #@@#3
                                elif mini_board[new_idx+number+2]==0:
                                    result[8]+=1
                    else:
                        if new_idx>=3:
                            if mini_board[new_idx-1]==0 and mini_board[new_idx-2]==0:
                                result[11]+=1
                else:
                    if forward+number<5:
                        continue
                    if mini_board[new_idx+number]==0:
                        result[11] += 1
                        if mini_board[new_idx+number+1]==piece:
                            result[9]+=1
        return result
    # HÀM PHỤC VỤ ĐẾM TYPE 0-11 CHO CẢ BOARD
    def count_continues_all(board, piece):
        # đếm số lượng loại trong 13 type ứng với từng index của piece
        result = [0 for _ in range(12)]
        lst_turn = np.where(board == piece)
        idx_lst = [(lst_turn[0][i], lst_turn[1][i]) for i in range(len(lst_turn[0]))]

        for idx in idx_lst:
            temp =  count_type_piece(board,idx,piece)
            for i in range(len(result)):
                result[i]+=temp[i]
        return result

    def tinhdiem(board, piece):
        dif_piece = piece % 2 + 1
        # tính điểm cho điểm
        mark = 0
        count_main = count_continues_all(board,piece)
        count_dif = count_continues_all(board,dif_piece)
        mark_main = [1000,  600 ,800   , 200  ,600   ,60  ,  600 ,  450 , 150,80, 50, 10]
        mark_dif = [-5000, -5000, -5000, -1000, -5000, -60, -5000, -5000, -400, 80, 50, 10]
        for i in range(len(count_main)):
            mark = count_main[i]*mark_main[i]+count_dif[i]*mark_dif[i]
        return mark

    def minimax(board, piece, depth, alpha=-math.inf, beta=math.inf,step=(-1,-1)):
        result = (-1, -1)
        dif_piece = piece % 2 + 1
        if who_wins(board,piece):
            return step,100000
        if depth == 0:
            k = tinhdiem(board, piece)
            return step, k
        lst_idx_available = set(potential_step(board,piece))
        lst_idx_available = tuple(lst_idx_available)
        if not lst_idx_available:
            lst_idx_available = set(potential_step_for_1_piece(board,piece))
        lst_idx_available = tuple(lst_idx_available)
        if len(lst_idx_available) == 0: ### hết nước đi
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
                id_row = id_dif[0] + random.randint(-2, 2)
                id_col = id_dif[1] + random.randint(-2, 2)
                if id_row >= 0 and id_row < size and id_col >= 0 and id_col < size:
                    if id_row != id_dif[0] and id_col != id_dif[1]:
                        return id_row, id_col
########################################################################## MAIN FUNCTION
    if piece not in board:
        return gen_init(board,piece)
    else:
        return minimax(board, piece, depth, alpha=-math.inf, beta=math.inf)[0]

