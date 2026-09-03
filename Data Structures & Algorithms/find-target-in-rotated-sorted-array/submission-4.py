class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums) - 1

        while left < right:
            mid = (left + right) //2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid +1
        rot = left

        # check which side target is in:
        if nums[rot] <= target <= nums[-1]:
            left = rot
            right = len(nums) -1
        else:
            left = 0
            right = rot -1

        # binary search:
        while left <= right:
            mid = (left + right )//2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid -1
            else:
                left = mid +1
        return -1

