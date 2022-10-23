from ai_search_helper import *


def SearchAlgorithmVisual():
    #init D
    file_name = LEVEL2_INPUT_PATH + '/' + 'input3.txt'
    bonus_points, matrix = read_file(file_name)
    ROWS = len(matrix)
    COLS = len(matrix[0])

    WIN, grid, HEIGHT, WIDTH , start, end = restore_pygame(matrix,COLS,ROWS)
    pygame.display.set_caption("GBFS " + file_name)
    width = WIDTH
    draw(WIN, grid, ROWS, width,bonus_points)
    resetTmpImage()
    isPath, length = Astar_bonus_point(WIN, lambda: draw(WIN, grid, ROWS, width, bonus_points), grid, grid[start[0]][start[1]], grid[end[0]][end[1]], ManhattanDistance,bonus_points)   #having lambda lets you run the function inside the function
    createVideo('gbfs_heuristic_2.mp4') 
    #createText(isPath, length, output_path + '/gbfs/gbfs_heuristic_2.txt') 
    #nonBonusStart()
    #bonusStart()
    pygame.quit()

SearchAlgorithmVisual()