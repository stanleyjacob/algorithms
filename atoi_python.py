def myAtoi(self, str):
      """
      :type str: str
      :rtype: int
      """
      new_str = str.lstrip()
      if new_str == '':
          return 0
      if new_str[0].isdigit() == False and \
          new_str[0] != '-':
          return 0
      digits_lst = []

      is_negative = False
      if new_str[0] == '-':
          if len(new_str) >= 2 and \
              new_str[1].isdigit():
              is_negative = True
          else:
              return 0

      is_decimal = False
      decimal_count = 0
      for i in range(len(new_str)):
          if new_str[i].isdigit():
              digits_lst.append(int(new_str[i]))
          elif new_str[i] == '.':
              digits_lst.append('.')
              is_decimal = True
          if is_decimal:
              decimal_count += 1

      return_num = 0
      digit_placevalue = -decimal_count
      for i in range(len(digits_lst)-1, -1, -1):
          if digits_lst[i] == '.':
              digit_placevalue += 1
              continue
          else:
              return_num += digits_lst[i] * pow(10, digit_placevalue)
              digit_placevalue += 1
      if is_negative:
          return_num = -return_num
      if return_num < -2147483648:
          return -2147483648
      if return_num > 2147483647:
          return 2147483647
      return return_num

def myAtoi2(self, str):
        """
        :type str: str
        :rtype: int
        """
        new_str = str.lstrip()
        if new_str == '':
            return 0
        if new_str[0].isdigit() == False and \
            new_str[0] != '-' and new_str[0] != '+':
            return 0
        digits_lst = []
        
        is_negative = False
        has_positive = False
        if new_str[0] == '-':
            if len(new_str) >= 2 and \
                new_str[1].isdigit():
                is_negative = True
            else:
                return 0
        elif new_str[0] == '+':
            if len(new_str) >= 2 and \
                new_str[1].isdigit():
                has_positive = True
            else:
                return 0
        
        if is_negative or has_positive:
            new_str = new_str[1:]
        for i in range(len(new_str)):
            if new_str[i].isdigit():
                digits_lst.append(int(new_str[i]))
            else:
                break
                
        return_num = 0
        digit_placevalue = 0
        for i in range(len(digits_lst)-1, -1, -1):
            return_num += digits_lst[i] * pow(10, digit_placevalue)
            digit_placevalue += 1
        if is_negative:
            return_num = -return_num
        if return_num < -2147483648:
            return -2147483648
        if return_num > 2147483647:
            return 2147483647
        return return_num
