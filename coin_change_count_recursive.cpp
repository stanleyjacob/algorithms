class Solution {
public:
    int change(int amount, vector<int>& coins) {
        vector<vector<int>> dp_table(amount + 1, vector<int>(coins.size(), -1));
        
        for (int i = 0; i < coins.size(); ++i) {
            dp_table[0][i] = 1;
        }
        
        for (int i = 1; i < (amount + 1); ++i) {
            for (int j = 0; j < coins.size(); ++j) {
                int x = ((i - coins[j]) >= 0) ? dp_table[i - coins[j]][j] : 0;
                int y = (j >= 1) ? dp_table[i][j - 1] : 0;
                dp_table[i][j] = x + y;
            }
        }
        return dp_table[amount][coins.size() - 1];
    }
};
