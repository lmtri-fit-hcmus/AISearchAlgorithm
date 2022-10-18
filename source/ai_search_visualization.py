#source code to make video display:
#https://www.youtube.com/watch?v=JtiK0DOeI4A
from turtle import width
from typing import List
from numpy import mat
import pygame
import pygame.font
import math
from queue import PriorityQueue
from ai_search_helper import *

HEIGHT = 500
pygame.font.init()
FONT = pygame.font.SysFont('abyssinicasil', 30)
RED = (255,0,0)
GREEN = (0,255,0)
YELLOW = (255,255,0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

class Spot:
    def __init__(self, row, col, width, total_rows,total_cols):
        self.row = row
        self.col = col
        self.x = col * width
        self.y = row * width
        self.colour =  WHITE
        self.neighbours = []
        self.width = width
        self.total_rows = total_rows
        self.total_cols = total_cols
    
    def isColor(self):
        return self.colour!=WHITE

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.colour == RED

    def is_open(self):
        return self.colour ==GREEN

    def is_barrier(self):
        return self.colour == BLACK

    def is_start(self):
        return self.colour == YELLOW

    def is_end(self):
        return self.colour == RED

    def reset(self):
        self.colour = WHITE

    def make_closed(self):
        self.colour = RED

    def make_open(self):
        self.colour = GREEN

    def make_barrier(self):
        self.colour = BLACK

    def make_end(self):
        self.colour = TURQUOISE

    def make_path(self):
        self.colour = PURPLE

    def make_bonus_point(self):
        self.colour = YELLOW

    def draw(self, win):
        pygame.draw.rect(win, self.colour, (self.x, self.y, self.width, self.width))
    
    def make_start(self):
        self.colour = ORANGE

    def update_neighbours(self, grid):
        self.neighbours = []
        if(self.row == 2 and self.col == 10):
            print(1)
        if self.row < self.total_rows - 1 and not grid[self.row +1][self.col].is_barrier():  #DOWN
            self.neighbours.append(grid[self.row +1][self.col])

        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():   # UP
            self.neighbours.append(grid[self.row -1][self.col])

        if self.col < self.total_cols - 1 and not grid[self.row][self.col+ 1].is_barrier():  #RIGHT
            self.neighbours.append(grid[self.row ][self.col+1])

        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier():  #RIGHT
            self.neighbours.append(grid[self.row][self.col - 1])

    def __lt__(self,other):
        return False  

def add_text(win, spot, text):
        font = pygame.font.Font('freesansbold.ttf', 25)
        text = font.render(text, True, BLACK, WHITE)
        textRect = text.get_rect()
        textRect.center = (spot.x+spot.width/2, spot.y+spot.width/2)
        win.blit(text, textRect)

def reconstruct_path(win, came_from: list, draw):
    i = 0
    for current in came_from:
        current = came_from[len(came_from)-1-i]
        #print((current.row, current.col))
        current.make_path()
        pygame.image.save(win, "tmp_image/" + str(i) + "_.png")
        i+=1
        draw()

def restore_pygame(matrix,COLS,ROWS):
    HEIGHT, WIDTH, grid = make_grid(COLS, ROWS)
    for rows in range(len(matrix)):
        for cols in range(len(matrix[0])):
            grid[rows][cols].reset()
 
    WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # flags = pygame.HIDDEN
    pygame.display.set_caption("Pathfinding")
    for rows in range(len(matrix)):
        for cols in range(len(matrix[rows])):
            if(matrix[rows][cols] == 'x'):
                grid[rows][cols].make_barrier()
            if(matrix[rows][cols] == 'S'):
                start = rows,cols
                grid[rows][cols].make_start()
            if(isExit(rows,cols,matrix)):
                grid[rows][cols].make_end()
                end = rows,cols
    for row in grid:
        for spot in row:
            spot.update_neighbours(grid)
    return WIN, grid, HEIGHT, WIDTH, start, end
    
def make_grid(cols,rows):
    grid = []
    gap = HEIGHT // rows
    
    for i in range(rows):
        grid.append([])
        for j in range(cols):
            spot = Spot(i, j, gap, rows,cols)
            grid[i].append(spot)

    return gap*rows, gap * cols, grid

def draw_grid(win, cols, rows, width):
    gap = width //cols
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i*gap),(width, i*gap))
        for j in range(cols):
            pygame.draw.line(win, GREY, (j* gap, 0), (j* gap,width))

def draw(win, grid, rows, width, bonus_point):
    win.fill(WHITE)
    for row in grid:
        for spot in row:
            spot.draw(win)

    for i in bonus_point:
        add_text(win,grid[i[0]][i[1]],'+')

    draw_grid(win, len(grid[0]), rows, width)
    pygame.display.update()


