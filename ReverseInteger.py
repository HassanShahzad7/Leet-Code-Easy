class Solution:
    def reverse(self, number: int) -> int:
        # initializing an empty list
        b = []
        # equating num to number
        num = number
        
        # if number specified is negative, making it positive, its negative sign will be dealt later
        if number < 0:
            number = number * -1
        # converting the number to string and equating its length to a
        a = len(str(number))
        # finding modulus 10 of the number in order to take into account the last digit in the number
        c = number % 10
        # appending the number to b list
        b.append(str(c))
        # 1 is subtracted from the range as the last digit is already taken into account
        for i in range(a-1):
            # dividing the number by 10 and cast it to int for it to become a whole number
            number = int(number / 10)
            # finding modulus 10 of the number in order to take into account the last digit in the number
            c = number % 10
            b.append(str(c))
        # as the numbers were added as a separate entries in the list, for it to become a number we use join method
        s = ""
        s = int(s.join(b))
        # if the number was originally negative then multiply s with -1 
        if num < 0:
            s = s * -1
        # for the number to be in the range [-2^31 - 2^31 -1], if no then return 0
        if s < -2147483648 or s > 2147483647:
            return 0
        return s