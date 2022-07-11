class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int, int> nums_to_count_map;
        for (int& num: nums) {
            auto it = nums_to_count_map.find(num);
            if (it == nums_to_count_map.end()) {
                nums_to_count_map.insert( {num, 1} );
            }
            else {
                return true;
            }
        }
        return false;
    }
};
