class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            sz = len(s)
            encoded += str(sz) + "#" + s
        return encoded
    def decode(self, s: str) -> List[str]:
        num = ""
        decoded = []
        i = 0
        while i < len(s):
            while i < len(s) and s[i] != '#':
                num += s[i]
                i += 1
            end = i + int(num) + 1
            decoded.append("".join(s[i+1:end]))
            num = ""
            i = end
        return decoded