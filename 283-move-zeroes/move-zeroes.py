class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        
        for num in range(len(nums)):
            if nums[num] != 0:
                nums[left] , nums[num] = nums[num] , nums[left]
                left += 1
