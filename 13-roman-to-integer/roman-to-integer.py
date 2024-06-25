class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        expRoman = {'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
        skip = False
        i=len(s)-1

        while(i>=0):
            if s[i] in roman:
                if s[i-1]+s[i] in expRoman and i != 0:
                    sum += expRoman[(s[i-1]+s[i])]
                    skip = True
                    i-=1
                if skip ==False:
                    sum += roman[s[i]]
                i-=1
                skip = False

        
        return sum