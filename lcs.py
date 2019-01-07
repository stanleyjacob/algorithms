
def lcs_length(string1, string2, int m, int n):
  if m == 0 or n == 0:
    return 0
  
  if string1[m - 1] == string2[n - 1]:
    return lcs_length(string1, string2, m - 1, n - 1) + 1
  
  return max(lcs_length(string1, string2, m, n - 1), \
    lcs_length(string1, string2, m - 1, n)
  
def main():
  x = 'ser'
  y = 'erd'
  print('Length: ' + lcs_length(x, y, len(x), len(y))
  
