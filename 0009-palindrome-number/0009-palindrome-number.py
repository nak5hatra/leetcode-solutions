class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        temp_ = str(x)
        if temp_[::-1] == temp_:
            return True
        else:
            False
            
            
        # temp = x
        # rev = 0
        # while temp > 0:
        #     rem = temp % 10
        #     rev = (rev * 10) + rem
        #     temp // 10
        # if rev == x:
        #     return True
        # else:
        #     return False