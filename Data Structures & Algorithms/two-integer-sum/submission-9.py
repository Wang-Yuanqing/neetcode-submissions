class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}                          # value -> index
        for i, x in enumerate(nums):
            b = target - x
            if b in seen:
                return [seen[b], i]        # earlier index first
            seen[x] = i                    # store AFTER the check