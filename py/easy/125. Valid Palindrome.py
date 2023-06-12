class Solution:
    def isPalindrome2(self, s: str) -> bool:
        newString = "".join(x for x in s if x.isalnum()).lower()
        return newString == newString[::-1]
        
    def isPalindrome(self, s: str) -> bool:
        lptr = 0
        rptr = len(s) - 1
        while lptr < rptr:
            # reach alnum character
                while lptr < rptr and not s[lptr].isalnum():
                    lptr += 1
                while lptr < rptr and not s[rptr].isalnum():
                    rptr -= 1
                if (lptr < rptr):
                    if (s[lptr].lower() != s[rptr].lower()):
                        return False
                    else:
                        lptr += 1
                        rptr -= 1
        return True