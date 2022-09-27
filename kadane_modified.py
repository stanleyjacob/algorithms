
def largestVar(s: str):
  freq = {i:0 for i in range(26)}
  for i in range(len(s)):
    freq[(int) (chr(i) - 'a')] += 1
  
  max_var = 0
  for a in range(26):
    for b in range(26):
      left_a = freq[a]
      left_b = freq[b]
      
