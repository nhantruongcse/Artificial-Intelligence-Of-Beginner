import numpy as np
import random
def agent_0(board) :
    # đổi board thành 2 giá trị 0 và 1 (1: có thể chọn; 0: không thể chọn)
    board_empty = [[1 if i == 0 else 0 for i in row] for row in board]
    lst = np.nonzero(board_empty)
    # lấy random 1 vị trí
    k = random.randrange(len(lst[0])-1)
    return lst[1][k],lst[0][k]

