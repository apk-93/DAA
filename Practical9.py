N=4
#create board
    
board=[[0 for i in range(N)]for j in range(N)]
#print(board)

def check_column(board,row,column):
    for i in range(row,-1,-1):
        if board[i][column]==1:
            return False
    return True

def check_diagonal(board,row,column):
    for i,j in zip(range(row,-1,-1),range(column,-1,-1)):
        if board[i][j]==1:
            return False

    for i,j in zip(range(row,-1,-1),range(column,N)):
        if board[i][j]==1:
            return False
    return True

def NQueens(board,row):
    if row==N:
        return True
    for i in range(N):
        if(check_column(board,row,i)==True and check_diagonal(board,row,i)):
            board[row][i]=1
            if NQueens(board,row+1):
                return True
            board[row][i]=1
            if NQueens(board,row+1):
                return True
            board[row][i]=0
    return False
NQueens(board,0)
for row in board:
    print(row)
