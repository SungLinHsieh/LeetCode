class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        while x%10 == 0 and x !=0:
            x=x/10
        s = list(str(x))
        s.reverse()
        if s[-1] == '-':
            s= ['-'] + s[:-1]
        n=int("".join(s))
        if n <= 2147483647 and n >= -2147483647 :
            return n
        else:
            return 0
