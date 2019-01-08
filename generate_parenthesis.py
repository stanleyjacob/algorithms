
def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return
        if n == 1:
            return ['()']
        max_num_open_parenthesis = n / 2
        
        for i in range(n):
            pass
