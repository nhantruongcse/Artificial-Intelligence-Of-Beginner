#import resource
#import time
from sys import getsizeof
import tracemalloc
import numpy as np
from collections.abc import Mapping, Container

from sys import getsizeof

from memory_profiler import profile
from memory_profiler import memory_usage

clear =[  [0 , 0, 0, 0, 0, 0, 0, 0, 0],
          [0 , 0, 0, 0, 0, 0, 0, 0, 0],
          [0 , 0, 0, 0, 0, 0, 0, 0, 0],
          [0 , 0, 0, 0, 0, 0, 0, 0, 0],
          [0 , 0, 0, 0, 0, 0, 0, 0, 0],
          [0 , 0, 0, 0, 0, 0, 0, 0, 0],
          [0 , 0, 0, 0, 0, 0, 0, 0, 0],
          [0 , 0, 0, 0, 0, 0, 0, 0, 0],
          [0 , 0, 0, 0, 0, 0, 0, 0, 0]]

game =[   [7 , 5, 0, 0, 0, 0, 0, 8, 3],
          [0 , 0, 0, 9, 0, 8, 0, 0, 0],
          [0 , 9, 0, 0, 4, 0, 0, 1, 0],
          [0 , 0, 5, 8, 0, 2, 3, 0, 0],
          [0 , 8, 0, 0, 0, 0, 0, 5, 0],
          [0 , 0, 9, 4, 0, 7, 8, 0, 0],
          [0 , 2, 0, 0, 1, 0, 0, 4, 0],
          [0 , 0, 0, 2, 0, 6, 0, 0, 0],
          [9 , 1, 0, 0, 0, 0, 0, 3, 8]]

data = [[8, 0, 1, 3, 2, 5, 6, 0, 4],
        [5, 0, 2, 6, 0, 0, 0, 1, 7],
        [3, 6, 0, 1, 7, 4, 8, 2, 0],
        [0, 1, 3, 5, 8, 0, 4, 0, 9],
        [9, 5, 0, 4, 1, 7, 2, 3, 6],
        [7, 0, 4, 9, 0, 6, 0, 8, 0],
        [2, 0, 6, 7, 4, 1, 9, 0, 3],
        [0, 3, 0, 2, 6, 9, 0, 4, 8],
        [4, 9, 7, 8, 0, 0, 1, 6, 0]]

game = np.asarray(game)

def check_solved(board):
  row = [set(i) for i in board]
  col = []
  for i in range(9):
    temp=[ board[j,i] for j in range(9)]
    col.append(set(temp))
  for i in range(9):
    if len(row[i]) !=9 or len (col[i]) !=9: return False
    if (0 in row[i]) or (0 in col[i]): return False
  return True


def list_number_for_search(data_board, row, col):
    lst = []
    row_lst = data_board[row, :].flatten().tolist()
    col_lst = data_board[:, col].flatten().tolist()
    row_block = row - row % 3
    col_block = col - col % 3
    block_lst = data_board[row_block:row_block + 3, col_block:col_block + 3].flatten().tolist()
    for number in range(1, 10):
        if (number not in row_lst) and (number not in col_lst) and (number not in block_lst):
            lst.append((number))
    return lst


def list_empty_cell(data):
    lst = []
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i, j] == 0:
                lst.append((i, j))
    return lst

def heuristic_select_cel(data):
    lst_empty_cell = list_empty_cell(data)
    if len(lst_empty_cell) == 1:
        return lst_empty_cell[0]
    if len(lst_empty_cell)==0:
        return None
    counting_list = [0 for _ in range(len(lst_empty_cell))]
    for index in range(len(lst_empty_cell)):
        row = lst_empty_cell[index][0]
        col = lst_empty_cell[index][1]
        counting_list[index] = len(list_number_for_search(data, row, col))
    min_valid = min(counting_list)
    id = counting_list.index(min_valid)
    return lst_empty_cell[id]

def check_valid_num(data, row, col, number):  # kiểm tra nếu đặt number tại vị trí (row,col) có hợp lệ không
    row_lst = data[row, :].flatten().tolist()
    col_lst = data[:, col].flatten().tolist()
    id_box_r = row - row % 3
    id_box_c = col - col % 3
    box = data[id_box_r:id_box_r + 3, id_box_c:id_box_c + 3].flatten().tolist()
    if row_lst.count(number) == 0 and col_lst.count(number) == 0 and box.count(
            number) == 0:  # kiểm tra row, col, box chưa xuất hiện number
        return True
    else:
        return False
@profile()
def solve_sudoku(data):
    empty_cell = heuristic_select_cel(data)
    if empty_cell is None:   # Tất cả các ô đã được fill chính xác
      if check_solved(data):
        print("SOLUTION FOUND: ")
        return data
      else:
        print("None")
        return None
    row, col = empty_cell
    for num in range(1, 10): #thử giá trị từ 1 đến 9
        if check_valid_num(data, row, col, num):
            data[row][col] = num
            print("Next step is: ")
            print(data)
            result = solve_sudoku(data)
            if result is not None:
                return result
            # Nếu không thể giải tiếp, quay lại giá trị 0 cho ô
            data[row][col] = 0
            print("IT'S NOT WAY TO SOLUTION- SET BOARD BACK: ")
            print(data)
@profile()
def main(board):
    return solve_sudoku(board)


main(game)

#
# mem_usage = memory_usage((main(game)))
# print("MAX memory   ",max(mem_usage))

#x= '1234567'
#
#print(getsizeof(main(game)))
clear2 = [  [8, 7, 1, 3, 2, 5, 6, 9, 4],
            [5, 4, 2, 6, 9, 8, 3, 1, 7],
            [3, 6, 9, 1, 7, 4, 8, 2, 5],
            [6, 1, 3, 5, 8, 2, 4, 7, 9],
            [9, 5, 8, 4, 1, 7, 2, 3, 6],
            [7, 2, 4, 9, 3, 6, 5, 8, 1],
            [2, 8, 6, 7, 4, 1, 9, 5, 3],
            [1, 3, 5, 2, 6, 9, 7, 4, 8],
            [4, 9, 7, 8, 5, 3, 1, 6, 2]]
print(getsizeof(clear2))