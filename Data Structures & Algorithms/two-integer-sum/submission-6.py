class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x in nums:
            i=nums.index(x)
            b = target - x
            if b==x:
                if nums.count(b) != 1:
                    nums.remove(x)
                    for y in nums:
                        if b==y:
                            j=nums.index(b) + 1
                            return [i,j]
            else:
                for y in nums:
                    if y==b:
                        j=nums.index(y)
                        return [i,j]