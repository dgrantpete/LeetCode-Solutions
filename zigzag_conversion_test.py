# https://leetcode.com/problems/zigzag-conversion/

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        rows = []

        total = 0
        is_reversed = False

        while total < len(s):
            next_amount = total + numRows
            if not is_reversed:
                append_val = s[total:next_amount]
                rows.append(f"{append_val:{numRows}}")
            else:
                next_amount -= 2
                append_val = s[next_amount - 1:total - 1:-1]
                rows.append(f"{append_val:>{numRows - 1}} ")
            is_reversed = not is_reversed
            total = next_amount
        return "".join("".join(char for char in chars if char != " ") for chars in zip(*rows))

# Test cases

def test_convert():
    s = Solution()
    assert s.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
    assert s.convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
    assert s.convert("A", 1) == "A"
    assert s.convert("AB", 1) == "AB"
    assert s.convert("ABCD", 2) == "ACBD"
    assert s.convert("ABCD", 3) == "ABDC"
    assert s.convert("ABCD", 4) == "ABCD"
    assert s.convert("ABCDE", 4) == "ABCED"
    assert s.convert("ABCDE", 5) == "ABCDE"
