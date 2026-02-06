def dfs3jugs(caps, target):
    seen = set()
    def dfs(s):
        if s in seen: return
        seen.add(s)
        if s == target: return [s]
        a,b,c = s
        capA,capB,capC = caps
        moves = [
            (capA,b,c),(a,capB,c),(a,b,capC),
            (0,b,c),(a,0,c),(a,b,0),
            (a-min(a,capB-b),b+min(a,capB-b),c),
            (a-min(a,capC-c),b,c+min(a,capC-c)),
            (a+min(b,capA-a),b-min(b,capA-a),c),
            (a,b-min(b,capC-c),c+min(b,capC-c)),
            (a+min(c,capA-a),b,c-min(c,capA-a)),
            (a,b+min(c,capB-b),c-min(c,capB-b))
        ]
        for m in moves:
            res = dfs(m)
            if res: return [s]+res
    return dfs((0,0,0))


caps = (8,5,3)
target = (4,4,0)
print(dfs3jugs(caps,target))
