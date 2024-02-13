import sys
import pygame
import numpy as np

from constants import *

# PYGAME SETUP
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TIC TAC TOE AI')
screen.fill(BG_COLOR)

class Board:
    def __init__(self):
        self.squares = np.zeros((ROWS, COLS))

    def mark_square(self, row, col, player):
        self.squares[row][col] = player

    def empty_square(self, row, col):
        return self.squares[row][col] == 0

class Game:
    def __init__(self):
        self.board = Board()
        self.player = 1 # 1 - cross # 2 - circle
        self.show_lines()

    def show_lines(self):
        # Vertical
        pygame.draw.line(screen, LINE_COLOR, (SQSIZE, 0), (SQSIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (WIDTH - SQSIZE, 0), (WIDTH - SQSIZE, HEIGHT), LINE_WIDTH)

        # Horizontal
        pygame.draw.line(screen, LINE_COLOR, (0, SQSIZE), (WIDTH, SQSIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0, HEIGHT - SQSIZE), (WIDTH, HEIGHT - SQSIZE), LINE_WIDTH)
    
    def draw_fig(self, row, col):
        if self.player == 1:
            # Draw cross
            # Desc line
            start_desc = (col * SQSIZE + OFFSET, row * SQSIZE + OFFSET) 
            end_desc = (col * SQSIZE + SQSIZE - OFFSET, row * SQSIZE + SQSIZE - OFFSET)
            pygame.draw.line(screen, CROSS_COLOR, start_desc, end_desc, CROSS_WIDTH)
            # Asc line
            start_asc = (col * SQSIZE + OFFSET, row * SQSIZE + SQSIZE - OFFSET) 
            end_asc = (col * SQSIZE + SQSIZE - OFFSET, row * SQSIZE + OFFSET)
            pygame.draw.line(screen, CROSS_COLOR, start_asc, end_asc, CROSS_WIDTH)

        elif self.player == 2:
            # Draw circle
            center = (col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2)
            pygame.draw.circle(screen, CIRCLE_COLOR, center, RADIUS, CIRCLE_WIDTH)

    def next_turn(self):
        self.player = self.player %2 + 1 

def main():
    # Object
    game = Game()
    board = game.board

    # Mainloop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Convert from pixels to row and columns
                pos = event.pos
                row = pos[1] // SQSIZE
                col = pos[0] // SQSIZE

                if board.empty_square(row, col):
                    game.board.mark_square(row, col, game.player)
                    game.draw_fig(row, col)
                    game.next_turn()

        pygame.display.update()

main()