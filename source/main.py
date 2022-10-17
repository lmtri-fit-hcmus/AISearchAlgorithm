from operator import ne
from source.ai_search_helper import *
from ai_search_visualization import *
from ai_search_createvideo import createVideo
from queue import Queue, PriorityQueue
import sys
import pygame.camera


def DFS(win, draw, grid , start: Spot, exit: Spot):
    stack = [(start,[start])]
    visited = []
    currentVertex = start
    count = 0
    while stack:
        currentVertex, path = stack.pop()
        if(currentVertex!=start):
            currentVertex.make_open()
        if(currentVertex not in visited):
            if currentVertex == exit:
                break
            visited.append(currentVertex)
            for neig in currentVertex.neighbours:
                if(neig not in visited):
                    stack.append((neig,path+[neig]))
                    neig.make_open()
                    draw()  
            pygame.image.save(win, "tmp_image/" + str(count) + ".png")
            count+=1
    if(stack):
        reconstruct_path(win, path, draw)
    return []

def BFS(win, draw, grid , start: Spot, exit: Spot):
    queue = [(start,[start])]
    visited = []
    count = 0
    while(queue):
        currentVertex, path = queue.pop(0)
        if currentVertex == exit:
            break
        for neig in currentVertex.neighbours:
            if neig not in visited:
                queue.append((neig, path+[neig]))
                visited.append(neig)
                if(neig!=start):
                    neig.make_open() 
                count+=1
                draw()
        pygame.image.save(win, "tmp_image/" + str(count) + ".png")
    if(queue):
        reconstruct_path(win, path, draw)
    return []

def UCS(win, draw, grid, start: Spot, exit: Spot, weigh = None):
    priorQ = PriorityQueue()
    priorQ.put((0,(start,[start])))
    visited = []
    count = 0
    while(priorQ):
        w, (currentVertex, path) = priorQ.get()
        visited.append(currentVertex)
        if(currentVertex!=start):
            currentVertex.make_open()
        #pygame.image.save(win, "tmp_image/" + str(count) + ".png")
        count+=1
        if(currentVertex == exit):
            break
        for neig in currentVertex.neighbours:
            if neig not in visited:
                #cost = w + weigh[currentVertex][neig]
                cost = 0
                priorQ.put((cost, (neig, path + [neig])))
                neig.make_open()
                pygame.image.save(win, "tmp_image/" + str(count) + ".png")
                draw()
                count+=1
                

    if(priorQ):
        reconstruct_path(win, path, draw)
        draw()
    return []

#def GBFS(draw, grid, start: Spot, exit: Spot):


def SearchAlgorithmVisual():
    #init D

    #Get matrix, bonus point, start, end
    file_name = "./input/maze_map.txt"
    bonus_points, matrix = read_file(file_name)
    ROWS = len(matrix)
    COLS = len(matrix[0])

    WIN, grid, HEIGHT, WIDTH , start, end = restore_pygame(matrix,COLS,ROWS)
    width = WIDTH
    draw(WIN, grid, ROWS, width)
    DFS(WIN, lambda: draw(WIN, grid, ROWS, width), grid, grid[start[0]][start[1]], grid[end[0]][end[1]])   #having lambda lets you run the function inside the function
    createVideo("1.mp4")
    
    WIN, grid, HEIGHT, WIDTH , start, end = restore_pygame(matrix,COLS,ROWS)
    width = WIDTH
    draw(WIN, grid, ROWS, width)
    BFS(WIN, lambda: draw(WIN, grid, ROWS, width), grid, grid[start[0]][start[1]], grid[end[0]][end[1]])   #having lambda lets you run the function inside the function
    createVideo("2.mp4")
    
    WIN, grid, HEIGHT, WIDTH , start, end = restore_pygame(matrix,COLS,ROWS)
    width = WIDTH
    draw(WIN, grid, ROWS, width)
    UCS(WIN, lambda: draw(WIN, grid, ROWS, width), grid, grid[start[0]][start[1]], grid[end[0]][end[1]])   #having lambda lets you run the function inside the function
    createVideo("3.mp4")

    pygame.quit()

SearchAlgorithmVisual()