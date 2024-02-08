class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split()
        l = len(arr)
        rev = ""
        for i in range(l):
            rev = rev + arr.pop() + " "
        return rev.strip()

        