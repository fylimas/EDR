#!/usr/bin/env python

# import sys sys.exit()
import matplotlib.pyplot as plt
import control as ct
import numpy as np

from matplotlib.font_manager import FontProperties
宋体 = FontProperties(fname=r"/Users/fangyuanli/Library/Fonts/simsun.ttc", size=12)# 指定本机的字体文件路径【需要在自己本机上找你自己的字体】

w = 1
A = [[0,1],[-w*w,0]]
B = [[0],[1]]
C = [[1,0]]
D = 0
X0 = np.array([[0],[0]])
sys = ct.StateSpace(A,B,C,D)

时长 = 10
计算类型 = [ct.step_response,ct.impulse_response]
计算响应 = 计算类型[0]#简单修改计算类型，缩短程序
#【实验1】开环系统的响应
开环t,开环y,开环x = 计算响应(sys,时长,X0=X0,return_x=True)
plt.plot(开环t, 开环y, label='Open Loop')
#配置极点
poles = [-1, -2]
K = ct.place(A, B, poles)
#【实验2】闭环系统的响应
cl_sys = ct.StateSpace(A - B @ K, B, C, D) # @表示矩阵乘法
闭环t, 闭环y, 闭环x = 计算响应(cl_sys,时长,return_x=True)
plt.plot(闭环t, 闭环x[0,:], label='cl_sys x1')
plt.plot(闭环t, 闭环x[1,:], label='cl_sys x2')
plt.legend()
plt.show()
