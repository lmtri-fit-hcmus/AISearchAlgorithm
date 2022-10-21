from operator import ne
from time import sleep
from ai_search_helper import *
from ai_search_visualization import *
from ai_search_heuristic_function import *
from ai_search_createvideo import createVideo

from queue import Queue, PriorityQueue
import sys
import pygame.camera

def heuristic_bonus_point(win, draw, grid, start: Spot, exit: Spot, matrix, H, bonus_point):
    currentPoint=Spot(bonus_point[1], bonus_point[0], exit.width, exit.row,exit.col)
    return H(start, currentPoint) + H(currentPoint,exit) + bonus_point[2]

def Astar_bunus_point(win, draw, grid, start: Spot, exit: Spot, matrix, H, bonus_points):
    priorQ = PriorityQueue()
    priorQ.put((0, (start, [start])))
    
    
    # pathPoint = PriorityQueue()
    # pathPoint.put((0,((exit.x, exit.y, -10000), [(exit.x, exit.y, -10000)])))
    
    # listBonusPoints=[]
    # for i in range(0, len(bonus_points)):
    #     cur = Spot(bonus_points[i][0], bonus_points[i][1], exit.width, exit.row, exit.col)
    #     listBonusPoints.append(cur)
    
    ### Tạm thời
    # target = (exit.x, exit.y, -10000)
    ###
    
    visited = []
    costSoFar:dict[Spot, int] = {}
    costSoFar[start] = 0
    count = 0
    bonus = 0
    while not priorQ.empty():
        
        # Lấy thông tin điểm có độ ưu tiên cao nhất ra khỏi hàng đợi
        # Điểm này là điểm hàng xóm kế tiếp có đánh giá là cho con đường đi ngắn nhất trong tất
        # cả các hàng xóm
        dis , (currentVertex, path) = priorQ.get()
        
        # Nếu đã tìm đến điểm kết thúc thì dừng tìm kiếm và chuyển sang bước in đường đi
        if(currentVertex == exit):
            break
        
        # Kiểm tra nếu điểm đang xét là một điểm cộng
        # thì chúng ta thực hiện giảm độ dài đường đi tương ứng với điểm cộng đó
        print("Choose "+str(currentVertex.x/currentVertex.width)+", "+str(currentVertex.y/currentVertex.width)+" "+str(dis))

        currentVertex.make_closed()
        # Đặt giá trị ban đầu của độ dài heuristic dự đoán là số lớn
        # Từ đó đi tìm các độ dài ngắn hơn đến khi tìm được độ dài quãng đường dự đoán là ngắn nhất

        # print("costSoFar")
        # print(costSoFar[currentVertex])
        bonus = 0
        newCost = 1 + costSoFar[currentVertex]
        for neig in currentVertex.neighbours:
            j = 0
            n = len(bonus_points)
            while(j < n):
                if(currentVertex.x/currentVertex.width == bonus_points[j][0] and currentVertex.y/currentVertex.width == bonus_points[j][1]):
                    bonus = bonus + bonus_points[j][2]
                    bonus_points.remove(bonus_points[j])
                    j = j - 1
                    n = n - 1
                j = j + 1
                
            newCost = newCost + bonus
            # Tính hàm f(x) = g(x) + h(x) cho biết tổng độ dài đường đi dự đoán nếu ta tiếp tục đi từ điểm hiện tại đến đích
            heuristicCost =  H(neig,exit)
            # print("exit cost "+str(cost))
            # Xét khoảng cách từ điểm hàng xóm đang xét đến các điểm cộng
            # Tìm con đường được dự đoán là ngắn nhất như sau:
            
            # Tính hàm h(x_0, exit) = h(x_0, x_bonus) + h(x_bonus, exit) cho biết tổng độ dài khi lựa chọn đi qua điểm thưởng
            # Sau đó kiểm tra chi phí đến điểm nào là tối ưu nhất và đưa dần chúng vào hàng đợi ưu tiên với thứ tự ưu tiên giảm dần 
            # theo dự đoán (thêm cả điểm đích vào hàm đợi ưu tiên đó).
            print(str(neig.col) + " " + str(neig.row))
            print("NewCost "+str(newCost))
            print("Exit cost "+str(heuristicCost))

            for j in range(0,len(bonus_points)):
                heuristicCurrentCost = heuristic_bonus_point(win, draw, grid, neig , exit, matrix, H, bonus_points[j])
                
                print("heuristic ("+str(bonus_points[j][0])+", "+str(bonus_points[j][1])+ ") "+str(heuristicCurrentCost))
                # Nếu tìm ra đường đi được dự đoán tốt hơn đi thẳng đến đích thì gán nó là đường đi ưu tiên
                # Sau bước này, ta sẽ tìm ra đường đi được dự đoán là tốt nhất
                if(heuristicCurrentCost < heuristicCost):
                    heuristicCost = heuristicCurrentCost

 
            # Nếu điểm hàng xóm đang xét chưa đi qua, hoặc chi phí mới để đạt đến điểm hiện tại nhỏ hơn chi phí
            # đã tính trước đây thì thực hiện cập nhật chi phí mới
            if neig not in visited or newCost < costSoFar[neig]:
                neig.make_open()
                costSoFar[neig] = newCost
                
                priority = heuristicCost + costSoFar[neig]
                print("Priority "+str(priority))
                priorQ.put( (priority, (neig, path + [neig] )))
                visited.append(neig)

                #sleep(0.5)
            draw()
            pygame.image.save(win, "tmp_image/" + str(count) + ".png")
            count+=1
        print("________")

    if not priorQ.empty():
        reconstruct_path(win, path, draw)
    return []