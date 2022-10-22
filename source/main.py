from ai_search_helper import *
from BonusPointAlgorithms import *


def SearchAlgorithmVisual():
    #init D

    #Get matrix, bonus point, start, end
    # file_name = "./input/level_1/input2.txt"
    # bonus_points, matrix = read_file(file_name)
    # ROWS = len(matrix)
    # COLS = len(matrix[0])
    
    # WIN, grid, HEIGHT, WIDTH , start, end = restore_pygame(matrix,COLS,ROWS)
    # width = WIDTH

    # draw(WIN, grid, ROWS, width,bonus_points)
    # print(str(grid[start[0]][start[1]])+" "+str(grid[end[0]][end[1]])+" "+ str(ManhattanDistance(grid[start[0]][start[1]], grid[end[0]][end[1]])))
    # UCS(WIN, lambda: draw(WIN, grid, ROWS, width, bonus_points), grid, grid[start[0]][start[1]], grid[end[0]][end[1]])
    # createVideo("6.mp4")
    
    nonBonusStart()

    pygame.quit()

SearchAlgorithmVisual()