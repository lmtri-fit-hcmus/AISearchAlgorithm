from fileinput import filename

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

