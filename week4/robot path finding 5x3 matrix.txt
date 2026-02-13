import heapq

grid = [
    [0,0,0],
    [0,1,0],
    [0,1,0],
    [0,0,0],
    [0,0,0]
]

start, goal = (0,0), (4,2)
R, C = 5, 3

def h(a,b): 
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def astar():
    pq = [(0, start)]
    g = {start:0}
    parent = {}

    while pq:
        _, cur = heapq.heappop(pq)
        if cur == goal:
            path = []
            while cur in parent:
                path.append(cur)
                cur = parent[cur]
            return [start] + path[::-1]

        for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            nr, nc = cur[0]+dr, cur[1]+dc
            if 0<=nr<R and 0<=nc<C and grid[nr][nc]==0:
                newg = g[cur] + 1
                if (nr,nc) not in g or newg < g[(nr,nc)]:
                    g[(nr,nc)] = newg
                    f = newg + h((nr,nc), goal)
                    heapq.heappush(pq, (f, (nr,nc)))
                    parent[(nr,nc)] = cur

    return None

print("Path:", astar())
