from operator import ne
from time import sleep
from Helper import *
from Visualization import *
import sys
import pygame.camera

def DFS(draw, grid , start: Spot, exit: Spot):
    stack = [(start,[start])]
    visited = []
    currentVertex = start
    while stack:
        currentVertex, path = stack.pop()

        currentVertex.make_open()
        if(currentVertex not in visited):
            if currentVertex == exit:
                break
            visited.append(currentVertex)
            for neig in currentVertex.neighbours:
                if(neig not in visited):
                    stack.append((neig,path+[neig]))
                    neig.make_open()
                    sleep(0.01)
                    draw()  
    if(stack):
        reconstruct_path(path, draw)
    return []

def BFS(draw, grid , start: Spot, exit: Spot):
    queue = [(start,[start])]
    visited = []
    while(queue):
        currentVertex, path = queue.pop(0)
        if currentVertex == exit:
            break
        for neig in currentVertex.neighbours:
            if neig not in visited:
                queue.append((neig, path+[neig]))
                visited.append(neig)
                neig.make_open()
                sleep(0.01)
                draw()
    if(start):
        reconstruct_path(path, draw)
    return []

def main():
    #init pygame
    pygame.init()
    pygame.camera.init()
    

    #Get matrix, bonus point, start, end
    file_name = "./input/maze_map.txt"
    bonus_points, matrix = read_file(file_name)
    ROWS = len(matrix)
    COLS = len(matrix[0])
    HEIGHT, WIDTH, grid = make_grid(COLS, ROWS)
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pathfinding")
    run = True
    started = False

                
    while run:
        width = WIDTH
        draw(WIN, grid, ROWS, width)
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
           
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if started:
                continue
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    for row in grid:
                        for spot in row:
                            spot.update_neighbours(grid)
                    BFS(lambda: draw(WIN, grid, ROWS, width), grid, grid[start[0]][start[1]], grid[end[0]][end[1]])   #having lambda lets you run the function inside the function


    pygame.quit()


main()