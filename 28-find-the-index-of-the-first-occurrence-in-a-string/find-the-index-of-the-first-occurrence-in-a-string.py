class Solution(object):
    def strStr(self, haystack, needle):
        # If needle is an empty string, return 0 (following common convention)
        if not needle:
            return 0

        # Loop through the haystack to find the first occurrence of needle
        for i in range(len(haystack) - len(needle) + 1):
            # Check if the substring from i to i+len(needle) matches needle
            if haystack[i:i+len(needle)] == needle:
                return i  # Return the index of the first occurrence

        # If no match is found, return -1
        return -1

        