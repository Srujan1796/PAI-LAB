import numpy as np

R = np.full((3,4), -1.0)
R[0,3], R[1,3] = 0, -10
V = np.zeros((3,4))
gamma, eps = 0.9, 1e-4
T = [(0,3),(1,3)]
A = [(-1,0),(1,0),(0,-1),(0,1)]

while True:
    d = 0
    for i in range(3):
        for j in range(4):
            if (i,j) in T: continue
            vals = []
            for a in A:
                ni, nj = i+a[0], j+a[1]
                if not (0<=ni<3 and 0<=nj<4): ni,nj = i,j
                vals.append(R[ni,nj] + gamma*V[ni,nj])
            nv = max(vals)
            d = max(d, abs(nv - V[i,j]))
            V[i,j] = nv
    if d < eps: break

print(V)
