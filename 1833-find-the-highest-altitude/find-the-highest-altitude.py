class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        h=0
        ch=0
        for i in gain:
            ch+=i
            h=max(h, ch)
        return h
        