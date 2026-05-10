class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        a = ord('a')
        for s in strs:
            letters = [0] * 26
            for c in s:
                letters[ord(c) - a] += 1            
            anagrams.setdefault(tuple(letters), []).append(s)
        return list(anagrams.values())