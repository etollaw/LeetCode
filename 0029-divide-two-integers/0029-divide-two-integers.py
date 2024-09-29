class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
           return 2147483647
        if dividend == 0:
           return 0
        if dividend  < 0 and divisor < 0:
            dividend = abs(dividend)
            divisor = abs(divisor)
            quotient = dividend // divisor
            return quotient
        elif dividend  > 0 and divisor > 0:
            quotient = 0
            quotient = dividend // divisor
            return quotient
        elif dividend < 0 or divisor < 0:
            dividend = abs(dividend)
            divisor = abs(divisor)
            quotient = dividend // divisor
            return -quotient
        
        