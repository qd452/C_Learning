# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 06:02:46 2016

@author: dong.qu

2: 1-1,                                  2
3: 1-1-1,     1-2,                       2-1
4: 1-1-1-1,   1-1-2,            1-2-1, , 2-1-1,          2-2
5: 1-1-1-1-1, 1-1-1-2, 1-1-2-1, 1-2-1-1, 2-1-1-1, 2-1-2, 2-2, 2-2-1
"""

def stair(c):
    if (c <2):
        return c
    return stair(c-1) + stair(c-2)
    
def stair_combinations(c):
    return stair(c + 1)
    
print(stair_combinations(2))
print(stair_combinations(3))
print(stair_combinations(4))
print(stair_combinations(5))

