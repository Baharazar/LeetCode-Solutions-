class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        while s != '':
            if '()' in s:
                x = s.split('()')
                s = ''
                for item in x:
                    s = s + item
            elif '[]' in s:
                x = s.split('[]')
                s = ''
                for item in x:
                    s = s + item
            elif ('{'+'}') in s:
                x = s.split(('{'+'}'))
                s = ''
                for item in x:
                    s = s + item
            else: 
                return False
                break
        
        return True