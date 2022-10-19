from nonBonusPointAlgorithms import *
from BonusPointAlgorithms import *

def SearchAlgorithmVisual():
    #init D

    #Get matrix, bonus point, start, end
    file_name = "./input/level_1/input1.txt"
    bonus_points, matrix = read_file(file_name)
    ROWS = len(matrix)
    COLS = len(matrix[0])

    # WIN, grid, HEIGHT, WIDTH , start, end = restore_pygame(matrix,COLS,ROWS)
    # width = WIDTH
    # draw(WIN, grid, ROWS, width,bonus_points)
    # Astar(WIN, lambda: draw(WIN, grid, ROWS, width, bonus_points), grid, grid[start[0]][start[1]], grid[end[0]][end[1]],matrix, nonBonusPointAstarHFunct1)
    # createVideo("4.mp4")

    # WIN, grid, HEIGHT, WIDTH , start, end = restore_pygame(matrix,COLS,ROWS)
    # width = WIDTH
    # draw(WIN, grid, ROWS, width,bonus_points)
    # Astar(WIN, lambda: draw(WIN, grid, ROWS, width, bonus_points), grid, grid[start[0]][start[1]], grid[end[0]][end[1]],matrix, nonBonusPointAstarHFunct2)
    # createVideo("5.mp4")

    WIN, grid, HEIGHT, WIDTH , start, end = restore_pygame(matrix,COLS,ROWS)
    width = WIDTH
    draw(WIN, grid, ROWS, width,bonus_points)
    DFS(WIN, lambda: draw(WIN, grid, ROWS, width, bonus_points), grid, grid[start[0]][start[1]], grid[end[0]][end[1]])   #having lambda lets you run the function inside the function
    createVideo("1.mp4")
    
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