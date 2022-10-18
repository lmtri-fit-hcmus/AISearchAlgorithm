from operator import ne
from time import sleep
from ai_search_helper import *
from ai_search_visualization import *
from ai_search_heuristic_function import *
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

def GBFS(win, draw, grid, start: Spot, exit: Spot):
    return 1

def Astar(win, draw, grid, start: Spot, exit: Spot, matrix, H):
    priorQ = PriorityQueue()
    priorQ.put((0, (start, [start])))
    visited = []
    costSoFar:dict[Spot, int] = {}
    costSoFar[start] = 0
    count = 0
    while not priorQ.empty():
        _, (currentVertex, path) = priorQ.get()
        
        if(currentVertex == exit):
            break
        currentVertex.make_closed()
        for neig in currentVertex.neighbours:
            newCost = costSoFar[currentVertex] + 1
            if neig not in visited or newCost < costSoFar[neig]:
                neig.make_open()
                
                costSoFar[neig] = newCost
                priority = newCost + H(neig,exit)
                print(str(neig.row) + " " + str(neig.col) + " " + str(priority))
                priorQ.put( (priority, (neig, path + [neig] )))
                visited.append(neig)
                #sleep(0.5)
            draw()
            pygame.image.save(win, "tmp_image/" + str(count) + ".png")
            count+=1
                



    if not priorQ.empty():
        reconstruct_path(win, path, draw)
    return []


def SearchAlgorithmVisual():
    #init D

    #Get matrix, bonus point, start, end
    file_name = "./input/level_1/input1.txt"
    bonus_points, matrix = read_file(file_name)
    ROWS = len(matrix)
    COLS = len(matrix[0])

    WIN, grid, HEIGHT, WIDTH , start, end = restore_pygame(matrix,COLS,ROWS)
    width = WIDTH
    draw(WIN, grid, ROWS, width,bonus_points)
    Astar(WIN, lambda: draw(WIN, grid, ROWS, width, bonus_points), grid, grid[start[0]][start[1]], grid[end[0]][end[1]],matrix, nonBonusPointAstarHFunct1)
    createVideo("4.mp4")

    WIN, grid, HEIGHT, WIDTH , start, end = restore_pygame(matrix,COLS,ROWS)
    width = WIDTH
    draw(WIN, grid, ROWS, width,bonus_points)
    Astar(WIN, lambda: draw(WIN, grid, ROWS, width, bonus_points), grid, grid[start[0]][start[1]], grid[end[0]][end[1]],matrix, nonBonusPointAstarHFunct2)
    createVideo("5.mp4")

    # WIN, grid, HEIGHT, WIDTH , start, end = restore_pygame(matrix,COLS,ROWS)
    # width = WIDTH
    # draw(WIN, grid, ROWS, width,bonus_points)
    # DFS(WIN, lambda: draw(WIN, grid, ROWS, width, bonus_points), grid, grid[start[0]][start[1]], grid[end[0]][end[1]])   #having lambda lets you run the function inside the function
    # createVideo("1.mp4")
    
    # WIN, grid, HEIGHT, WIDTH , start, end = restore_pygame(matrix,COLS,ROWS)
    # width = WIDTH
    # draw(WIN, grid, ROWS, width,bonus_points)
    # BFS(WIN, lambda: draw(WIN, grid, ROWS, width, bonus_points), grid, grid[start[0]][start[1]], grid[end[0]][end[1]])   #having lambda lets you run the function inside the function
    # createVideo("2.mp4")
    
    # WIN, grid, HEIGHT, WIDTH , start, end = restore_pygame(matrix,COLS,ROWS)
    # width = WIDTH
    # draw(WIN, grid, ROWS, width,bonus_points)
    # UCS(WIN, lambda: draw(WIN, grid, ROWS, width, bonus_points), grid, grid[start[0]][start[1]], grid[end[0]][end[1]])   #having lambda lets you run the function inside the function
    # createVideo("3.mp4")

    pygame.quit()

SearchAlgorithmVisual()