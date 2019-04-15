import sys

# maximize the subset sums
# with the constraint that requests
# 1 to n have weights 
def subset_sum(weights_lst, n, W):
	if W < 0:
		return None
	m_table = [[0 for i in range(W + 1)] \
		for j in range(n + 1)]
	for i in range(1, n + 1):
		for w in range(W + 1):
			if weights_lst[i - 1] > w:
				m_table[i][w] = m_table[i - 1][w]
			else:
				m_table[i][w] = max(m_table[i - 1][w], weights_lst[i - 1] + m_table[i - 1][w - weights_lst[i - 1]])

	return m_table[n][W]

weights_lst = [3, 8, 12, 4, 9]
W = 3603555 # terminate quickly if exceeds the sum of the possible weights
res = subset_sum(weights_lst, len(weights_lst), W)
print(res)
print(sum(weights_lst))