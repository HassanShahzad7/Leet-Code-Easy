class Solution:

    def isHappy(self, num: int) -> bool:
        summ = []
        # equating sum to the sum of squares of all the numbers in the list 
        # the number given in the argument is converted into a list
        summ = sum([int(n)*int(n) for n in list(str(num))])
        i=0
        # loop terminates only if summ == 1 and i = 20 
        while summ!=1 and i!=20:
            summ = sum([int(n)*int(n) for n in list(str(summ))])
            i+=1
        # if the number is happy that is if its sum is equal to 1 then return True
        if (summ==1):
            return(True)
        else: 
            return(False)