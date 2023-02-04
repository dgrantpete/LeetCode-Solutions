# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        char_vals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        s += 'I'

        total = 0
        str_iter = zip(s, s[1:])

        for cur_val, next_val in str_iter:
            if char_vals[cur_val] < char_vals[next_val]:
                total += char_vals[next_val] - char_vals[cur_val]
                next(str_iter)
            else:
                total += char_vals[cur_val]

        return total
        
# Test Cases

def test_romanToInt():
    s = Solution()
    assert s.romanToInt("III") == 3
    assert s.romanToInt("IV") == 4
    assert s.romanToInt("IX") == 9
    assert s.romanToInt("LVIII") == 58
    assert s.romanToInt("MCMXCIV") == 1994
    