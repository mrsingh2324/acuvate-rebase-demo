class Solution(object):
    def romanToInt(self, s):
        roman_values = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        total = 0
        for i in range(len(s)-1):
            current = roman_values[s[i]]
            next_value = roman_values[s[i + 1]]
            if current < next_value:
                total -= current
            else:
                total += current  
        total += roman_values[s[-1]]
        return total          




        
        