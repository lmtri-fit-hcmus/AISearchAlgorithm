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
            currentVertex.make_end()
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
                currentVertex.make_end()
                break
            visited.append(currentVertex)
            for neig in currentVertex.neighbours:
                if(neig not in visited):
                    stack.append((neig,path+[neig]))
                    if not neig.is_start():
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
            currentVertex.make_end()
            break
        for neig in currentVertex.neighbours:
            if neig not in visited:
                cost = 0
                priorQ.put((cost, (neig, path + [neig])))
                if not neig.is_start():
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
            currentVertex.make_end()
            break        
        
        for neig in currentVertex.neighbours:
            #if neighbour is a valid vertex
            if ( neig not in visited ):
                cost = H(neig, exit)
                priorQ.put( ( cost, ( neig, path + [neig] ) ) )
                if not neig.is_start():
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
        # N???u ??i???m ??ang x??c l?? ??i???m k???t th??c th?? d???ng
        if(currentVertex == exit):
            currentVertex.make_end()
            break
        
        # Th???c hi???n ????nh ????u ??i???m ??ang x??t l?? '???? ??i qua'
        currentVertex.make_closed()
        
        # X??t c??c h??ng x??m c???a ??i???m ??ang x??t
        for neig in currentVertex.neighbours:
            # T??nh ????? d??i ???????ng di ?????n ??i???m h??ng x??m
            newCost = costSoFar[currentVertex] + 1
            
            # N???u ??i???m h??ng x??m ???? ???????c ??i qua ho???c t??m ra con ???????ng ng???n h??n ??i ?????n ??i???m h??ng x??m
            # Th?? th???c hi???n m??? c??c ?? c???nh n??
            if neig not in visited or newCost < costSoFar[neig]:
                if neig!=start:
                    neig.make_open()
                
                # C???p nh???t ????? d??i con ???????ng ?????n ??i???m h??ng x??m
                costSoFar[neig] = newCost
                
                # T??nh h??m ????nh gi?? d???a tr??n ????? d??i ???? ??i qua ??? hi???n t???i c???ng v???i ????? d??i ???????ng
                # ??i d??? ??o??n ?????n ??i???m ????ch.
                priority = newCost + H(neig,exit)
                
                # In gi?? tr??? ????? ki???m tra
                #print(str(neig.row) + " " + str(neig.col) + " " + str(priority))
                
                # ????a ??i???m ??ang h??ng x??m ??ang x??t, ???????ng ??i c??ng ????? d??i qu??ng ???????c ????nh gi?? v??o
                # h??ng ?????i ??u ti??n
                priorQ.put( (priority, (neig, path + [neig] )))
                
                # Th??m h??ng x??m v??o t???p c??c ??i???m ???? ??i qua.
                visited.append(neig)
                #sleep(0.5)
            draw()
            count+=1
        pygame.image.save(win, "tmp_image/" + str(count) + ".png")
                



    if not priorQ.empty() or currentVertex == exit:
        reconstruct_path(win, path, draw)
        return 1,len(path) 
    return 0,0