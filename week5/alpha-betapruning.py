import math

board = [" "]*9
H, A = "O", "X"
restricted = {1,2}
wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]

def print_board():
    for i in range(9):
        print(board[i] if board[i]!=" " else str(i+1), end="|")
        if i%3==2: print("\n-----")

def win(p): return any(board[a]==board[b]==board[c]==p for a,b,c in wins)

def minimax(ai, alpha, beta):
    if win(A): return 1
    if win(H): return -1
    if " " not in board: return 0
    best = -math.inf if ai else math.inf
    for i in range(9):
        if board[i]==" " and (ai or i not in restricted):
            board[i]=A if ai else H
            score=minimax(not ai, alpha, beta)
            board[i]=" "
            if ai: best=max(best,score); alpha=max(alpha,best)
            else: best=min(best,score); beta=min(beta,best)
            if beta<=alpha: break
    return best

def best_move():
    move,best=-1,-math.inf
    for i in range(9):
        if board[i]==" " and i not in restricted:
            board[i]=A
            score=minimax(False,-math.inf,math.inf)
            board[i]=" "
            if score>best: best,move=score,i
    return move

print("Positions:\n1|2|3\n-----\n4|5|6\n-----\n7|8|9")
while True:
    print_board()
    try: p=int(input("Enter position (1-9): "))-1
    except: continue
    if p<0 or p>8 or board[p]!=" ": continue
    board[p]=H
    if win(H): print_board(); print("Human wins!"); break
    if " " not in board: print_board(); print("Draw!"); break
    m=best_move()
    if m==-1: print_board(); print("Draw!"); break
    board[m]=A
    if win(A): print_board(); print("AI wins!"); break
