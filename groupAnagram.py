def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    total_dict = dict()
    for current_str in strs:
        new_dict = dict()
        for current_char in current_str:
            if current_char not in new_dict:
                new_dict[current_char] = 1
            else:
                new_dict[current_char] += 1
        frozen_dict = frozenset(new_dict.items())
        if frozen_dict not in total_dict:
            total_dict[frozen_dict] = [current_str]
        else:
            total_dict[frozen_dict].append(current_str)
    output = []
    for key, value in total_dict.items():
        output.append(value)
    return output
