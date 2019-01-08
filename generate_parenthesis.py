
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
                current_parenthesis = ''
                for j in range(n):
                        if j == 0:
                                parenthesis_list += '('
                        elif j == (n - 1):
                                parenthesis_list += ')'
                        else:
                                pass
                parenthesis_list.append(current_parenthesis)
