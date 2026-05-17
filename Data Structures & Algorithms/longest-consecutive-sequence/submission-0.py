class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        cnums = set(nums)
        for num in nums:
            if num - 1 not in cnums:
                counter, val = 1, num + 1
                while val in cnums:
                    counter += 1
                    val += 1
                longest = max(longest, counter)
        return longest