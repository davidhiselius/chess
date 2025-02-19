import numpy as np
import pygame
from pygame.locals import *

class Piece:
    def __init__(self, color=None, type=None, x_pos=0, y_pos=0):
        self.color = color
        self.type = type
        self.x_pos = x_pos
        self.y_pos = y_pos

    def __str__(self):
        return f"{self.color}, {self.type}, position [x,y]: {self.x_pos},{self.y_pos}"

class Pawn(Piece):
    def __init__(self, color, type, position):
        super().__init__(color, type, position)


class Board:
    def __init__(self):
        position = None
        self.position = np.empty((8,8),dtype=Piece)
        for i in range(0,8):
            for j in range(0,8):
                self.position[i,j] = Piece()
        # Placing pawns:
        for i in range(0,8):
            self.position[6,i] = Piece('black','pawn')
            self.position[1,i] = Piece('white','pawn')
        # Placing rooks:
        for i in [0,7]:
            self.position[7,i] = Piece('black','rook')
            self.position[0,i] = Piece('white','rook')
        # Placing knights:
        for i in [1,6]:
            self.position[7,i] = Piece('black','knight')
            self.position[0,i] = Piece('white','knight')
        # Placing bishops:
        for i in [2,5]:
            self.position[7,i] = Piece('black','bishop')
            self.position[0,i] = Piece('white','bishop')
        # Placing queens:
        self.position[7,3] = Piece('black','queen')
        self.position[0,3] = Piece('white','queen')

        # Placing kings:
        self.position[7,4] = Piece('black','king')
        self.position[0,4] = Piece('white','queen')


    def add_piece(self, piece):
        self.position[piece.x_pos,piece.y_pos] = piece

    def remove_piece(self, piece):
        self.add_piece(Piece(None,None,piece.x_pos,piece.y_pos))
        
    def move_piece(self, piece, x_pos_new, y_pos_new):
        self.remove_piece(piece)
        moved_piece = piece
        moved_piece.x_pos = x_pos_new
        moved_piece.y_pos = y_pos_new
        self.add_piece(moved_piece)
        
    def get_piece(self,pos_x,pos_y):
        return f"Piece at position [{str(pos_x)},{str(pos_y)}]: (color: {self.position[pos_x,pos_y].color}, type: {self.position[pos_x,pos_y].type})"

    def __str__(self):
        disp_board = np.empty((8,8), dtype=Piece)
        for i in range(0,8):
            for j in range(0,8):
                disp_board[i,j] = f"{self.position[i,j].type}, {self.position[i,j].color}"
        return f"{disp_board}"


board = Board()

screen_height = int(640)
screen_width = int(640)
rect_width = int(80)
rect_height = int(80)

pygame.init()
screen = pygame.display.set_mode([screen_width, screen_height])
d_brown = pygame.Color(64, 40, 32)
l_brown = pygame.Color(179, 143, 96)

a = (1,3,5,7)
b = (0,2,4,6)

running = True
while running:

    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           running = False

    screen.fill(l_brown)

    rect = Rect((0,0),(rect_width,rect_height))
    for i in range(0,8):
            for j in range(0,8):
                if (i+j) % 2 != 0:
                    rect = Rect((i*rect_width,j*rect_height),(rect_width,rect_height))
                    pygame.draw.rect(screen,d_brown,rect)
    pygame.display.flip()

pygame.quit()
