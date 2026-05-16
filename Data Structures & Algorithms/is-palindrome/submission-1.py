class Solution:
    def isAlfanumerical(self, s: str) -> bool:
        a = ord(s[0])
        return ((a >= ord('a') and a <= ord('z')) or 
            (a >= ord('A') and a <= ord('Z')) or
            (a >= ord('0') and a <= ord('9')))

    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
                continue

            if not self.isAlfanumerical(s[i]):
                i += 1
                continue
            if not self.isAlfanumerical(s[j]):
                j -= 1
                continue
            
            diff = ord('a') - ord('A')
            a, b = ord(s[i]), ord(s[j])
            if a >= ord('a'):
                if b == (a - diff):
                    i += 1
                    j -= 1
                    continue
                return False
            if b >= ord('a'):
                if a == (b - diff):
                    i += 1
                    j -= 1
                    continue
                return False
            return False
        return True

