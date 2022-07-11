class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int max_sum = INT_MIN;
        for (int start_ind = 0; start_ind < nums.size(); ++start_ind) {
            for (int end_ind = start_ind; end_ind < nums.size(); ++ end_ind) {
                accumulate(nums.begin() + start_ind, nums.begin() + end_ind, 
                          decltype(nums)::value_type(0));
            }
        }
        return max_sum;
    }
};
