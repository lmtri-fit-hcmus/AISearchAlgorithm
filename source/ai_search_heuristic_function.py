from ai_search_visualization import *

#Mahatan distance
def nonBonusPointAstarHFunct1(node: Spot, end: Spot):
    dx = abs(node.row - end.row)
    dy = abs(node.col - end.col)
    return (dx + dy)

def nonBonusPointAstarHFunct2(node: Spot, end: Spot):
    dx = abs(node.row - end.row)
    dy = abs(node.col - end.col)
    return dx*dx + dy*dy