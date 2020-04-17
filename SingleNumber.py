class Solution:
	def singleNumber(self, nums: List[int]) -> int:
		# initializing an empty dictionary
		hashmap = dict()
		# since in dictionary there are unique keys so only unique keys will be assigned a value of 0
	    for i in nums:
	        hashmap[i] = 0  
	    # iterating through each element in the list and increment each hashmap key value by 1 each time an element comes that is already in the hashmap keys
	    for i in nums:
	        hashmap[i] += 1
	    # the hashmap key that only appeared once or whose key has correspondence value of 1 is returned
	    for idx, vals in hashmap.items():
	        if vals == 1:
	            return(idx)
        