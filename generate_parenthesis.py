
# returns possible combinations
# of parenthesis given n pairs
def generateParenthesis(self, n):
        if n == 0:
            return
        if n == 1:
            return ['()']
        max_num_open_parenthesis = n / 2
        
        parenthesis_list = []
        for i in range(n):
                for i in range(n):
                        if i == 0:
                                parenthesis_list.append('(')
                        elif i == (n - 1):
                                parenthesis_list.append(')')
                        else:
                                pass
