def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0:
        return False
    elif x < 10:
        return True
    digits_list = []
    current_num = x
    while True:
        most_right_digit = current_num % 10
        digits_list.append(most_right_digit)
        current_num = current_num // 10 
        if current_num == 0:
            break
    right_index = len(digits_list) - 1
    for i in range(len(digits_list) // 2):
        if digits_list[i] != digits_list[right_index]:
            return False
        right_index -= 1
    return True
