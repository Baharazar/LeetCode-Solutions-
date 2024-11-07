class Solution(object):
    def divide(self, dividend, divisor):
        # Define the 32-bit signed integer range
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31

        # Handle edge cases
        if divisor == 0:
            return MAX_INT  # Division by zero, not possible (hypothetical, as the problem assumes valid input)
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT  # Prevent overflow
        
        # Determine the sign of the result
        negative = (dividend < 0) != (divisor < 0)

        # Work with absolute values
        dividend, divisor = abs(dividend), abs(divisor)
        
        # Perform the division using subtraction
        quotient = 0
        while dividend >= divisor:
            temp_divisor, multiple = divisor, 1
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1
            dividend -= temp_divisor
            quotient += multiple

        # Apply the sign to the quotient
        if negative:
            quotient = -quotient
        
        # Ensure the result is within the 32-bit signed integer range
        return min(max(MIN_INT, quotient), MAX_INT)
