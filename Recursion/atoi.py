# String to Integer (atoi)

# The algorithm for myAtoi(string s) is as follows:
# Read in and ignore any leading whitespace.
# Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
# Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
# Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
# If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
# Return the integer as the final result.
# Note:

# Only the space character ' ' is considered a whitespace character.
# Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.

"""
Example 1:

Input: s = "42"
Output: 42
Explanation: The underlined characters are what is read in, the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "42" ("42" is read in)
           ^
The parsed integer is 42.
Since 42 is in the range [-231, 231 - 1], the final result is 42.
"""

class Solution:
    def myAtoi(self, s: str) -> int:
        def func(s, i, n, digitsStarted, ans):
            if i>=n:
                return ans
            if digitsStarted:    
                if s[i] in '1234567890':
                    ans = ans*10 + int(s[i])
                    return func(s, i+1,n, True, ans)
                else:
                    return ans
            if s[i] == ' ':
                return func(s, i+1,n, False, ans)
                
            if s[i] == '-':
                return -1 * func(s, i+1,n, True, ans)

            if s[i] == '+':
                return func(s, i+1,n, True, ans)
                        
            if s[i] in '1234567890':
                return func(s, i+1, n, True, int(s[i]))
            return 0

        ans = func(s, 0, len(s), False, 0)
        if ans < -2**31:
            return -2**31
        elif ans> 2**31 - 1:
            return 2**31 - 1
        else:
            return ans