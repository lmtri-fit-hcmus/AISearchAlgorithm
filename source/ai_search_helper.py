from fileinput import filename
import imp
from os import listdir
import shutil
from ai_search_createvideo import *
from nonBonusPointAlgorithms import *

LEVEL1_INPUT_PATH = "./input/level_1"
LEVEL2_INPUT_PATH = "./input/level_2"

LEVEL1_OUTPUT_PATH = "./output/level_1"
LEVEL2_OUTPUT_PATH = "./output/level_2"



def read_file(file_name: str = 'maze.txt'):
    f = open(file_name, 'r')
    n_bonus_points = int(next(f)[:-1])
    bonus_points = []
    for i in range(n_bonus_points):
        x, y, reward = map(int, next(f)[:-1].split(' '))
        bonus_points.append((x, y, reward))

    text = f.read()
    matrix = [list(i) for i in text.splitlines()]
    f.close()

    return bonus_points, matrix

x = [(-1,0),(1,0),(0,-1),(0,1)]
def isValidVertex(vertex,matrix):
    if(vertex[0]<0 or vertex[0]>=len(matrix) or vertex[1] < 0 or vertex[1] > len(matrix[0])):
        return False
    if(matrix[vertex[0]][vertex[1]] == 'x'):
        return False
    return True


def resetTmpImage():
    if os.path.exists('tmp_image'):
        shutil.rmtree('tmp_image')
    os.mkdir('tmp_image')

def nonBonusStart():
    for i in listdir(LEVEL1_INPUT_PATH):
        file_name = LEVEL1_INPUT_PATH + '/' + i
        bonus_points, matrix = read_file(file_name)
        ROWS = len(matrix)
        COLS = len(matrix[0])

        output_path = LEVEL1_OUTPUT_PATH + '/' + i.split('.')[0]

        if not os.path.exists(LEVEL1_OUTPUT_PATH):
            os.mkdir(LEVEL1_OUTPUT_PATH)
        if not os.path.exists(output_path):
            os.mkdir(output_path)

        WIN, grid, HEIGHT, WIDTH , start, end = restore_pygame(matrix,COLS,ROWS)
        width = WIDTH
        draw(WIN, grid, ROWS, width,bonus_points)
        resetTmpImage()
        DFS(WIN, lambda: draw(WIN, grid, ROWS, width, bonus_points), grid, grid[start[0]][start[1]], grid[end[0]][end[1]])   #having lambda lets you run the function inside the function
        createVideo(output_path + '/dfs.mp4') 

        WIN, grid, HEIGHT, WIDTH , start, end = restore_pygame(matrix,COLS,ROWS)
        width = WIDTH
        draw(WIN, grid, ROWS, width,bonus_points)
        resetTmpImage()
        BFS(WIN, lambda: draw(WIN, grid, ROWS, width, bonus_points), grid, grid[start[0]][start[1]], grid[end[0]][end[1]])   #having lambda lets you run the function inside the function
        createVideo(output_path + '/bfs.mp4') 
        
        WIN, grid, HEIGHT, WIDTH , start, end = restore_pygame(matrix,COLS,ROWS)
        width = WIDTH
        draw(WIN, grid, ROWS, width,bonus_points)
        resetTmpImage()
        UCS(WIN, lambda: draw(WIN, grid, ROWS, width, bonus_points), grid, grid[start[0]][start[1]], grid[end[0]][end[1]])   #having lambda lets you run the function inside the function
        createVideo(output_path + '/ucs.mp4') 


    
