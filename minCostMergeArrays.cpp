
#include <vector>
#include <iostream>
#include <algorithm>
#include <numeric>

int mergeArrays(std::vector<int>& arr, int k) {

	size_t n = arr.size();
	if ((n - 1) % (k - 1)) {
		return -1;
	}

	std::vector<int> prefix(n + 1);
	for (size_t i = 0; i < n; ++i) {
		prefix[i + 1] = prefix[i] + arr[i];
	}

	// 2d grid n x n for bottom-up dynamic programming
	std::vector<std::vector<int>> dp(n, std::vector<int>(n));

	// outer loop from k to end of array
	for (int outer_ind = k; outer_ind <= n; ++outer_ind) {
		for (int inner_ind = 0; (inner_ind + outer_ind) <= n; ++inner_ind) {
			int j = inner_ind + outer_ind - 1;

			int* val = &dp[inner_ind][j];
			*val = INT_MAX;
			for (int mid = inner_ind; mid < j; mid += (k - 1)) {
				*val = std::min(*val,
					dp[inner_ind][mid] + dp[mid + 1][j]);
				// std::cout << *val << " ";
			}
			if ((j - inner_ind) % (k - 1) == 0) {
				*val += prefix[j + 1] - prefix[inner_ind];
				// std::cout << *val << " ";
			}
		}
		// std::cout << std::endl;
	}

	return dp[0][n - 1];

}

int main() {

	std::vector<int> x = { 1, 3, 4, 5, 234, 2, 23, 231, 11 };
	int y = 5;
	std::cout << mergeArrays(x, y) << std::endl;

	return 0;
}
