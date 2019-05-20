
def powerset(array):
	
    ret_val = [[]]
    for elem in array:
        for i in range(len(ret_val)):
            curr_set = ret_val[i]
            ret_val.append(curr_set + [elem])

    return ret_val
