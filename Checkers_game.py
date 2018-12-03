# To Mr. V: the game works better (and you can see the board better in 'Lucinda console' or 'Terminal' font)
# Sorry, I couldn't find a way to replace a piece by another in update_board

def initialize_board() -> list:
        '''
        Return the list b, which is the base of the board as it is at the beginning of the game
        >>>initialize_board()
        [" 1 1 1 1", "1 1 1 1 ", " 1 1 1 1", "0 0 0 0 ", " 0 0 0 0", "2 2 2 2 ", " 2 2 2 2", "2 2 2 2 "]
        '''
        b = [" 1 1 1 1", "1 1 1 1 ", " 1 1 1 1", "0 0 0 0 ", " 0 0 0 0", "2 2 2 2 ", " 2 2 2 2", "2 2 2 2 "] 
        return b




def display_board(board) -> str:
        '''
        Return each item of board as a line
        >>>display_board([" 1 1 1 1", "1 1 1 1 ", " 1 1 1 1", "0 0 0 0 ", " 0 0 0 0", "2 2 2 2 ", " 2 2 2 2", "2 2 2 2 "])
            01234567
        0 |  1 1 1 1 |
        1 | 1 1 1 1  |
        2 |  1 1 1 1 |
        3 | 0 0 0 0  |
        4 |  0 0 0 0 |
        5 | 2 2 2 2  |
        6 |  2 2 2 2 |
        7 | 2 2 2 2  |
        '''
        print('    01234567')
        row = 0
        for item in board :
                print(row,'|',item,'|')
                row += 1




def valid_piece(board, piece) -> bool:
    """
    Return True iff board at index piece is moveable and is the player's piece
    >>>initialize_board()
    >>>valid_piece(b,22)
    False
    """
    p0,p1=int(piece[0]),int(piece[1])
    if((p0<0) or (p0>7) or (p1<0) or (p1>7)):
        return False
    direction=3-2*player
    if (p1+direction>7) or (p1+direction<0):
        return False
    if board[p0][p1] == ' ' :
        return False
    if not int(board[p0][p1]) == player :
        return False
    if (p0==0):
        if int(board[p0+1][p1+direction]) == 0:
            return True
    if (p0==7):
        if int(board[p0-1][p1+direction]) == 0:
            return True
    if ((p0>0) and (p0<7)):
        if (int(board[p0+1][p1+direction]) == 0) or (int(board[p0-1][p1+direction]) == 0):
            return True
    otherplayer=3-player
    m1=p1+2*direction
    if (m1>7) or (m1<0):
        return False
    m0=p0+2
    if (m0>7):
        m0=p0-2
        if (int(board[m0][m1]) == 0) and (int(board[(p0+m0)/2][(p1+m1)/2]) == otherplayer):
            return True
        else:
            return False
    if (int(board[m0][m1]) == 0) and (int(board[int((p0+m0)/2)][int((p1+m1)/2)]) == otherplayer):
        return True
    m0=p0-2
    if (m0<0):
        return False
    return (int(board[m0][m1]) == 0) and (int(board[(p0+m0)/2][(p1+m1)/2]) == otherplayer)




def valid_move(board, move, piece) -> bool :
    """
    Return True iff piece is moveable in board at the index move
    >>>initialize_board()
    >>>valid_move(b,21,30)
    True
    """
    # if not board[int(move[0])][int(move[1])] == ' ' :
    #   return True
    # return False

    m0,m1,p0,p1=int(move[0]),int(move[1]),int(piece[0]),int(piece[1])
    noerror=((m0>=0) and (m0<8) and (m1>=0) and (m1<8))
    if not noerror :
        print('Target position outside the board!')
        return False
    if (board[m0][m1]==' '):
        print('Target position on white square!')
        return False
    target=int(board[m0][m1])
    if not (target==0):
        print('Occupied square!')
        return False
    dlin=m0-p0
    dcol=m1-p1
    direction=3-2*player
    if not (noerror and (abs(dcol)*direction>0) and (abs(dcol)*direction<3) and (abs(dlin)<3) and (abs(dlin)>0) and (abs(dcol)*direction==abs(dlin))) :
        print('Wrong move!')
        return False
    if (int(dlin*direction)==1):
        return True
    otherplayer=3-player
    mid0=p0+int(dlin/2)
    mid1=p1+int(dcol/2)
    return (int(board[mid0][mid1])==otherplayer)




def update_board(board : list, move : str, piece : str, player : int) -> bool : #Sur celle-la, je ne sais pas verifier si il y a fin de jeu
    """
    Update board by moving piece of player to move.
    Return True if and only if the opposing player
    (the one that is not moving a piece)
    has no valid moves after updating the game.
    """
    m0,m1,p0,p1=int(move[0]),int(move[1]),int(piece[0]),int(piece[1])
    dlin=m0-p0
    dcol=m1-p1
    list(board[m0]).insert(m1,board[p0][p1])
    list(board[p0]).insert(p1,board[m0][m1])
    a, b = list(board[m0]).pop(m1+1), list(board[p0]).pop(p1+1)
    otherplayer=3-player
    mid0=(p0+dlin)/2
    mid1=(p1+dcol)/2
    if int(board[int(mid0)][int(mid1)]) == otherplayer :
        a = board.pop([mid0][mid1])
        board.insert([mid0][mid1] ,'0')

    a=[]
    for line in range(len(board)) :
        for col in range(len(board[line])):
            piece = str(line) + str(col)
            if not board[line][col] == ' ' :
                if int(board[line][col]) == player :
                    a += [valid_piece(board,piece)]
    return a[0] and a[1] and a[2] and a[3] and a[4] and a[5] and a[6] and a[7]




def update_player(player) -> int :
    '''
    Return the value of the non playing player for player
    >>>update_player(1)
    2
    '''
    if player == 1 :
        return 2
    elif player == 2 :
        return 1




if __name__ == "__main__":
    board = initialize_board()
    player = 1
    gameover = False
    while not gameover:
        display_board(board)
        piece = input("Player {}, pick a piece to move".format(player))
        while not valid_piece(board, piece):
            piece = input("Player {}, pick a valid piece".format(player))
        move = input("Player {}, where would you like to move the piece at {}?".format(player, piece))
        while not valid_move(board, move, piece):
            move = input("Player {}, pick a valid move for the piece at {}.".format(player, piece))
        gameover = update_board(board, move, piece, player)
        player = update_player(player)
    player = update_player(player)
print("Game over, player {} wins!".format(player))