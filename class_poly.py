# -*- coding: utf-8 -*-
"""
Created on Thu May 20 15:15:20 2021

@author: Chris Chiang
"""

class Polygon:
    def __init__(self, *dot_list):
        self.dot_list = dot_list
        
    def __repr__(self):
        return f'perimeter is {Polygon.perimeter(self):.2f}'
           
    def perimeter(self):
        dot_list = self.dot_list
        length = 0
        for i in range(len(dot_list)):
            x = (dot_list[i-1][0] - dot_list[i][0])**2
            y = (dot_list[i-1][1] - dot_list[i][1])**2
            length += (x+y) ** 0.5
        return round(length, 2)
    
try:
    triangle = Polygon((0,0), (3,0), (0,4))
    diamond = Polygon((-1,0), (0,-1), (1,0), (0,1))

    print(triangle.perimeter())
    print(diamond.perimeter())

    print(triangle)
    print(diamond)
except Exception as e:
    print(e)