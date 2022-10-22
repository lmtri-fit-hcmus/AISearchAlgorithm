from operator import ne
from time import sleep
from ai_search_helper import *
from ai_search_visualization import *
from ai_search_heuristic_function import *
from ai_search_createvideo import createVideo

from queue import Queue, PriorityQueue
import sys
import pygame.camera


def BFS(win, draw, grid , start: Spot, exit: Spot):
    queue = [(start,[start])]
    visited = []
    count = 0
    while(queue):
        currentVertex, path = queue.pop(0)
        if(currentVertex!=start):
            currentVertex.make_closed()
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
    if(queue or currentVertex == exit):
        reconstruct_path(win, path, draw)
        return 1,len(path) 
    return 0,0


def DFS(win, draw, grid , start: Spot, exit: Spot):
    stack = [(start,[start])]
    visited = []
    currentVertex = start
    count = 0
    while stack:
        currentVertex, path = stack.pop()
        if(currentVertex!=start):
            currentVertex.make_closed()
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
            count +=1
    if(stack or currentVertex == exit):
        reconstruct_path(win, path, draw)
        return 1,len(path) 
    return 0,0


def UCS(win, draw, grid, start: Spot, exit: Spot, weigh = None):
    priorQ = PriorityQueue()
    priorQ.put((0,(start,[start])))
    visited = []
    count = 0
    while(priorQ.qsize()):
        w, (currentVertex, path) = priorQ.get()
        visited.append(currentVertex)
        if(currentVertex!=start):
            currentVertex.make_closed()
        count+=1
        if(currentVertex == exit):
            break
        for neig in currentVertex.neighbours:
            if neig not in visited:
                cost = 0
                priorQ.put((cost, (neig, path + [neig])))
                neig.make_open()
                count+=1
        draw()
        pygame.image.save(win, "tmp_image/" + str(count) + ".png")
        #infinity loop

    if(priorQ.qsize() or currentVertex == exit):
        reconstruct_path(win, path, draw)
        return 1,len(path) 
    return 0,0

def GBFS(win, draw, grid, start: Spot, exit: Spot, H):
    priorQ = PriorityQueue() 
    priorQ.put( (0, (start, [start])) )
    visited = []
    count = 0
    while priorQ.qsize():
        #get top and make closed (if possible)
        _, ( currentVertex, path ) = priorQ.get() 
        if currentVertex != start:
            currentVertex.make_closed()
        if currentVertex == exit:
            break        
        
        for neig in currentVertex.neighbours:
            #if neighbour is a valid vertex
            if ( neig not in visited ):
                cost = H(neig, exit)
                priorQ.put( ( cost, ( neig, path + [neig] ) ) )
                neig.make_open()
                visited.append(neig)
        draw()
        pygame.image.save(win, "tmp_image/" + str(count) + ".png")
        count+=1

    if priorQ.qsize() or currentVertex == exit:
        reconstruct_path(win, path, draw)
        return 1,len(path) 
    return 0,0


def Astar(win, draw, grid, start: Spot, exit: Spot, H):
    priorQ = PriorityQueue()
    priorQ.put((0, (start, [start])))
    visited = []
    costSoFar:dict[Spot, int] = {}
    currentVertex = start
    costSoFar[start] = 0
    count = 0
    while not priorQ.empty():
        _, (currentVertex, path) = priorQ.get()
        # Nếu điểm đang xác là điểm kết thúc thì dừng
        if(currentVertex == exit):
            break
        
        # Thực hiện đánh đáu điểm đang xét là 'đã đi qua'
        currentVertex.make_closed()
        
        # Xét các hàng xóm của điểm đang xét
        for neig in currentVertex.neighbours:
            # Tính độ dài đường di đến điểm hàng xóm
            newCost = costSoFar[currentVertex] + 1
            
            # Nếu điểm hàng xóm đã được đi qua hoặc tìm ra con đường ngắn hơn đi đến điểm hàng xóm
            # Thì thực hiện mở các ô cạnh nó
            if neig not in visited or newCost < costSoFar[neig]:
                neig.make_open()
                
                # Cập nhật độ dài con đường đến điểm hàng xóm
                costSoFar[neig] = newCost
                
                # Tính hàm đánh giá dựa trên độ dài đã đi qua ở hiện tại cộng với độ dài đường
                # đi dự đoán đến điểm đích.
                priority = newCost + H(neig,exit)
                
                # In giá trị để kiểm tra
                #print(str(neig.row) + " " + str(neig.col) + " " + str(priority))
                
                # Đưa điểm đang hàng xóm đang xét, đường đi cùng độ dài quãng được đánh giá vào
                # hàng đợi ưu tiên
                priorQ.put( (priority, (neig, path + [neig] )))
                
                # Thêm hàng xóm vào tập các điểm đã đi qua.
                visited.append(neig)
                #sleep(0.5)
            draw()
            count+=1
        pygame.image.save(win, "tmp_image/" + str(count) + ".png")
                



    if not priorQ.empty() or currentVertex == exit:
        reconstruct_path(win, path, draw)
        return 1,len(path) 
    return 0,0