class Solution:
    def romanToInt(self, s: str) -> int:

        roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50,
                      "C": 100, "D": 500, "M": 1000}

        sum = roman_dict[s[0]]
        for i in range(1, len(s)):
            if roman_dict[s[i]] > roman_dict[s[i - 1]]:
                sum -= roman_dict[s[i - 1]]
                sum += (roman_dict[s[i]] - roman_dict[s[i - 1]])
            else:
                sum += roman_dict[s[i]]
            print(s[i], sum)
        
        return sum