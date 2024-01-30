from sys import getsizeof
from memory_profiler import profile
import tracemalloc
import numpy as np
import time

############################### TESTCASE
clear =[[0 , 0, 0, 0, 0, 0, 0, 0, 0],
        [0 , 0, 0, 0, 0, 0, 0, 0, 0],
        [0 , 0, 0, 0, 0, 0, 0, 0, 0],
        [0 , 0, 0, 0, 0, 0, 0, 0, 0],
        [0 , 0, 0, 0, 0, 0, 0, 0, 0],
        [0 , 0, 0, 0, 0, 0, 0, 0, 0],
        [0 , 0, 0, 0, 0, 0, 0, 0, 0],
        [0 , 0, 0, 0, 0, 0, 0, 0, 0],
        [0 , 0, 0, 0, 0, 0, 0, 0, 0]]

game_ba1=[[0 , 1, 0, 0, 0, 7, 6, 3, 0],
          [7 , 0, 2, 0, 6, 0, 0, 1, 9],
          [0 , 9, 0, 0, 0, 0, 0, 7, 0],
          [0 , 0, 0, 0, 0, 0, 0, 0, 3],
          [0 , 5, 0, 0, 9, 4, 0, 0, 2],
          [3 , 0, 0, 0, 1, 0, 0, 5, 0],
          [2 , 0, 0, 0, 0, 0, 0, 8, 0],
          [9 , 3, 7, 0, 0, 6, 5, 0, 0],
          [0 , 8, 0, 1, 7, 0, 0, 0, 0]]

game_ea1=[[0 , 7, 0, 0, 1, 0, 0, 2, 0],
          [0 , 0, 0, 0, 0, 0, 0, 0, 0],
          [2 , 6, 0, 0, 0, 0, 0, 1, 4],
          [0 , 0, 2, 1, 0, 4, 6, 0, 0],
          [0 , 0, 0, 0, 0, 0, 0, 0, 0],
          [0 , 8, 0, 3, 2, 9, 0, 5, 0],
          [3 , 0, 0, 4, 0, 2, 0, 0, 5],
          [6 , 0, 0, 0, 0, 0, 0, 0, 8],
          [7 , 5, 0, 8, 0, 3, 0, 4, 1]]

game_in1=[[0 , 5, 6, 1, 7, 0, 0, 0, 0],
          [9 , 0, 1, 0, 0, 0, 7, 0, 0],
          [7 , 4, 0, 0, 9, 6, 0, 8, 0],
          [5 , 0, 0, 0, 0, 1, 3, 0, 0],
          [6 , 0, 8, 0, 0, 0, 5, 0, 9],
          [0 , 0, 9, 5, 0, 0, 0, 0, 1],
          [0 , 9, 0, 6, 5, 0, 0, 1, 7],
          [0 , 0, 5, 0, 0, 0, 2, 0, 6],
          [0 , 0, 0, 0, 1, 2, 9, 5, 0]]

game_ad1=[[3 , 0, 7, 4, 0, 0, 0, 0, 0],
          [0 , 8, 0, 1, 0, 0, 0, 0, 0],
          [4 , 0, 0, 0, 9, 0, 6, 0, 0],
          [5 , 1, 0, 6, 0, 8, 0, 0, 0],
          [0 , 0, 4, 0, 0, 0, 8, 0, 0],
          [0 , 0, 0, 2, 0, 7, 0, 1, 6],
          [0 , 0, 3, 0, 6, 0, 0, 0, 5],
          [0 , 0, 0, 0, 0, 4, 0, 2, 0],
          [0 , 0, 0, 0, 0, 2, 1, 0, 8]]

game_ex1=[[6 , 0, 0, 7, 0, 1, 0, 0, 4],
          [0 , 2, 0, 3, 0, 8, 0, 1, 0],
          [0 , 0, 0, 5, 4, 6, 0, 0, 0],
          [3 , 7, 1, 0, 0, 0, 2, 6, 9],
          [0 , 0, 8, 0, 0, 0, 3, 0, 0],
          [4 , 6, 9, 0, 0, 0, 5, 8, 1],
          [0 , 0, 0, 1, 3, 5, 0, 0, 0],
          [0 , 3, 0, 9, 0, 7, 0, 5, 0],
          [5 , 0, 0, 4, 0, 2, 0, 0, 3]]

game_ex2=[[0 , 0, 0, 0, 0, 0, 2, 0, 0],
          [0 , 6, 2, 0, 8, 5, 7, 3, 0],
          [0 , 4, 0, 0, 6, 0, 1, 0, 0],
          [0 , 8, 0, 0, 0, 3, 0, 0, 5],
          [0 , 0, 0, 1, 9, 0, 0, 0, 4],
          [0 , 7, 0, 0, 0, 4, 0, 1, 0],
          [3 , 0, 4, 0, 0, 0, 8, 0, 0],
          [0 , 5, 0, 0, 0, 0, 0, 2, 0],
          [0 , 0, 0, 0, 0, 0, 0, 0, 7]]

game_el1=[[0 , 3, 0, 9, 0, 0, 7, 0, 0],
          [0 , 0, 0, 0, 6, 0, 5, 0, 3],
          [5 , 6, 0, 3, 0, 0, 0, 0, 0],
          [0 , 0, 0, 0, 4, 0, 8, 0, 9],
          [0 , 8, 0, 5, 0, 1, 0, 7, 0],
          [9 , 0, 2, 0, 3, 0, 0, 0, 0],
          [0 , 0, 0, 0, 0, 3, 0, 1, 7],
          [7 , 0, 4, 0, 1, 0, 0, 0, 0],
          [0 , 0, 3, 0, 0, 7, 0, 5, 0]]

####################################### CODE
def find_empty_cell(data):
  for i in range(len(data)):
    for j in range(len(data[0])):
      if data[i,j]==0:
        return (i,j)
  return None

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

def check_valid_num(data, row,col, number): #kiểm tra nếu đặt number tại vị trí (row,col) có hợp lệ không
  row_lst = data[row,:].flatten().tolist()
  col_lst = data[:,col].flatten().tolist()
  id_box_r = row-row%3
  id_box_c = col-col%3
  box = data[id_box_r:id_box_r+3,id_box_c:id_box_c+3].flatten().tolist()
  if row_lst.count(number)==0 and col_lst.count(number)==0 and box.count(number)==0: #kiểm tra row, col, box chưa xuất hiện number
    return True
  else:
    return False

def solve_sudoku(data):
    empty_cell = find_empty_cell(data)
    if empty_cell is None:   # Tất cả các ô đã được fill chính xác
      if check_solved(data):
        print("SOLUTION FOUND: ")
        print(data)
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

start = time.time()
tracemalloc.clear_traces()
tracemalloc.start()
solve_sudoku(np.asarray(game_ad1))
print(f"Bộ nhớ tối đa sử dụng: {tracemalloc.get_traced_memory()[1]} bytes")
tracemalloc.stop()
print(f"Thời gian chạy là {time.time() - start} giây ")


## COUNTING ZERO CELL
# lst = [game_ba1,game_el1,game_ea1,game_in1,game_ad1,game_ex1,game_el1]
# counting = [81 - np.count_nonzero(np.asarray(i)) for i in lst]
# print(counting)
