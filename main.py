# -*- coding: utf-8 -*-

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from collections import defaultdict

X = np.loadtxt('data.csv', delimiter=",", usecols=(0,2,3,4),
               dtype=[("id", "i8"), ("x", "f8"), ("y", "f8"), ("p", "i8")])

pos = {} # 緯度経路
pop = {} # 人工
for elem in X:
    pos[elem[0]] = (elem[2], elem[1])
    pop[elem[0]] = elem[3]


# 都道府県の隣接情報
adj = np.loadtxt("adj.txt", delimiter=",", dtype=np.int)
G = nx.Graph()
G.add_edges_from(adj)

# グラフ
fig = plt.figure(figsize=(5, 3))
ax = fig.gca()
nx.draw_networkx_nodes(G, pos, ax=ax, node_size=30, node_color='k')
nx.draw_networkx_edges(G, pos, ax=ax, alpha=0.5)
plt.subplots_adjust(0, 0, 1, 1)
plt.savefig("plot2d.png", dpi=300)
plt.close()


# グラフ (3D)
fig = plt.figure(figsize=(9, 5))
ax = fig.gca(projection='3d')

node_color = 'k'
edge_color = 'k'
edge_alpha = 0.5
scale = 1.15
cwidth = 6
column_color = 'r'

for v in G.nodes:
    x, y = pos[v]
    z = 0.0
    ax.scatter(x, y, z, c=node_color, s=20)

for u, v in G.edges():
    x = np.array([pos[u][0], pos[v][0]])
    y = np.array([pos[u][1], pos[v][1]])
    z = np.zeros(2)
    ax.plot(x, y, z, c=edge_color, alpha=edge_alpha)

# 人口を縦に置く
for u in pop:
    x = np.array([pos[u][0], pos[u][0]])
    y = np.array([pos[u][1], pos[u][1]])
    z = np.array([0.0, pop[u]])
    ax.plot(x, y, z, c=column_color, alpha=0.75, lw=cwidth, solid_capstyle="round")

ax.view_init(30, 30)
ax.set_axis_off()
plt.subplots_adjust(0, 0, 1, 1)
plt.show()

# rotation
# for angle in range(0, 360):
#     ax.view_init(30, angle)
#     plt.draw()
#     plt.pause(.001)
# plt.close()
