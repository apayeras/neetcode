class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        count = [[] for i in range(len(nums))] 
        repetition = {}
        for elem in nums:
            repetition[elem] = repetition.get(elem, 0) + 1

        for key, value in repetition.items():
            count[value - 1].append(key)

        for i in range(len(nums) - 1, -1, -1):
            for n in count[i]:
                res.append(n)
                if len(res) == k:
                    return res