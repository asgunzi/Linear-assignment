# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 10:46:24 2025

@author: asgunzi
"""

import numpy as np
cost = np.array([[4, 1, 3], [2, 0, 5], [3, 2, 2]])

print(cost)

from scipy.optimize import linear_sum_assignment

row_ind, col_ind = linear_sum_assignment(cost)


print(row_ind)
print(col_ind)
cost[row_ind, col_ind].sum()

