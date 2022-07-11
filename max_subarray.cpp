class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int max_sum = INT_MIN;
        int curr_sum = 0;
        // unordered_map<pair<int, int>, int> range_sum_map;
        for (int start_ind = 0; start_ind < nums.size(); ++start_ind) {
            curr_sum = max(curr_sum + nums[start_ind], nums[start_ind]);
            max_sum = max(curr_sum, max_sum);
        }
        return max_sum;
    }
};
