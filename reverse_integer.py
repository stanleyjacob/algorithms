def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    is_negative = False

    current_num = None
    if x < 0:
        is_negative = True
        current_num = -x
    else:
        current_num = x

    digits_list = []
    while True:
        current_digit = current_num % 10
        current_num //= 10
        digits_list.append(current_digit)
        if current_num == 0:
            break
    exponent_value = 0
    result_num = 0
    for i in range(len(digits_list) - 1, -1, -1):
        result_num += digits_list[i] * pow(10, exponent_value)
        exponent_value += 1

    if is_negative:
        result_num = -result_num
        if result_num < -pow(2, 31):
            return 0
    elif result_num > (pow(2, 31) - 1):
        return 0
    return result_num
