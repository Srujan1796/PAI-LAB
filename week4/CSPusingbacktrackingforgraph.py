import networkx as nx
import matplotlib.pyplot as plt

V = ['A','B','C','D']
E = [('A','B','1'),('A','C','2'),('B','C','3'),('B','D','4'),('C','D','5')]
C = ['red','green','blue']
sol = {}

# Adjacency
G_dict = {v:[] for v in V}
for u,v,_ in E:
    G_dict[u].append(v); G_dict[v].append(u)

def solve():
    if len(sol)==len(V): return True
    v = [x for x in V if x not in sol][0]
    for c in C:
        if all(sol.get(n)!=c for n in G_dict[v]):
            sol[v]=c
            if solve(): return True
            del sol[v]
    return False

solve()
print("Solution:", sol)

# Draw
G = nx.Graph()
G.add_nodes_from(V)
G.add_edges_from([(u,v) for u,v,_ in E])

pos = nx.spring_layout(G)
nx.draw(G,pos,with_labels=True,node_color=[sol[n] for n in G],node_size=2000)
nx.draw_networkx_edge_labels(G,pos,edge_labels={(u,v):l for u,v,l in E})

plt.show()
