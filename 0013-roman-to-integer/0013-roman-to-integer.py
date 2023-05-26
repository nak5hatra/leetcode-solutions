class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # Loop through each character in the string containing the roman numerals.
        # Compare the value of the current roman symbol with the value of the roman symbol to its right.
        # If the current value is greater than or equal to the value of the symbol to the right, add the current symbol’s value to the total.
        # If the current value is smaller than the value of the symbol to the right, subtract the current symbol’s value from the total.
        num = 0
        dic={"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
        for i in range(len(s)-1):
            if dic[s[i]] < dic[s[i+1]]:
                num = num - dic[s[i]]
            else:
                num = num + dic[s[i]]
        return num + dic[s[-1]]
        