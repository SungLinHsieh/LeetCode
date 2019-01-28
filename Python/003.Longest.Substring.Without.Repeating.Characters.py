class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_dict = {}
        max_len = 0
        left_index = 0
        for right_index, char in enumerate(s):
            if char in char_dict:
                left_index = max(left_index, char_dict[char] + 1)
            max_len = max(max_len, right_index - left_index +1)
            char_dict[char] = right_index
        return max_len
