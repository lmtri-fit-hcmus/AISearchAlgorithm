x = [(-1,0),(1,0),(0,-1),(0,1)]
def isValidVertex(vertex,matrix):
    if(vertex[0]<0 or vertex[0]>=len(matrix) or vertex[1] < 0 or vertex[1] > len(matrix[0])):
        return False
    if(matrix[vertex[0]][vertex[1]] == 'x'):
        return False
    return True
def DFS(matrix, start, exit):
    stack = [start]
    path = []
    currentVertex = start
    while stack:
        currentVertex = stack.pop()
        path.append(currentVertex)
        for neig in x:
            nextVertex = (currentVertex[0] + neig[0],currentVertex[1] + neig[1])
            if(isValidVertex(nextVertex,matrix) and not(nextVertex in path)):
                if(nextVertex == exit):
                    path.append(nextVertex)
                    return path
                stack.append(nextVertex)
    return []
            
