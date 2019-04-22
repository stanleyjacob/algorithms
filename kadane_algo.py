
def kadanesAlgorithm(array):
    if len(array) == 0:
        return 0
    max_end = curr_max = array[0]
    for i in range(1, len(array)):
        max_end = max(array[i], max_end + array[i])
        curr_max = max(max_end, curr_max)
    return curr_max
    
