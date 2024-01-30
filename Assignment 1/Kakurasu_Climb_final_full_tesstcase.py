import numpy as np
import time
import tracemalloc
from itertools import combinations


############################################# TESTCASE
###################     test 4
board4_e_1 =[   [0,0,0,0,4],
                [0,0,0,0,3],
                [0,0,0,0,4],
                [0,0,0,0,1],
                [7,2,1,3,0]]

board4_e_2 =[   [0,0,0,0,6],
                [0,0,0,0,6],
                [0,0,0,0,8],
                [0,0,0,0,6],
                [8,7,8,5,0]]

board4_h_1 =[   [0,0,0,0,4],
                [0,0,0,0,7],
                [0,0,0,0,6],
                [0,0,0,0,1],
                [5,3,3,5,0]]

board4_h_2 =[   [0,0,0,0,3],
                [0,0,0,0,7],
                [0,0,0,0,3],
                [0,0,0,0,7],
                [9,9,1,6,0]]

size4 = 4

###################     test 5
board5_e_1 =[   [ 0, 0, 0, 0, 0, 8],
                [ 0, 0, 0, 0, 0, 13],
                [ 0, 0, 0, 0, 0, 8],
                [ 0, 0, 0, 0, 0, 13],
                [ 0, 0, 0, 0, 0, 8],
                [ 14,3,12, 11,10,0]]

board5_e_2 =[   [ 0, 0, 0, 0, 0, 10],
                [ 0, 0, 0, 0, 0, 5],
                [ 0, 0, 0, 0, 0, 14],
                [ 0, 0, 0, 0, 0, 12],
                [ 0, 0, 0, 0, 0, 6],
                [ 5,12, 3, 13,10,0]]

board5_h_1 =[   [ 0, 0, 0, 0, 0, 4],
                [ 0, 0, 0, 0, 0, 7],
                [ 0, 0, 0, 0, 0,14],
                [ 0, 0, 0, 0, 0,12],
                [ 0, 0, 0, 0, 0, 9],
                [ 4,14, 8, 13, 9,0]]

board5_h_2 =[   [ 0, 0, 0, 0, 0, 12],
                [ 0, 0, 0, 0, 0, 6],
                [ 0, 0, 0, 0, 0, 10],
                [ 0, 0, 0, 0, 0, 4],
                [ 0, 0, 0, 0, 0,12],
                [ 11,11, 5, 13, 6,0]]
size5 = 5

###################     test 6
board6_e_1 =[   [0 , 0, 0, 0, 0, 0, 5],
                [0 , 0, 0, 0, 0, 0, 17],
                [0 , 0, 0, 0, 0, 0, 17],
                [0 , 0, 0, 0, 0, 0, 18],
                [0 , 0, 0, 0, 0, 0,14],
                [0 , 0, 0, 0, 0, 0,14],
                [14 ,10,17, 9,15,20, 0]]

board6_e_2 =[   [0 , 0, 0, 0, 0, 0, 15],
                [0 , 0, 0, 0, 0, 0, 12],
                [0 , 0, 0, 0, 0, 0, 12],
                [0 , 0, 0, 0, 0, 0, 13],
                [0 , 0, 0, 0, 0, 0,20],
                [0 , 0, 0, 0, 0, 0,17],
                [16 ,20,14, 12,15,18, 0]]

board6_h_1 =[   [0 , 0, 0, 0, 0, 0, 18],
                [0 , 0, 0, 0, 0, 0, 14],
                [0 , 0, 0, 0, 0, 0, 13],
                [0 , 0, 0, 0, 0, 0, 7],
                [0 , 0, 0, 0, 0, 0, 6],
                [0 , 0, 0, 0, 0, 0,10],
                [17, 5, 1, 7,17,10, 0]]

board6_h_2 =[   [0 , 0, 0, 0, 0, 0, 7],
                [0 , 0, 0, 0, 0, 0, 16],
                [0 , 0, 0, 0, 0, 0, 9],
                [0 , 0, 0, 0, 0, 0, 3],
                [0 , 0, 0, 0, 0, 0,10],
                [0 , 0, 0, 0, 0, 0,16],
                [13,10,5,12,16, 8, 0]]
size6 = 6

###################     test 7
board7_e_1 =[   [0 , 0, 0, 0, 0, 0, 0, 15],
                [0 , 0, 0, 0, 0, 0, 0, 13],
                [0 , 0, 0, 0, 0, 0, 0, 17],
                [0 , 0, 0, 0, 0, 0, 0, 6],
                [0 , 0, 0, 0, 0, 0, 0,7],
                [0 , 0, 0, 0, 0, 0, 0,15],
                [0 , 0, 0, 0, 0, 0, 0,13],
                [6 , 1,8, 5,6,23, 16, 0]]

board7_e_2 =[   [0 , 0, 0, 0, 0, 0, 0, 18],
                [0 , 0, 0, 0, 0, 0, 0, 21],
                [0 , 0, 0, 0, 0, 0, 0, 23],
                [0 , 0, 0, 0, 0, 0, 0, 21],
                [0 , 0, 0, 0, 0, 0, 0,23],
                [0 , 0, 0, 0, 0, 0, 0,14],
                [0 , 0, 0, 0, 0, 0, 0,23],
                [21 ,19,24,24,5,22, 27, 0]]

board7_h_1 =[   [0 , 0, 0, 0, 0, 0, 0,24],
                [0 , 0, 0, 0, 0, 0, 0,22],
                [0 , 0, 0, 0, 0, 0, 0, 4],
                [0 , 0, 0, 0, 0, 0, 0, 14],
                [0 , 0, 0, 0, 0, 0, 0,19],
                [0 , 0, 0, 0, 0, 0, 0,21],
                [0 , 0, 0, 0, 0, 0, 0,20],
                [17 , 14,17,19,21,25,10,0]]

board7_h_2 =[   [0 , 0, 0, 0, 0, 0, 0, 20],
                [0 , 0, 0, 0, 0, 0, 0, 18],
                [0 , 0, 0, 0, 0, 0, 0, 6],
                [0 , 0, 0, 0, 0, 0, 0, 12],
                [0 , 0, 0, 0, 0, 0, 0,15],
                [0 , 0, 0, 0, 0, 0, 0,22],
                [0 , 0, 0, 0, 0, 0, 0,20],
                [4 ,18,15,25,17,25, 7, 0]]
size7= 7
###################     test 8
board8_e_1 =[   [0 , 0, 0, 0, 0, 0, 0, 0, 15],
                [0 , 0, 0, 0, 0, 0, 0, 0, 2],
                [0 , 0, 0, 0, 0, 0, 0, 0, 7],
                [0 , 0, 0, 0, 0, 0, 0, 0, 7],
                [0 , 0, 0, 0, 0, 0, 0, 0,3],
                [0 , 0, 0, 0, 0, 0, 0, 0,19],
                [0 , 0, 0, 0, 0, 0, 0, 0,13],
                [0 , 0, 0, 0, 0, 0, 0, 0,18],
                [7 , 3,14, 16,14,15, 7, 13, 0]]

board8_e_2 =[   [0 , 0, 0, 0, 0, 0, 0, 0, 24],
                [0 , 0, 0, 0, 0, 0, 0, 0, 35],
                [0 , 0, 0, 0, 0, 0, 0, 0, 33],
                [0 , 0, 0, 0, 0, 0, 0, 0, 34],
                [0 , 0, 0, 0, 0, 0, 0, 0,35],
                [0 , 0, 0, 0, 0, 0, 0, 0,19],
                [0 , 0, 0, 0, 0, 0, 0, 0,27],
                [0 , 0, 0, 0, 0, 0, 0, 0,31],
                [16 ,25,33,29,22,29, 30,35, 0]]

board8_h_1 =[   [0 , 0, 0, 0, 0, 0, 0, 0,14],
                [0 , 0, 0, 0, 0, 0, 0, 0,11],
                [0 , 0, 0, 0, 0, 0, 0, 0,12],
                [0 , 0, 0, 0, 0, 0, 0, 0,16],
                [0 , 0, 0, 0, 0, 0, 0, 0,33],
                [0 , 0, 0, 0, 0, 0, 0, 0,18],
                [0 , 0, 0, 0, 0, 0, 0, 0,18],
                [0 , 0, 0, 0, 0, 0, 0, 0,24],
                [23 ,21,19,31,26,25, 7, 19, 0]]

board8_h_2 =[   [0 , 0, 0, 0, 0, 0, 0, 0,14],
                [0 , 0, 0, 0, 0, 0, 0, 0, 3],
                [0 , 0, 0, 0, 0, 0, 0, 0,24],
                [0 , 0, 0, 0, 0, 0, 0, 0, 18],
                [0 , 0, 0, 0, 0, 0, 0, 0,34],
                [0 , 0, 0, 0, 0, 0, 0, 0,11],
                [0 , 0, 0, 0, 0, 0, 0, 0,27],
                [0 , 0, 0, 0, 0, 0, 0, 0,20],
                [12,30,26,15,9,19,28,23, 0]]

size8= 8
###################     test 9
board9_e_1 =[   [0 , 0, 0, 0, 0, 0, 0, 0, 0,44],
                [0 , 0, 0, 0, 0, 0, 0, 0, 0, 39],
                [0 , 0, 0, 0, 0, 0, 0, 0, 0, 26],
                [0 , 0, 0, 0, 0, 0, 0, 0, 0, 36],
                [0 , 0, 0, 0, 0, 0, 0, 0, 0,39],
                [0 , 0, 0, 0, 0, 0, 0, 0, 0,41],
                [0 , 0, 0, 0, 0, 0, 0, 0, 0,33],
                [0 , 0, 0, 0, 0, 0, 0, 0, 0,36],
                [0 , 0, 0, 0, 0, 0, 0, 0, 0, 36],
                [29 ,40,42,30,34,36,42,37,33, 0]]

board9_e_2 =[   [0 , 0, 0, 0, 0, 0, 0, 0, 0, 5],
                [0 , 0, 0, 0, 0, 0, 0, 0, 0, 11],
                [0 , 0, 0, 0, 0, 0, 0, 0, 0, 9],
                [0 , 0, 0, 0, 0, 0, 0, 0, 0, 2],
                [0 , 0, 0, 0, 0, 0, 0, 0, 0,27],
                [0 , 0, 0, 0, 0, 0, 0, 0, 0,8],
                [0 , 0, 0, 0, 0, 0, 0, 0, 0,1],
                [0 , 0, 0, 0, 0, 0, 0, 0, 0,9],
                [0 , 0, 0, 0, 0, 0, 0, 0, 0, 18],
                [12,10,7, 5,22,11, 14, 5, 11, 0]]

board9_h_1 =[   [0 , 0, 0, 0, 0, 0, 0, 0, 0, 9],
                [0 , 0, 0, 0, 0, 0, 0, 0, 0, 18],
                [0 , 0, 0, 0, 0, 0, 0, 0, 0, 33],
                [0 , 0, 0, 0, 0, 0, 0, 0, 0, 41],
                [0 , 0, 0, 0, 0, 0, 0, 0, 0,26],
                [0 , 0, 0, 0, 0, 0, 0, 0, 0,17],
                [0 , 0, 0, 0, 0, 0, 0, 0, 0,28],
                [0 , 0, 0, 0, 0, 0, 0, 0, 0,13],
                [0 , 0, 0, 0, 0, 0, 0, 0, 0, 18],
                [44 ,15,20,19,13,29,13,42,14, 0]]

board9_h_2 =[   [0 , 0, 0, 0, 0, 0, 0, 0, 0, 17],
                [0 , 0, 0, 0, 0, 0, 0, 0, 0, 22],
                [0 , 0, 0, 0, 0, 0, 0, 0, 0, 18],
                [0 , 0, 0, 0, 0, 0, 0, 0, 0, 17],
                [0 , 0, 0, 0, 0, 0, 0, 0, 0,42],
                [0 , 0, 0, 0, 0, 0, 0, 0, 0,40],
                [0 , 0, 0, 0, 0, 0, 0, 0, 0,39],
                [0 , 0, 0, 0, 0, 0, 0, 0, 0,23],
                [0 , 0, 0, 0, 0, 0, 0, 0, 0, 10],
                [24,27,35,29,14,24,42,23,21, 0]]

size9 = 9

##################################################### CODE
def get_value_right(board, row, col):
    if board[row][col] == 1:
        return col + 1
    else:
        return 0
def get_value_bottom(board, row, col):
    if board[row][col] == 1:
        return row + 1
    else:
        return 0
def check_final(board, size):
    for row in range(0, size):
        sum_row = 0
        for col in range(0, size):
            sum_row += get_value_right(board, row, col)
        if sum_row != board[row][size]:
            return False
    for col in range(0, size):
        sum_col = 0
        for row in range(0, size):
            sum_col += get_value_bottom(board, row, col)
        if sum_col != board[size][col]:
            return False
    return True
def check_sum(target, set_lst):
    if set_lst is None: return False
    else:
        if sum(set_lst) == target: return True
        return False
def valid_combination(target,size,lst):
    result =[]
    if len(lst)==1: return result
    valid_num = lst[0]
    picked_num = lst[1]
    if len(valid_num)==0: return result

    for i in range(1,size):
        temp_lst = list(combinations(valid_num,i))
        for j in temp_lst:
            if not check_sum(target,j): continue
            get = True
            for number in picked_num:
                if number not in j:
                    get = False
                    break
            if get:
                result.append(j)
    return result

def get_list_number_available_row(board,size,row):
    lst = []
    picked_lst= []
    # check complete row
    sum_row=0
    for j in range(size):
      if board[row][j]==1: sum_row+= j+1
    if sum_row == board[row][size]: return [[],[]]

    #with not complete row

    for i in range(size):
        if board[row][i]!=-1:
            lst.append(i+1)
    # lists number must have:
    for i in range(size):
        if board[row][i]==1:
            picked_lst.append(i+1)
    return [lst,picked_lst]

def get_list_number_available_col(board,size,col):
    lst = []
    picked_lst= []
    # check complete col
    sum_col=0
    for j in range(size):
      if board[j][col]==1: sum_col+= j+1
    if sum_col == board[size][col]: return [[],[]]

    #with not complete col
    for i in range(size):
        if board[i][col]!=-1:
            lst.append(i+1)
    # lists number must have:
    for i in range(size):
        if board[i][col]==1:
            picked_lst.append(i+1)
    return [lst, picked_lst]

def select_where_to_action(board,size):
    row_number = [get_list_number_available_row(board,size,row) for row in range(size)]
    col_number = [get_list_number_available_col(board,size,col) for col in range(size)]
    row_lst_combination =[]
    col_lst_combination=[]
    for i in range(size):
        temp_row_lst = valid_combination(board[i][size],size,row_number[i])
        row_lst_combination.append(temp_row_lst)
        temp_col_lst = valid_combination(board[size][i],size,col_number[i])
        col_lst_combination.append(temp_col_lst)
    row_count_combi = [len(i) for i in row_lst_combination]
    col_count_combi = [len(i) for i in col_lst_combination]
    for i in range(size):
        if row_count_combi[i]==0: row_count_combi[i]=size+1
        if col_count_combi[i]==0: col_count_combi[i]=size+1
    min_row = min(row_count_combi)
    min_col = min(col_count_combi)
    if min_col== size+1: return None
    if min_row <= min_col:
        indx = row_count_combi.index(min_row)
        return ('row',indx,row_lst_combination[indx])
    else:
        indx = col_count_combi.index(min_col)
        return ('col',indx,col_lst_combination[indx])

def solve(board, size):
    if check_final(board, size):
        return board
    info = select_where_to_action(board,size)
    if info is None: return None
    print("CAC TO HOP CO THE CHON O ",info[0]," ",info[1]," LA ",info[2])
    if info[0] == 'row':
        row = info[1]
        lst = info[2]
        for element in lst:
            ori_mark = [i for i in range(size) if board[row][i] == -1]
            ori_pick = [i for i in range(size) if board[row][i] == 1]
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  action with @@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ", element)
            for i in range(size):
              if i+1 in element: board[row][i]=1
              else: board[row][i]=-1
            print("NEXT STEP IS")
            print(np.asarray(board))

            if solve(board,size) is None:
                 print("IT'S NOT WAY TO SOLUTION- SET BOARD BACK: ")
                 for i in range(size):
                    if i in ori_mark:
                        board[row][i]=-1
                    else:
                        if i not in ori_pick:
                            board[row][i]=0
                 print(np.asarray(board))
            else: return solve(board,size)
    else: # action by column
        col = info[1]
        lst = info[2]

        for element in lst:
            ori_mark = [i for i in range(size) if board[i][col] == -1]
            ori_pick = [i for i in range(size) if board[i][col] == 1]

            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  action with @@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ", element)
            for i in range(size):
              if i+1 in element: board[i][col]=1
              else: board[i][col]=-1
            print("NEXT STEP IS")
            print(np.asarray(board))

            if solve(board,size) is None:
                print("IT'S NOT WAY TO SOLUTION- SET BOARD BACK: ")
                for i in range(size):
                    if i in ori_mark:
                        board[i][col]=-1
                    else:
                        if i not in ori_pick:
                            board[i][col]=0
                print(np.asarray(board))
            else: return solve(board,size)
def main(board, size):
    result = solve(board, size)
    if result is None:
        print("NO SOLUTION")
    else:
        print("SOLUTION IS")
        print(np.asarray(board))
###########################################################################

start = time.time()
tracemalloc.clear_traces()
tracemalloc.start()
main(board9_e_1,size9)
print(f"Bộ nhớ tối đa sử dụng: {tracemalloc.get_traced_memory()[1]} bytes")
tracemalloc.stop()
print(f"Thời gian chạy là {time.time()-start} giây ")
