class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        counter = 1
        prev_string = self.countAndSay(n - 1)
        prev_digit = prev_string[0]
        count_and_say = ""
        for digit in prev_string[1:]:
            if digit == prev_digit:
                counter += 1
            else:
                count_and_say += str(counter) + prev_digit
                prev_digit = digit
                counter = 1
        
        count_and_say += str(counter) + prev_digit
            
        return count_and_say
