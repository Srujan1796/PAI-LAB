import math
board = [" "]*9
HUMAN, AI = "O", "X"
restricted = {1,2}   # positions 2 and 6 (0-indexed)
def print_board():
    for i in range(0,9,3):
        print("|".join(board[i:i+3]))
        print("-"*5)
def win(p):
    w = [(0,1,2),(3,4,5),(6,7,8),
         (0,3,6),(1,4,7),(2,5,8),
         (0,4,8),(2,4,6)]
    return any(board[a]==board[b]==board[c]==p for a,b,c in w)
def minimax(is_ai):
    if win(AI): return 1
    if win(HUMAN): return -1
    if " " not in board: return 0
    best = -math.inf if is_ai else math.inf
    for i in range(9):
        if board[i]==" " and (not is_ai or i not in restricted):
            board[i] = AI if is_ai else HUMAN
            score = minimax(not is_ai)
            board[i] = " "
            best = max(best,score) if is_ai else min(best,score)
    return best
def best_move():
    best, move = -math.inf, -1
    for i in range(9):
        if board[i]==" " and i not in restricted:
            board[i]=AI
            score=minimax(False)
            board[i]=" "
            if score>best:
                best, move = score, i
    return move
print("Positions:")
print("1|2|3\n-----\n4|5|6\n-----\n7|8|9")
while True:
    print_board()
    p=int(input("Enter position (1-9): "))-1
    if board[p]!=" ":
        print("Invalid move")
        continue
    board[p]=HUMAN
    if win(HUMAN):
        print_board(); print("Human wins"); break
    if " " not in board:
        print_board(); print("Draw"); break
    m=best_move()
    board[m]=AI
    if win(AI):
        print_board(); print("AI wins"); break
