class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        result = 0
        for _ in range(32):
            result <<= 1
            result += n & 1
            n >>= 1
        return result


if __name__ == "__main__":
    solution = Solution()