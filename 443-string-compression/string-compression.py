class Solution:
    def compress(self, chars: List[str]) -> int:
        i, op_index = 0, 0
        while i < len(chars):
            letter = chars[i]
            count = 0
            while i < len(chars) and letter == chars[i]:
                count += 1
                i += 1
            chars[op_index] = letter
            op_index += 1 
            if count > 1: 
                for ind in str(count):
                    chars[op_index] = ind
                    op_index += 1 
        return op_index





        