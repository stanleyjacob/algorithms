

def reconstruct(source_dict, curr_index):
    total_path = [curr_index]
    while curr_index in source_dict.keys():
        curr_index = source_dict[curr_index]
        total_path.append(curr_index)
    return total_path
  
def a_star(start, goal):
  
    evaluated_set = {}
    needs_evaluation_set = {start}
    
    previous_map = {}
    
