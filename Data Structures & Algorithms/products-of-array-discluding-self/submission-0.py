class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [nums[0] for i in range(len(nums))] 
        sufix = [nums[-1] for i in range(len(nums))] 

        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i]

        for j in range(len(nums) - 2, -1 , -1):
            sufix[j] = sufix[j + 1] * nums[j]
        
        res = []
        res.append(sufix[1])
        for i in range(1, len(nums) - 1):
            res.append(prefix[i-1]*sufix[i+1])
        res.append(prefix[len(nums)-2])
        return res