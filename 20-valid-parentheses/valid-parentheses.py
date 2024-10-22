class Solution(object):
    def isValid(self, s):
        # Define the mapping of open to close brackets
        open_brackets = ['(', '{', '[']
        close_brackets = [')', '}', ']']
        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []
        
        # First, check if the length of the string is odd, if so return False
        if len(s) % 2 != 0:
            return False
        
        # Traverse the string
        for char in s:
            if char in open_brackets:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)
            elif char in close_brackets:
                # If it's a closing bracket, check if the stack is empty
                if not stack:
                    return False
                # Pop the last opening bracket from the stack
                last_open_bracket = stack.pop()
                # Check if the last opening bracket matches the current closing bracket
                if bracket_map[char] != last_open_bracket:
                    return False
        
        # At the end, the stack should be empty if all brackets matched
        return not stack
