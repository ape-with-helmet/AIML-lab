import random

board=[" " for _ in range(9)]
checker=[0 for _ in range(9)]

def print_board():
    print(f"\n|{board[0]}|{board[1]}|{board[2]}|")
    print(f"|{board[3]}|{board[4]}|{board[5]}|")
    print(f"|{board[6]}|{board[7]}|{board[8]}|\n")

def player_move():
    while True:
        ch = int(input("Make your move!"))
        if board[ch-1]==" ":
            board[ch-1] = "X"
            checker[ch-1]=5
            break
        else:
            print("\nSpace taken!\ntry again!")

def victory():
    if (board[0] == "X" and board[1] == "X" and board[2] == "X") or (board[3] == "X" and board[4] == "X" and board[5] == "X") or (board[6] == "X" and board[7] == "X" and board[8] == "X") or (board[0] == "X" and board[3] == "X" and board[6] == "X") or (board[1] == "X" and board[4] == "X" and board[7] == "X") or (board[2] == "X" and board[5] == "X" and board[8] == "X") or (board[0] == "X" and board[4] == "X" and board[8] == "X") or (board[2] == "X" and board[4] == "X" and board[6] == "X"):
        return True
    else:
        return False

def is_draw():
    if " " not in board:
        return True
    else:
        return False

def check_filled(a,b,c):
    if checker[a] == 0:
        return a
    elif checker[b] == 0:
        return b
    elif checker[c] == 0:
        return c
    else: return 99

def Pwinning_move():
    if checker[0] + checker[1]+ checker[2] == 10:
        return check_filled(0,1,2)
    elif checker[3] + checker[4]+ checker[5] == 10:
        return check_filled(3,4,5)
    elif checker[6] + checker[7]+ checker[8] == 10:
        return check_filled(6,7,8)
    elif checker[0] + checker[3]+ checker[6] == 10:
        return check_filled(0,3,6)
    elif checker[1] + checker[4]+ checker[7] == 10:
        return check_filled(1,4,7)
    elif checker[2] + checker[5]+ checker[8] == 10:
        return check_filled(2,5,8)
    elif checker[0] + checker[4]+ checker[8] == 10:
        return check_filled(0,4,8)
    elif checker[2] + checker[4]+ checker[6] == 10:
        return check_filled(2,4,6)
    else:
        return 99

def Cwinning_move():
    if checker[0] + checker[1]+ checker[2] == 6:
        return check_filled(0,1,2)
    elif checker[3] + checker[4]+ checker[5] == 6:
        return check_filled(3,4,5)
    elif checker[6] + checker[7]+ checker[8] == 6:
        return check_filled(6,7,8)
    elif checker[0] + checker[3]+ checker[6] == 6:
        return check_filled(0,3,6)
    elif checker[1] + checker[4]+ checker[7] == 6:
        return check_filled(1,4,7)
    elif checker[2] + checker[5]+ checker[8] == 6:
        return check_filled(2,5,8)
    elif checker[0] + checker[4]+ checker[8] == 6:
        return check_filled(0,4,8)
    elif checker[2] + checker[4]+ checker[6] == 6:
        return check_filled(2,4,6)
    else:
        return 99

def random_mover():
    while " " in board:
        listpos = [0,1,2,3,4,5,6,7,8]
        cmove = int(random.choice(listpos))
        if board[cmove] == " ":
            board[cmove] = "O"
            checker[cmove] = 3
            return
def comp_decider(c,d):
    if d == 3:
        random_mover()
    elif c%d == 0:
        computer_move()
    else:
        random_mover()
def computer_move():
    win_move = Cwinning_move()
    if win_move == 99:
        p_win = Pwinning_move()
        if p_win == 99:
            random_mover()
            return False
        else:
            board[p_win] = "O"
            checker[p_win] = 3
            return False
    else:
        board[win_move] = "O"
        checker[win_move] = 3
        print("Computer Wins!")
        return True
print("\n\n\nWELCOME TO IMPOSSIBLE' XOX!\nTRY NOT TO LOSE!\n\n\n")
side = bool(random.choice([True,False]))
d = int(input("Enter difficulty!\n1 - hard\n2 - medium\n3 - easy"))
c = 0
print_board()
if side:
    while True:
        print("Player move!")
        player_move()
        print_board()
        if victory():
            print("Player Won!")
            break
        if is_draw():
            print("DRAW!")
            break 
        print("Computer move!")
        if comp_decider(c,d):
            print_board()
            break
        print_board()
        if is_draw():
            print_board()
            print("DRAW!")
            break 
else:
    while True:
        print("Computer move!")
        if comp_decider(c,d):
            print_board()
            print("Computer Wins!")
            break
        print_board()
        if is_draw():
            print_board()
            print("DRAW!")
            break 
        print("Player move!")
        player_move()
        print_board()
        if victory():
            print("Player Won!")
            break
        if is_draw():
            print("DRAW!")
            break 
