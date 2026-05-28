class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {nums[i] : i for i in range(len(nums))}
        for i in range(len(nums)):
            if target - nums[i] in hm and hm[target - nums[i]]!= i:
                return [i, hm[target - nums[i]]]

        
        