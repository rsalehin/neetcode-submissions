class Solution:
    def reverseBits(self, n: int) -> int:
        binary = ''
        for i in range(32):
            if n & (1<<i):
                binary += '1'
            else:
                binary += '0'
        
        length = len(binary)
        decimal_value = 0
        for i in range(length):
            bit = int(binary[i])
            decimal_value += bit*2**(length-1-i)
        return decimal_value

        
