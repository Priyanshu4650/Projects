import copy
import random

class TicTacToe:
    def __init__(self, board, winning_state):
        self.winning_state = winning_state
        self.board = board

    def print_board(board):
        for i in range(0, 9, 3):
            print(board[i:i+3])
            print('\n')

    def evaluate_board(winning_states, state):   
        if " " not in state:
            for i in range(8):
                x = winning_states[i]
                if state[x[0]-1]==state[x[1]-1] and state[x[1]-1]==state[x[2]-1] and state[x[0]-1]!=" ":
                    if state[x[0]-1]=="O" :
                        return -1
                    else :
                        return 1
            return 0 
        else :
            for i in range(8):
                x= winning_states[i]
                if state[x[0]-1]==state[x[1]-1] and state[x[1]-1]==state[x[2]-1] and state[x[0]-1]!=" ":
                    if state[x[0]-1]=="O" :
                        return -1
                    else :
                        return 1
            return 2 
        
    def max_value(state):
        x = TicTacToe.evaluate_board(winning_state, state)
        #print(x)
        if(x != 2):
            return x
        
        moves = []
        utility = []

        for i  in range(len(state)):
            if(state[i] == " "):
                board_copy = copy.deepcopy(state)
                board_copy[i] = "X"
                moves.append(board_copy)
            
        #print("After max : ", len(moves))  
        #print_board(moves[0])
        for i in range(len(moves)):
            utility.append(TicTacToe.min_value(moves[i]))

        return max(utility)

    def min_value(state):
        x = TicTacToe.evaluate_board(winning_state, state)
        if(x != 2):
            return x
        
        moves = []
        utility = []
        
        for i  in range(len(state)):
            if(state[i] == " "):
                board_copy = copy.deepcopy(state)
                board_copy[i] = "O"
                moves.append(board_copy)
        
        #print("After min : ", len(moves))  
        #print_board(moves[0])
        for i in range(len(moves)):
            utility.append(TicTacToe.max_value(moves[i]))

        return min(utility)


    def comp_move(board):
        moves = []
        #global board
        
        for i  in range(len(board)):
            if(board[i] == " "):
                board_copy = copy.deepcopy(board)
                board_copy[i] = "X"
                moves.append(board_copy)
            
        utility = []
        
        
        #print(len(moves))
        #print_board(moves[0])
        for i in range(len(moves)):
            utility.append(TicTacToe.min_value(moves[i]))
        
        m = max(utility)
        
        gen_moves = []
        for i in range(len(moves)):
            if utility[i] == m :
                gen_moves.append(i)
        
        rand_move = random.choice(gen_moves)
        
        board = moves[rand_move]
        TicTacToe.print_board(board)
        
        return board
        
    def human_move(board):
        pos = int(input("Enter position [1, 9] : "))
        
        while(board[pos-1] != " "):
            print("Invalid Move!!!\nEnter again")
            pos = int(input("Enter position [1, 9] : "))
        board[pos-1] = "O"
        #print_board(board)
        
        return board    

winning_state = [[1, 2, 3], 
                [1, 4, 7], 
                [4, 5, 6], 
                [7, 8, 9], 
                [2, 5, 8], 
                [3, 6, 9], 
                [1, 5, 9], 
                [3, 5, 7]]

board = [" " for i in range(9)]


TicTacToe(board, winning_state)

while(1):
    #print_board(board)
    #pos = int(input("Enter position [1, 9] : "))

    board = TicTacToe.human_move(board)

    #print_board(board)

    if(TicTacToe.evaluate_board(winning_state, board) == 0):
        print("\n\nGame Draw!!!")
        break

    elif(TicTacToe.evaluate_board(winning_state, board) == -1):
        print("\n\nPlayer O(You) wins!!!")
        break

    else:
        board = TicTacToe.comp_move(board)
        if(TicTacToe.evaluate_board(winning_state, board) == 1):
            print("\n\nPlayer X(A.I) wins!!!")
            break
