# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 15:46:06 2022

@author: Jacob Landerer
"""

from vpython import * 
floor = box(color = color.red,pos = vector(0,-5,0),length = 10,height = .1,width = 10)
ball = sphere(radius = 4, pos = vector(0,4,0),color = color.blue)
delY = .1
yPos = 4
while True:
    rate(10)
    if (yPos < -1 or yPos > 20):
        delY = -1*delY
        ball.pos = vector(0,delY,0)
    yPos = yPos + delY
    ball.pos = vector(0,yPos,0)