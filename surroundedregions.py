#https://leetcode.com/problems/surrounded-regions/
class Solution:
    def isborder(m,n,x,y):
        isb=False
        if x == 0:
            isb = True
        elif x == m:
            isb = True
        elif y == 0:
            isb = True
        elif y == n:
            isb = True
        else:
            isb = False
        return isb   
    
    def issurr(board,i,j):
        sur = False
        if board[i][j-1] =='X' and (board[i][j+1] =='X') and (board[i+1][j] =='X') and (board[i-1][j] =='X'):
            return True

        #check 4 directions North
        if (Solution.issurr(board,i,j-1)):
            #south
            if  Solution.issurr(board,i,j+1):
                print(i,j+1,board[i][j+1])
                #east
                if  Solution.issurr(board,i+1,j):
                    print(i+1,j,board[i+1][j])
                    #west
                    if  Solution.issurr(board,i-1,j):
                        return True
        

            
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        m = len(board)-1
        n = len(board[0])-1
        print (m,n)
        for i in range(0,m):
            for j in range(0,n):
                if not Solution.isborder(m,n,i,j):
                    print(i,j,board[i][j],'notborder')
                    if board[i][j]=='O':
                        flip = False
                        if Solution.issurr(board,i,j):
                            flip = True
                            board[i][j]='X'
        print (board)
                                        
