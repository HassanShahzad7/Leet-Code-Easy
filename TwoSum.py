class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
	
	# initializing an empty dictionary 
        hashmap = dict()

        for i in range(len(nums)):

	    # if the number exists in hashmap as a key then return a tuple
            if nums[i] in hashmap.keys():
                return (i, hashmap[nums[i]])
	    
            else:
		# setting diff equal to the difference of target and entries in the array
                diff = target - nums[i]
		# setting the dictionary key values to the loop variable
                hashmap[diff] = i