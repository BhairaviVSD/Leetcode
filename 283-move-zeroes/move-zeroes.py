class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, ind = 0, 0
        while ind < len(nums):
            if (nums[i]==0):
                nums.append(nums.pop(i))         
            else:
                i+=1
            ind +=1