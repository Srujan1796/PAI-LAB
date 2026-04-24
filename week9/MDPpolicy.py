import numpy as np, random

R = np.full((3,4), -1.0)
R[0,3], R[1,3] = 0, -10
V = np.zeros((3,4))
P = np.random.randint(0,4,(3,4))
gamma = 0.9
T = [(0,3),(1,3)]
A = [(-1,0),(1,0),(0,-1),(0,1)]

def step(i,j,a):
    ni, nj = i+A[a][0], j+A[a][1]
    return (ni,nj) if (0<=ni<3 and 0<=nj<4) else (i,j)

while True:
    # Policy Evaluation
    while True:
        d = 0
        for i in range(3):
            for j in range(4):
                if (i,j) in T: continue
                ni,nj = step(i,j,P[i,j])
                nv = R[ni,nj] + gamma*V[ni,nj]
                d = max(d, abs(nv - V[i,j]))
                V[i,j] = nv
        if d < 1e-4: break

    # Policy Improvement
    stable = True
    for i in range(3):
        for j in range(4):
            if (i,j) in T: continue
            vals = []
            for a in range(4):
                ni,nj = step(i,j,a)
                vals.append(R[ni,nj] + gamma*V[ni,nj])
            best = np.argmax(vals)
            if best != P[i,j]: stable = False
            P[i,j] = best
    if stable: break

print(V)
print(P)
