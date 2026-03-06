import math

s = [0,0,0]  # system state: 0=safe,1=compromised
D,A = 1,-1

def moves(st,p): return [i for i,v in enumerate(st) if (p==A and v==0) or (p==D and v==1)]
def apply(st,i,p): n=st[:]; n[i]=1 if p==A else 0; return n
def eval_st(st): return st.count(0)-st.count(1)
def over(st): return all(v==1 for v in st) or all(v==0 for v in st)

def minimax(st,depth,p,alpha,beta):
    if depth==0 or over(st): return eval_st(st)
    if p==D:
        best=-math.inf
        for m in moves(st,D):
            best=max(best,minimax(apply(st,m,D*-1),depth-1,A,alpha,beta))
            alpha=max(alpha,best)
            if beta<=alpha: break
        return best
    else:
        best=math.inf
        for m in moves(st,A):
            best=min(best,minimax(apply(st,m,D),depth-1,D,alpha,beta))
            beta=min(beta,best)
            if beta<=alpha: break
        return best

def best(st,p):
    bm,best_val=(-1,-math.inf) if p==D else (-1,math.inf)
    for m in moves(st,p):
        v=minimax(apply(st,m,p),5,-p,-math.inf,math.inf)
        if (p==D and v>best_val) or (p==A and v<best_val): best_val,bm=v,m
    return bm

cur=A
while not over(s):
    print("State:",s)
    m=best(s,cur)
    print(("Defender" if cur==D else "Attacker"),"chooses",m)
    s[m]=1 if cur==A else 0
    cur*=-1
print("Final state:",s)
v=eval_st(s)
print("Defender wins!" if v>0 else "Attacker wins!" if v<0 else "Draw!")
