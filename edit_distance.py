def levenshteinDistance1(str1, str2):
    # Write your code here.
	
	m = len(str1)
	n = len(str2)
	dp_table = [[0 for j in range(n + 1)] for i in range(m + 1)]
	
	for i in range(m + 1):
		for j in range(n + 1):
			if i == 0:
				dp_table[0][j] = j
				continue
			if j == 0:
				dp_table[i][0] = i
				continue
				
			if str1[i - 1] != str2[j - 1]:
				dp_table[i][j] = 1 + min([dp_table[i - 1][j], \
									 dp_table[i][j - 1], \
									dp_table[i-1][j-1]])
			else:
				dp_table[i][j] = dp_table[i-1][j-1]
	return dp_table[m][n]

def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        m = len(s)
        n = len(t)
        
        if abs(m - n) > 1 or (m == 0 and n == 0) or s == t:
            return False
        
        if m == 0 or n == 0:
            return True
        
        def sub_check():
            curr_len = n
            for i in range(curr_len):
                replaced_str = s[:i] + t[i] + s[i+1:] 
                if replaced_str == t:
                    return True
            return False
        
        def insert_check():
            curr_len = n
            curr_str = t
            other_str = s
            if m < n:
                curr_len = m
                curr_str = s
                other_str = t
            
            for i in range(curr_len):
                inserted_str = curr_str[:i] + other_str[i] + curr_str[i:]
                if inserted_str == other_str:
                    return True
            
            for i in range(len(other_str)):
                deleted_str = other_str[:i] + other_str[i+1:]
                if deleted_str == curr_str:
                    return True
            
            return False
        if m == n:
            return sub_check()
        
        else:
            return insert_check()
