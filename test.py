#!/usr/bin/env python
import numpy as np
w = 0.06
a = -0**2
# Define your matrix
hA = np.array([[0, 1], [-w**2, 0]])
A = np.array([[0, 1], [-1, 0]])
B = np.array([[0], [1]])
K = np.array([[3,4]])
Gamma=np.array([[a, 0], [0, a]])
r=np.array([[1], [0]])
print(np.linalg.inv(hA + Gamma - B @ K)@(A + Gamma - B @ K) @ r)

