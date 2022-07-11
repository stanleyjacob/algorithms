class Solution {
public:
    int rob(vector<int>& nums) {
        
        if (nums.size() == 0) {
            return 0;
        }
        if (nums.size() == 1) {
            return nums[0];
        }
        
        vector<int> dp_table(nums.size());
        dp_table[0] = nums[0];
        dp_table[1] = max(nums[1], dp_table[0]);
        for (int i = 2; i < nums.size(); ++i) {
            dp_table[i] = max(dp_table[i - 2] + nums[i], dp_table[i - 1]);
        }
        
        return dp_table[nums.size() - 1];
    }
};
