def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    symbol_dict = {'I':1, 'V':5, 'X':10, \
                  'L':50, 'C':100, 'D':500,\
                  'M':1000}
    value_list = []
    for i in range(len(s)):
        value_list.append(symbol_dict[s[i]])

    aggregate_value = 0
    running_value = 0
    previous_value = None
    count = 1
    for current_value in value_list:
        if previous_value == None:
            previous_value = current_value
            running_value = previous_value

        elif current_value == previous_value:
            count += 1
            running_value = count * previous_value

        elif current_value < previous_value:
            aggregate_value += count * previous_value
            previous_value = current_value
            count = 1
            running_value = previous_value

        elif current_value > previous_value:
            aggregate_value += (current_value - previous_value)
            previous_value = None
            running_value = 0

    aggregate_value += running_value
    return aggregate_value
