import time
import numpy as np
import pygame
import sys
import math


########################################### add P1
from AGENT_RANDOM import agent_0
from GO_AGENT_1 import agent_1
from GO_AGENT_2 import agent_2
from GO_AGENT_3 import agent_3
from GO_AGENT_4 import agent_4
# lựa chọn HU - đánh tay, A0: Agent đúng luật, A1-A4: Agent minimax+alpha beta
player0 = "A1" # for turn 0 Black piece =1
player1 = "A3"  # for turn 1 White piece =2

def full_play(board):
    if len(np.where(board == 0)) == 0:
        return True
    return False
########################################### ending add P1


# initialize the pygame program
pygame.init()

# static variables
ROW_COUNT = 15
COL_COUNT = 15

# define screen size
BLOCKSIZE = 50 # individual grid
S_WIDTH = COL_COUNT * BLOCKSIZE # screen width
S_HEIGHT = ROW_COUNT * BLOCKSIZE # screen height
PADDING_RIGHT = 200 # for game menu
SCREENSIZE = (S_WIDTH + PADDING_RIGHT,S_HEIGHT)
RADIUS = 20 # game piece radius

# colors
Black = (0,0,0)
White = (255,255,255)
BROWN = (205,128,0)

# create a board array
def create_board(row, col):
    board = np.zeros((row,col))
    return board

# draw a board in pygame window
def draw_board(screen):
    for x in range(0,S_WIDTH,BLOCKSIZE):
        for y in range(0,S_HEIGHT,BLOCKSIZE):
            rect = pygame.Rect(x, y, BLOCKSIZE, BLOCKSIZE)
            pygame.draw.rect(screen,BROWN,rect)

    # draw inner grid lines
    # draw vertical lines
    for x in range(BLOCKSIZE // 2, S_WIDTH - BLOCKSIZE // 2 + BLOCKSIZE, BLOCKSIZE):
        line_start = (x, BLOCKSIZE // 2)
        line_end = (x,S_HEIGHT-BLOCKSIZE // 2)
        pygame.draw.line(screen, Black, line_start,line_end,2)

    # draw horizontal lines
    for y in range(BLOCKSIZE // 2, S_HEIGHT - BLOCKSIZE // 2 + BLOCKSIZE, BLOCKSIZE):
        line_start = (BLOCKSIZE // 2,y)
        line_end = (S_WIDTH-BLOCKSIZE // 2,y)
        pygame.draw.line(screen, Black, line_start,line_end,2)
    pygame.display.update()

# drop a piece
def drop_piece(board, row, col, piece):
    board[row][col] = piece

# draw a piece on board
def draw_piece(screen,board):
    # draw game pieces at mouse location
    for x in range(COL_COUNT):
        for y in range(ROW_COUNT):
            circle_pos = (x * BLOCKSIZE + BLOCKSIZE//2, y * BLOCKSIZE + BLOCKSIZE//2)
            if board[y][x] == 1:
                pygame.draw.circle(screen, Black, circle_pos, RADIUS)
            elif board[y][x] == 2:
                pygame.draw.circle(screen, White, circle_pos, RADIUS)
    pygame.display.update()

# check if it is a valid location
def is_valid_loc(board, row, col):
    return board[row][col] == 0

# victory decision
def who_wins(board, piece):
    # check for horizontal win
    for c in range(COL_COUNT - 4):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece\
                and board[r][c+4] == piece:
                return True

    # check for vertical win
    for c in range(COL_COUNT):
        for r in range(ROW_COUNT-4):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece\
                and board[r+4][c] == piece:
                return True

    # check for positively sloped diagonal wih
    for c in range(COL_COUNT-4):
        for r in range(4,ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece\
                and board[r-4][c+4] == piece:
                return True

    # check for negatively sloped diagonal win
    for c in range(COL_COUNT-4):
        for r in range(ROW_COUNT-4):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece\
                and board[r+4][c+4] == piece:
                return True


#######################################################

def main():
    # game variables
    glob_stage = 0
    game_over = False
    turn = 0 # turn == 0 for player 1, turn == 1 for player 2
    piece_1 = 1 # Black
    piece_2 = 2 # White
    piece = piece_1,piece_2
    player = player0, player1
    color = "Black", "White"
    # FPS
    FPS = 60
    frames_per_sec = pygame.time.Clock()
    # board 2D array
    board = create_board(ROW_COUNT,COL_COUNT)
    print(board)
    print(agent_0(board))
    # game screen
    SCREEN = pygame.display.set_mode(SCREENSIZE)
    SCREEN.fill(White)
    pygame.display.set_caption('Gomoku (Connet 5)')
    # font
    my_font = pygame.font.Font('freesansbold.ttf', 32)
    # text message
    label_1 = my_font.render('Black wins!', True, White, Black)
    label_2 = my_font.render('White wins!', True, White, Black)
    label = label_1,label_2
    # display the screen
    draw_board(SCREEN)

    #game loop
    while not game_over:
        glob_stage += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if player[turn] == "HU":  # Nếu là lượt của người chơi
            if pygame.mouse.get_pressed()[0]:  # Nút trái chuột đã được nhấn
                x_pos, y_pos = pygame.mouse.get_pos()
                col = int(math.floor(x_pos / BLOCKSIZE))
                row = int(math.floor(y_pos / BLOCKSIZE))

                # Xử lý đánh cờ của người chơi tại đây
                if is_valid_loc(board, row, col):
                    drop_piece(board, row, col, piece[turn])
                    draw_piece(SCREEN, board)

                    if who_wins(board, piece[turn]):
                        print(f'{color[turn]} wins!')
                        SCREEN.blit(label[turn], (280, 50))
                        pygame.display.update()
                        print(f" Lượt {glob_stage}")
                        game_over = True
                    if game_over:
                        pygame.time.wait(4000)
                    # increment turn
                    turn = (turn + 1) % 2
        elif player[turn] == "A0":  # Nếu là lượt của hàm agent_0
            # Đánh cờ bằng hàm agent_0 tại đây
            row, col = agent_0(board)  # Gọi hàm agent_0 để lấy vị trí đánh cờ
            if is_valid_loc(board, row, col):
                drop_piece(board, row, col, piece[turn])
                draw_piece(SCREEN, board)

                if who_wins(board, piece[turn]):
                    print(f'{color[turn]} wins!')
                    SCREEN.blit(label[turn], (280, 50))
                    pygame.display.update()
                    print(f" Lượt {glob_stage}")
                    game_over = True
                if game_over:
                    pygame.time.wait(4000)
                # increment turn
                turn = (turn + 1) % 2
                print(board)
            time.sleep(1)
        elif player[turn] == "A1":  # Nếu là lượt của hàm agent_1
            # Đánh cờ bằng hàm agent_1 tại đây
            row, col = agent_1(board,turn)  # Gọi hàm agent_1 để lấy vị trí đánh cờ
            if is_valid_loc(board, row, col):
                drop_piece(board, row, col, piece[turn])
                draw_piece(SCREEN, board)

                if who_wins(board, piece[turn]):
                    print(f'{color[turn]} wins!')
                    SCREEN.blit(label[turn], (280, 50))
                    pygame.display.update()
                    print(f" Lượt {glob_stage}")
                    game_over = True
                if game_over:
                    pygame.time.wait(1000)
                # increment turn
                turn = (turn+1) % 2
                print(board)
            time.sleep(1)
        elif player[turn] == "A2":  # Nếu là lượt của hàm agent_2
            # Đánh cờ bằng hàm agent_2 tại đây
            row, col = agent_2(board,turn)  # Gọi hàm agent_2 để lấy vị trí đánh cờ
            if is_valid_loc(board, row, col):
                drop_piece(board, row, col, piece[turn])
                draw_piece(SCREEN, board)

                if who_wins(board, piece[turn]):
                    print(f'{color[turn]} wins!')
                    SCREEN.blit(label[turn], (280, 50))
                    pygame.display.update()
                    print(f" Lượt {glob_stage}")
                    game_over = True
                if game_over:
                    pygame.time.wait(1000)
                # increment turn
                turn = (turn+1) % 2
                print(board)
            time.sleep(1)
        elif player[turn] == "A3":  # Nếu là lượt của hàm agent_3
            # Đánh cờ bằng hàm agent_3 tại đây
            row, col = agent_3(board,turn)  # Gọi hàm agent_3 để lấy vị trí đánh cờ
            if is_valid_loc(board, row, col):
                drop_piece(board, row, col, piece[turn])
                draw_piece(SCREEN, board)

                if who_wins(board, piece[turn]):
                    print(f'{color[turn]} wins!')
                    SCREEN.blit(label[turn], (280, 50))
                    pygame.display.update()
                    print(f" Lượt {glob_stage}")
                    game_over = True
                if game_over:
                    pygame.time.wait(1000)
                # increment turn
                turn = (turn+1) % 2
                print(board)
            time.sleep(1)
        elif player[turn] == "A4":  # Nếu là lượt của hàm agent_4
            # Đánh cờ bằng hàm agent_4 tại đây
            row, col = agent_4(board,turn)  # Gọi hàm agent_4 để lấy vị trí đánh cờ
            if is_valid_loc(board, row, col):
                drop_piece(board, row, col, piece[turn])
                draw_piece(SCREEN, board)

                if who_wins(board, piece[turn]):
                    print(f'{color[turn]} wins!')
                    SCREEN.blit(label[turn], (280, 50))
                    pygame.display.update()
                    print(f" Lượt {glob_stage}")
                    game_over = True
                if game_over:
                    pygame.time.wait(1000)
                # increment turn
                turn = (turn+1) % 2
                print(board)
            time.sleep(1)
        frames_per_sec.tick(FPS)

if __name__ == '__main__':
    main()
