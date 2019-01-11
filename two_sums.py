def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    contains_dict = {}
    for i, curr_num in enumerate(nums):
        contains_dict[curr_num] = i
    # print(contains_dict.values())
    for i, curr_num in enumerate(nums):
        remainder = target - nums[i]

        if remainder in contains_dict.keys():
            other_index = contains_dict[remainder]
            if i == other_index:
                continue
            return [i, other_index]
