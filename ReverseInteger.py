class Solution:
    def reverse(self, number: int) -> int:
        b = []
        num = number
        
        if number < 0:
            number = number * -1
        a = len(str(number))
        c = number % 10
        b.append(str(c))
        for i in range(a-1):
            number = int(number / 10)
            c = number % 10
            b.append(str(c))
        s = ""
        s = int(s.join(b))
        if num < 0:
            s = s * -1
        if s < -2147483648 or s > 2147483647:
            return 0
        return s