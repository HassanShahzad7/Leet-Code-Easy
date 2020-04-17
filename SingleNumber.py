class Solution:
	def singleNumber(self, nums: List[int]) -> int:
		hashmap = dict()
	    for i in nums:
	        hashmap[i] = 0  
	    for i in nums:
	        hashmap[i] += 1
	    for idx, vals in hashmap.items():
	        if vals == 1:
	            return(idx)
        