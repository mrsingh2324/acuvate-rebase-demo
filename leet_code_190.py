class Solution:
    def reverseBits(self, n: int) -> int:
        a=bin(n)[2:].zfill(32)
        reverse=a[::-1]
        return (int(reverse,2))