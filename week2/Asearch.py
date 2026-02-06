import heapq

def water_jug_a_star(a, b, goal):
    h = lambda s: min(abs(goal - s[0]), abs(goal - s[1]))
    start = (0, 0)

    pq = [(h(start), 0, start)]
    parent = {start: None}

    while pq:
        _, g, (x, y) = heapq.heappop(pq)

        if x == goal or y == goal:
            path = []
            cur = (x, y)
            while cur:
                path.append(cur)
                cur = parent[cur]
            return path[::-1]

        for nx, ny in {
            (a, y), (x, b), (0, y), (x, 0),
            (x - min(x, b - y), y + min(x, b - y)),
            (x + min(y, a - x), y - min(y, a - x))
        }:
            if (nx, ny) not in parent:
                parent[(nx, ny)] = (x, y)
                heapq.heappush(pq, (g + 1 + h((nx, ny)), g + 1, (nx, ny)))

    return None



print(water_jug_a_star(4, 3, 2))
