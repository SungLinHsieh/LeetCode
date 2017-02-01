class Solution(object):
    def fizzBuzz(self, n):
        l = list()
        for i in range(n):
            if (i+1)%15==0:
                l.append("FizzBuzz")
            elif (i+1)%3==0:
                l.append("Fizz")
            elif (i+1)%5==0:    
                l.append("Buzz")
            else:
                l.append(str(i+1))
        return l
        """
        :type n: int
        :rtype: List[str]
        """