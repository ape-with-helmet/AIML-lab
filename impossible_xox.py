#import random generator library
import random 

board=[" " for _ in range(9)] #generate the actual xox board
checker=[0 for _ in range(9)] #generate the number board for the computer to refer to

def print_board(): #prints the board in a structured format
    print(f"\n|{board[0]}|{board[1]}|{board[2]}|")
    print(f"|{board[3]}|{board[4]}|{board[5]}|")
    print(f"|{board[6]}|{board[7]}|{board[8]}|\n")

def player_move():
    while True:
        ch = int(input("Make your move!")) #take user input
        if board[ch-1]==" ": #check if location is empty
            board[ch-1] = "X"
            checker[ch-1]=5 #set number to 5 for playr move
            break
        else:
            print("\nSpace taken!\ntry again!") #re take the input

def victory(): #checks the win condition for xox
    if (board[0] == "X" and board[1] == "X" and board[2] == "X") or (board[3] == "X" and board[4] == "X" and board[5] == "X") or (board[6] == "X" and board[7] == "X" and board[8] == "X") or (board[0] == "X" and board[3] == "X" and board[6] == "X") or (board[1] == "X" and board[4] == "X" and board[7] == "X") or (board[2] == "X" and board[5] == "X" and board[8] == "X") or (board[0] == "X" and board[4] == "X" and board[8] == "X") or (board[2] == "X" and board[4] == "X" and board[6] == "X"):
        return True 
    else:
        return False

def is_draw(): #checks if all the boxes are filled
    if " " not in board:
        return True
    else:
        return False

def check_filled(a,b,c): #returns the index of the block which will give victory for either player or computer
    if checker[a] == 0:
        return a
    elif checker[b] == 0:
        return b
    elif checker[c] == 0:
        return c
    else: return 99

def Pwinning_move(): #checks if player can win and returns the position of the winning block or 99
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

def Cwinning_move(): #checks if computer can win and returns the position of the winning block or 99
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

def random_mover(): #randomly fills a spot
    while " " in board:
        listpos = [0,1,2,3,4,5,6,7,8,0,0,2,2,0,4,4,6,6,8,8]
        cmove = int(random.choice(listpos))
        if board[cmove] == " ":
            board[cmove] = "O"
            checker[cmove] = 3
            return

def computer_move(): #computer movement algorithm
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
          return True
print("\n\n\nWELCOME TO IMPOSSIBLE' XOX!\nTRY NOT TO LOSE!\n\n\n")
print_board()
c_count = 0
side = bool(random.choice([True,False])) #randomly decide sides
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
        if computer_move():
            print_board()
            print("Computer Wins!")
            break
        print_board()
        if is_draw():
            print_board()
            print("DRAW!")
            break 
else:
    while True:
        print("Computer move!")
        if computer_move():
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
