#!/usr/bin/env python
import matplotlib.pyplot as plt
import control as ct
import numpy as np
import pickle as pc

from matplotlib.font_manager import FontProperties
宋体 = FontProperties(fname=r"/Users/fangyuanli/Library/Fonts/simsun.ttc", size=12)# 指定本机的字体文件路径【需要在自己本机上找你自己的字体】

w = 1
A = [[0,1],[-w*w,0]]
B = [[0],[1]]
C = [[1,0]]
D = 0
sys = ct.StateSpace(A,B,C,D)

时长 = 8
#引入参考信号p.519
r = 1
K = np.array([[3,4]])
N = 2
#更改系统参数
w=0.06
A_min = [[0,1],[-w*w,0]]
w=0.6
A_mid = [[0,1],[-w*w,0]]
w=1.6
A_max = [[0,1],[-w*w,0]]
#新控制器参数
a = 4
K_n = np.array([[a*a,0]])
#新控制器
参环t, 参环y, 参环x_n = ct.forced_response(ct.StateSpace(A - B@(K+K_n), B, C, D),T=np.linspace(0, 时长, 1000),U=(N+a*a)*r,return_x=True)
参变t, 参变y, 参变x_min_n = ct.forced_response(ct.StateSpace(A_min - B@(K+K_n), B, C, D),T=np.linspace(0, 时长,1000),U=(N+a*a)*r,return_x=True)
参变t, 参变y, 参变x_mid_n = ct.forced_response(ct.StateSpace(A_mid - B@(K+K_n), B, C, D),T=np.linspace(0, 时长,1000),U=(N+a*a)*r,return_x=True)
参变t, 参变y, 参变x_max_n = ct.forced_response(ct.StateSpace(A_max - B@(K+K_n), B, C, D),T=np.linspace(0, 时长,1000),U=(N+a*a)*r,return_x=True)

with open('Q/txu.pkl', 'rb') as ws:
    data_pickle = pc.load(ws)
t = data_pickle['t']
x = data_pickle['x']
t1 = data_pickle['t1']
x1 = data_pickle['x1']
t2 = data_pickle['t2']
x2 = data_pickle['x2']

#绘制不一致系统的控制
#绘制新控制器的x1
plt.figure(figsize=(6,4))# 设置绘图的宽、高，默认英寸
plt.plot(参变t, 参变x_min_n[0,:], label='Var. Ref., $\hat{\omega}_0=0.06$')
plt.plot(参变t, 参变x_mid_n[0,:], label='Var. Ref., $\hat{\omega}_0=0.6$')
plt.plot(参变t, 参变x_max_n[0,:], label='Var. Ref., $\hat{\omega}_0=1.6$')
print(t1.shape,x1.shape)
plt.plot(t, x[0,:], label='Q-learning, $\hat{\omega}_0=0.06$', linestyle = '--')
plt.plot(t1, x1[0,:], label='Q-learning, $\hat{\omega}_0=0.6$', linestyle = '--')
plt.plot(t2, x2[0,:], label='Q-learning, $\hat{\omega}_0=1.6$', linestyle = '--')
plt.xticks(fontproperties = 'Times New Roman', size = 12)
plt.yticks(fontproperties = 'Times New Roman', size = 12)
plt.xlabel('Time(sec)',fontproperties='Times New Roman', size = 12)
plt.ylabel('Amplitude of $y(x_1)$',fontproperties='Times New Roman', size = 12)
plt.xlim(0,时长)
plt.ylim(0,1.6)
plt.legend(fontsize=9)
plt.grid(True)
if False:
    plt.savefig('Q-x1.pdf', bbox_inches='tight')
plt.show()
