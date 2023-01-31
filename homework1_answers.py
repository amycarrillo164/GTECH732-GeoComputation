# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 14:45:42 2023

@author: amyca
"""

import platform
print(platform.python_version())

# [2]
import random
random.seed(1009)
rndList_2 = []
for i in range (1, 50):
    rndList_2.append(random.randint(0,200))
    
print(rndList_2)

import statistics
print(statistics.mean(rndList_2))
print(statistics.variance(rndList_2))