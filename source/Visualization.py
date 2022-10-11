#source code to make video display:
#https://www.youtube.com/watch?v=JtiK0DOeI4A

from time import sleep
from turtle import width
from typing import List
from numpy import mat
import pygame
import math
from queue import PriorityQueue

HEIGHT = 500


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

    def draw(self, win):
        pygame.draw.rect(win, self.colour, (self.x, self.y, self.width, self.width))

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

    def make_start(self):
        self.colour = ORANGE
def reconstruct_path(came_from: list, draw):
    i = 0
    for current in came_from:
        current = came_from[len(came_from)-1-i]
        print((current.row, current.col))
        current.make_path()
        sleep(0.01)
        i+=1
        draw()

def algorithm(draw, grid, start, end):
    count = 0
    open_set = PriorityQueue()   # returns the smallest value in the list
    open_set.put((0, count, start))
    came_from = {}
    g_score = {spot: float("inf") for row in grid for spot in row}
    g_score[start] = 0
    f_score = {spot: float("inf") for row in grid for spot in row}
    f_score[start] = h(start.get_pos(), end.get_pos())

    open_set_hash = {start}
    while not open_set.empty():
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                pygame.quit()
        current = open_set.get()[2]      # returns the best value
        open_set_hash.remove(current)
        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            start.make_start()
            return True

        for neighbour in current.neighbours:
            temp_g_score = g_score[current]+1

            if temp_g_score < g_score[neighbour]:
                came_from[neighbour] = current
                g_score[neighbour] = temp_g_score
                f_score[neighbour] = temp_g_score + h(neighbour.get_pos(), end.get_pos())
                if neighbour not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbour], count, neighbour))
                    open_set_hash.add(neighbour)
                    neighbour.make_open()
        draw()
        if current != start:
            current.make_closed()

    return False



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

def draw(win, grid, rows, width):
    win.fill(WHITE)
    for row in grid:
        for spot in row:
            spot.draw(win)

    draw_grid(win, len(grid[0]), rows, width)
    pygame.display.update()

def isExit(rows,cols,matrix):
    if(cols == 0 and matrix[rows][cols] == ' '):
        if(matrix[rows][cols+1] != 'x'):
            return 1
    if(cols == len(matrix[0])-1 and matrix[rows][cols] == ' '):
        if(matrix[rows][cols-1] != 'x'):
            return 1
    if(rows == 0 and matrix[rows][cols] == ' '):
        if(matrix[rows+1][cols] != 'x'):
            return 1
    if(rows == len(matrix)-1 and matrix[rows][cols] == ' '):
        if(matrix[rows-1][cols] != 'x'):
            return 1
    return 0
