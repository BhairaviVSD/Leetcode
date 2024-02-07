class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxNum, sumGain = 0, 0
        for i in gain:
            sumGain += i
            maxNum = max(maxNum, sumGain)
        return maxNum
        