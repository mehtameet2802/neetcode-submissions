class Solution:
    def validPalindrome(self, s: str) -> bool:

        def is_palindrome(s1):
            return s1 == s1[::-1]

        l = 0
        r = len(s)-1

        def helper(l,r):
            if l>r:
                return True
            elif s[l] == s[r]:
                return helper(l+1, r-1)
            else:
                check1 = is_palindrome(s[l:r])
                check2 = is_palindrome(s[l+1:r+1])

                if check1 or check2:
                    return True
                return False

        return helper(0,r)