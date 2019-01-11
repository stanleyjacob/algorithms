

def removeElement1(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    while True:
        try:
            nums.remove(val)
        except:
        	break

def removeElement2(nums, val):
	"""
	:type nums: List[int]
	:type val: int
	:rtype: int
	"""
	i = 0
	while i != len(nums):
		print(i)
		if nums[i] == val:
			del nums[i] 
		else:
			i += 1

nums = [0, 2, 2, 3, 5, 7]
val = 2
removeElement2(nums, val)
print(nums)
