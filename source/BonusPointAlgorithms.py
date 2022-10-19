from operator import ne
from time import sleep
from ai_search_helper import *
from ai_search_visualization import *
from ai_search_heuristic_function import *
from ai_search_createvideo import createVideo

from queue import Queue, PriorityQueue
import sys
import pygame.camera

def find_good_way(win, draw, grid, start: Spot, exit: Spot, matrix, H, bonus_points):
    cost=10000;
    goodNextPoint=Spot(0,0,exit.width, exit.row, exit.col);
    for i in start.neighbours:
        currentCost = heuristic_bonus_point(win, draw, grid, i , exit, matrix, H, bonus_points)
        if(cost>currentCost):
            cost=currentCost
            goodNextPoint=i
            
    return cost, goodNextPoint
        

def heuristic_bonus_point(win, draw, grid, start: Spot, exit: Spot, matrix, H, bonus_point):
    currentPoint=Spot(bonus_point[0], bonus_point[1], exit.width, exit.row,exit.col)
    return H(currentPoint,exit)+H(start, currentPoint)-bonus_point[2]

def Astar_bunus_point(win, draw, grid, start: Spot, exit: Spot, matrix, H, bonus_points):
    priorQ = PriorityQueue()
    priorQ.put((0, (start, [start])))
    visited = []
    costSoFar:dict[Spot, int] = {}
    costSoFar[start] = 0
    count = 0
    while not priorQ.empty():
        _, (currentVertex, path) = priorQ.get()
        for i in range(0, len(bonus_points)):
            if(currentVertex.x == bonus_points[i][0] & currentVertex.y == bonus_points[i][1] ):
                newCost = costSoFar[currentVertex] + bonus_points[i][2]
        if(currentVertex == exit):
            break
        currentVertex.make_closed()


        cost = 10000
        for neig in currentVertex.neighbours:
            # Tính hàm f(x) = g(x) + h(x) cho biết tổng độ dài đường đi dự đoán nếu ta tiếp tục đi từ điểm hiện tại đến đích
            exitCost = newCost + H(neig,exit)
            
            # Tính hàm h(x_0, exit) = h(x_0, x_bonus) + h(x_bonus, exit) cho biết tổng độ dài khi lựa chọn đi qua điểm thưởng
            # Sau đó kiểm tra chi phí đến điểm nào là tối ưu nhất và đưa dần chúng vào hàng đợi ưu tiên với thứ tự ưu tiên giảm dần 
            # theo dự đoán (thêm cả điểm đích vào hàm đợi ưu tiên đó).
            heuristicCurrentCost = 10000;
            currentBonusPoint = (0,0,0);
            for j in range(0,len(bonus_points)):
                currentCost = heuristic_bonus_point(win, draw, grid, neig , exit, matrix, H, bonus_points[j])
                if(currentCost<exitPoint):
                    if(currentBonusPoint<heuristicCurrentCost):
                        heuristicCurrentCost = currentCost
                        currentBonusPoint = bonus_points[j]
            
            
        #   
            # newCost = costSoFar[currentVertex] + 1
            
            if neig not in visited or heuristicCurrentCost + costSoFar[currentVertex]< costSoFar[neig]:
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
