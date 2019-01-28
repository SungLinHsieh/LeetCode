class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            if self.invalid(board[i]) or self.invalid([board[j][i] for j in range(9)]) or\
            self.invalid([ board[i//3*3+k][i%3*3+j] for j in range(3) for k in range(3)]):
                return False
        return True
    def invalid(self,l):
        tmp = [None]*10
        for s in l:
            if s != '.' and tmp[int(s)]!=None:
                return True
            elif s != '.':
                tmp[int(s)] = int(s)
        return False
