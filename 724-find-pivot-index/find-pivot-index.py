class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sumLeft, sumRight = 0, sum(nums)
        for idx, ele in enumerate(nums):
            sumLeft += ele
            if  (sumLeft == sumRight):
                return idx
            sumRight -= ele
        return -1 
            
        