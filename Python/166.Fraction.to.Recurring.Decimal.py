class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        int_part, rem = divmod(abs(numerator), abs(denominator))
        remlist = list()
        sign = "-" if numerator*denominator<0 else ""
        result = [sign+str(int_part)+"."]
        while rem not in remlist:
            remlist.append(rem)
            digit, rem = divmod(10*rem, abs(denominator))
            result.append(str(digit))
            
        result.insert(remlist.index(rem)+1,"(")
        result.append(")")
        return "".join(result).replace("(0)","").rstrip(".")
