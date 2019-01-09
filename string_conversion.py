
def convert(s, numRows):
  total_len = len(s) / numRows
  str_matrix = [['\0' for j in range(numRows)] for i in range(total_len)]
  ind = 0
  column_count = 0
  for i in range(len(s)):
    matrix_size[ind][column_count] = s[i]
    ind = (ind + 1) % numRows
    column_count += 1
  print(str_matrix)
