class Solution:
    #Solution 1
    def divide(self, dividend: int, divisor: int) -> int:
        #Approach: Bit Manipulation
        #Time Complexity: O(log n)
        #Space Complexity: O(1)
        #where, n = abs(dividend)
        
        MIN_INT = -2147483648       # -2**31
        MAX_INT = 2147483647        # 2**31 - 1
        
        #integer overflow
        if divisor == 0 or (dividend == MIN_INT and divisor == -1):
            return MAX_INT
        
        neg_flag = False
        if dividend < 0:
            neg_flag = not neg_flag
            dividend = -dividend
        if divisor < 0:
            neg_flag = not neg_flag
            divisor = -divisor
        
        result = 0
        while dividend >= divisor:
            numShifts = 0
            while dividend >= (divisor << numShifts):   #bitwise left-shift
                numShifts += 1
            numShifts -= 1
            
            dividend -= (divisor << numShifts)          # -= divisor * 2^numShifts
            result += (1 << numShifts)                  # += 2^numShifts
            
        return -result if neg_flag else result
    
    #Solution 2
    """
    def divide(self, dividend: int, divisor: int) -> int:
        #Approach: Repeated Subtraction
        #Time Complexity: O(n)
        #Space Complexity: O(1)
        #where, n = abs(dividend)
        
        MIN_INT = -2147483648       # -2**31
        MAX_INT = 2147483647        # 2**31 - 1
        
        #integer overflow
        if divisor == 0 or (dividend == MIN_INT and divisor == -1):
            return MAX_INT
        
        neg_flag = False
        if dividend < 0:
            neg_flag = not neg_flag
            dividend = -dividend
        if divisor < 0:
            neg_flag = not neg_flag
            divisor = -divisor
        
        result = 0
        while dividend >= divisor:
            dividend -= divisor
            result += 1
            
        return -result if neg_flag else result
    """
