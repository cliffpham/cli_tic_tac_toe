class tic_tac_toe:
    def __init__(self):
        pass

    def create_board():
        board = []
        for _ in range(3):
            board.append([False for _ in range(3)])
        return board

    def print_board(board):
        board_copy = [row[:] for row in board]
        print(board_copy)

        for i in range(len(board_copy)):
            for j in range(len(board_copy)):
                if board_copy[i][j] == 1:
                    board_copy[i][j] = 'X'

                elif board_copy[i][j] == 2:
                    board_copy[i][j] = 'O'

                else:
                    board_copy[i][j] = '•'
                
        for row in board_copy:
            for spot in row:
                print(spot, end = " ")
            print()

    def place_move(board, which_user, cmd, used):
        x = int(cmd[0])
        y = int(cmd[1])

        if board[x][y] == False:
            if which_user == True:
                board[x][y] = 1
            else:
                board[x][y] = 2
        
        used.add(cmd)
        print(used)
        tic_tac_toe.print_board(board)

        return True

    def handle_input(board, cmd, used):
        accepted = ['00', '01', '02', '10', '11', '12', '20', '21', '22']
        if cmd not in accepted:
            return False
        if cmd in used:
            return False
        return True

    def check_row(board, which_user, cmd):
        x = int(cmd[0])
        # y = int(cmd[1])
        searching_for = None
        count = 0

        if which_user:
            searching_for = 1
        else:
            searching_for = 2

        for i in range(len(board)):
            if board[x][i] == searching_for:
                count += 1
        
        return count == 3
    
    def check_col(board, which_user, cmd):
        # x = int(cmd[0])
        y = int(cmd[1])
        searching_for = None
        count = 0

        if which_user:
            searching_for = 1
        else:
            searching_for = 2

        for i in range(len(board)):
            if board[i][y] == searching_for:
                count += 1

        return count == 3

    def check_diagonals(board, which_user, cmd):
        searching_for = None
        left_diag_count = 0
        right_diag_count = 0

        if which_user:
            searching_for = 1
        else:
            searching_for = 2

        for i in range(len(board)):
            if board[i][i] == searching_for:
                left_diag_count += 1
            
            if board[i][2-i] == searching_for:
                right_diag_count += 1

        if left_diag_count == 3 or right_diag_count == 3:
            return True
        
        return False


    def check_for_winner(board, which_user, cmd):
        if tic_tac_toe.check_diagonals(board, which_user, cmd) or tic_tac_toe.check_row(board, which_user, cmd) or tic_tac_toe.check_col(board, which_user, cmd):
            return True

        return False

    def play_again(cmd):
        if cmd == 'y':
            return True
        
        return False

    def turn(board, which_user):
        session_on = True
        which_user = True
        used = set()
        winner = None
    
        while session_on:
            cmd = input('type coordinates: ')
            print(which_user)
            if tic_tac_toe.handle_input(board, cmd, used):
                #whichuser is a boolean that tells if its either X or O turn X == True O == False
                if which_user == True:
                    if tic_tac_toe.place_move(board, which_user, cmd, used):
                        if tic_tac_toe.check_for_winner(board, which_user,cmd):
                            winner = 'X'
                            session_on = False
                        which_user = False
                else:
                    if tic_tac_toe.place_move(board, which_user, cmd, used):
                        if tic_tac_toe.check_for_winner(board, which_user,cmd):
                            winner = 'O'
                            session_on = False
                        which_user = True
            else:
                print('Not an accesible move')

        print('Game Over! Winner is: ' + winner)
        print('Play Again?')
        cmd = input("y/n: ")
        if tic_tac_toe.play_again(cmd):
            tic_tac_toe.start_new_game()


    def start_new_game():
        new_board = tic_tac_toe.create_board()
        tic_tac_toe.print_board(new_board)
        tic_tac_toe.turn(new_board, True)
        
        return 

tic_tac_toe.start_new_game()




