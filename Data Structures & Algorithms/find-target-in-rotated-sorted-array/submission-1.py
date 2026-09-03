class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #find the boundary first
        rot =0
        for i in range(len(nums)):
            if nums[i]> nums[-1] and nums[i]>nums[i+1]:
                rot = i+1

        if target < nums[-1] or rot ==0:
            #target in the second half nums[rot+1:]
            left = rot
            right = len(nums) -1
            while left <= right:
                mid = (left + right) //2
                if target == nums[mid]:
                    return mid
                elif target < nums[mid]:
                    right = mid -1
                else:
                    left = mid +1
            return -1
        if target == nums[-1]:
            return len(nums) -1
        else:
            #target in the first half
            left = 0
            right = rot
            while left <= right:
                mid = (left + right) //2
                if target == nums[mid]:
                    return mid
                elif target < nums[mid]:
                    right = mid -1
                else:
                    left = mid +1
            return -1