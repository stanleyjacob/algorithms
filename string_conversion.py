def convert(s, numRows):
  total_len = len(s)
	#print(total_len)
	str_matrix = [['' for j in range(total_len)] for i in range(numRows)]
	ind = 0
	column_count = 0
	i = 0
	while i != len(s):
		if column_count % 2 == 1 and ind % 2 == 0:
			ind += 1
			if ind == numRows:
				ind = 0
				column_count += 1
			continue
		str_matrix[ind][column_count] = s[i]
		i += 1
		ind += 1
		if ind == numRows:
			ind = 0
			column_count += 1

	final_str = []
	for i in range(numRows):
		#print(str_matrix[i])
		for j in range(len(str_matrix[i])):
			current_char = str_matrix[i][j]
			#print(current_char)
			if current_char != '':
				final_str.append(current_char)
	return ''.join(final_str)
