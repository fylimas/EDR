from q_learning.q_learning import *
from env.pendulum_env import *
import matplotlib.pyplot as plt
import numpy as np
import pickle as pc
import sys
from matplotlib.font_manager import FontProperties
宋体 = FontProperties(fname=r"/Users/fangyuanli/Library/Fonts/simsun.ttc", size=12)# 指定本机的字体文件路径【需要在自己本机上找你自己的字体】

# Function which executes the policy
def policy(x):
  th, w = get_positions_in_qtable(x)
  u = POLICY[th, w]
  return u

# Initialize Q-table
q_table = np.random.uniform(-1, 1, size=(DISCRETE_WINDOWS, DISCRETE_WINDOWS, len(CONTROLS)))

# Train or Load
if False:
    # Q-learning
    learned_q_table, cost_per_episode = q_learning(q_table)
    data_pickle = {'learned_q_table': learned_q_table,'cost_per_episode': cost_per_episode}
    with open('save.pkl', 'wb') as ws:
        pc.dump(data_pickle, ws)
else:
    data_pickle = {}
    with open('2w.pkl', 'rb') as ws:
        data_pickle = pc.load(ws)
    learned_q_table = data_pickle['learned_q_table']
    cost_per_episode = data_pickle['cost_per_episode']

# Get the optimal policy and value function from the learned Q-table
print(learned_q_table.shape)
POLICY, VALUE_FUNCTION = get_policy_and_value_function(learned_q_table)

SIMULATION_TIME=20
# Simulate the optimal policy
# System without inconsistencies
t, x, u = simulate(INITIAL_STATE, policy, SIMULATION_TIME, 0.06)
# System when omega=0.5
t1, x1, u1 = simulate(INITIAL_STATE, policy, SIMULATION_TIME, 0.6)
# System when omega=1.5
t2, x2, u2 = simulate(INITIAL_STATE, policy, SIMULATION_TIME, 1.6)
data_pickle = {'t': t, 'x': x, 't1': t1, 'x1': x1, 't2': t2, 'x2': x2}

with open('txu.pkl', 'wb') as ws:
    pc.dump(data_pickle, ws)

# Plot the cost per episode
plt.figure()
plt.plot(cost_per_episode)
plt.legend(['Cost'])
plt.xlabel('Episodes')
plt.show()

plt.figure()
plt.plot(t,x[0,:])
plt.plot(t1,x1[0,:])
plt.plot(t2,x2[0,:])
plt.legend(['$\hat{\omega}_0=1$','$\hat{\omega}_0=0.5$','$\hat{\omega}_0=1.5$'])
plt.show()

plt.figure()
plt.plot(t,x[1,:])
plt.plot(t1,x1[1,:])
plt.plot(t2,x2[1,:])
plt.legend(['$\hat{\omega}_0=1$','$\hat{\omega}_0=0.5$','$\hat{\omega}_0=1.5$'])
plt.show()

plt.figure()
plt.plot(t[1:],u[:])
plt.plot(t1[1:],u1[:])
plt.plot(t2[1:],u2[:])
plt.show()

# Visualize the results
#animate_robot(x)
sys.exit()
# plot and save all figures
cases=[('1k',20),('1w',20),('2w',20),('4w',20)]
for icase,SIMULATION_TIME in cases:
    with open(icase+'.pkl', 'rb') as ws:
        data_pickle = pc.load(ws)
    learned_q_table = data_pickle['learned_q_table']
    cost_per_episode = data_pickle['cost_per_episode']
    # Get the optimal policy and value function from the learned Q-table
    POLICY, VALUE_FUNCTION = get_policy_and_value_function(learned_q_table)
    print(learned_q_table.shape)
    # Simulate the optimal policy
    # System without inconsistencies
    t, x, u = simulate(INITIAL_STATE, policy, SIMULATION_TIME, 1)
    # System when omega=0.5
    t1, x1, u1 = simulate(INITIAL_STATE, policy, SIMULATION_TIME, 0.5)
    # System when omega=1.5
    t2, x2, u2 = simulate(INITIAL_STATE, policy, SIMULATION_TIME, 1.5)
    plt.figure()
    plt.plot(cost_per_episode)
    plt.xlabel('Episodes',fontproperties='Times New Roman', size = 12)
    plt.ylabel('Cost',fontproperties='Times New Roman', size = 12)
    plt.grid(True)
    plt.savefig(icase+'c.pdf', bbox_inches='tight')
    plt.show()
    plt.figure()
    plt.plot(t,x[0,:], label='$\hat{\omega}_0=1$')
    plt.plot(t1,x1[0,:], label='$\hat{\omega}_0=0.5$')
    plt.plot(t2,x2[0,:], label='$\hat{\omega}_0=1.5$')
    plt.xticks(fontproperties = 'Times New Roman', size = 12)
    plt.yticks(fontproperties = 'Times New Roman', size = 12)
    plt.xlabel('Time(sec)',fontproperties='Times New Roman', size = 12)
    plt.ylabel('Amplitude of $y(x_1)$',fontproperties='Times New Roman', size = 12)
    plt.xlim(0,SIMULATION_TIME)
    plt.ylim(0,1.6)#int(max(x1[0,:])*10+1)/10)
    plt.legend()
    plt.grid(True)
    plt.savefig(icase+'x1.pdf', bbox_inches='tight')
    plt.show()



