class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        count = 0
        idx = []
        for i in nums:
            # each time the zero appears then increment count and append its index in idx
            if i == 0:
                count += 1
                idx.append(j)
            # the number of times the loop has been run
            j += 1
      
        for i in range(len(idx)):
            # equating k equal to last item in the idx list each time 
            k = idx[-1]
            # pops the element from nums list with the help of index present in the idx list
            nums.pop(k)
            # pops the last element from the idx list also as that index element has been removed from the nums list
            idx.pop()
        for i in range(count):
            # appends the number of zeroes that had been removed from the list
            nums.append(0)
        # returns a list with zeroes at the end of the array
        return nums
        