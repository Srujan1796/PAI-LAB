import heapq

def a_star(start, goal):
    h = lambda s: sum(abs(divmod(s.index(i),3)[0]-divmod(goal.index(i),3)[0]) + abs(divmod(s.index(i),3)[1]-divmod(goal.index(i),3)[1]) for i in range(1,9))
    moves = [(-1,0),(1,0),(0,-1),(0,1)]
    q = [(h(start),0,start,[start])]
    seen = set()
    while q:
        f,g,s,path = heapq.heappop(q)
        if s in seen: continue
        seen.add(s)
        if s==goal: return path
        i = s.index(0); x,y = divmod(i,3)
        for dx,dy in moves:
            nx,ny = x+dx,y+dy
            if 0<=nx<3 and 0<=ny<3:
                n = list(s); ni = nx*3+ny; n[i],n[ni]=n[ni],n[i]
                heapq.heappush(q,(g+1+h(tuple(n)),g+1,tuple(n),path+[tuple(n)]))


start = (1,2,3,4,0,6,7,5,8)
goal  = (1,2,3,4,5,6,7,8,0)
sol = a_star(start,goal)
for st in sol:
    print(st[:3]); print(st[3:6]); print(st[6:]); print()
