class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        if len(a) > len(b):
            b = '0' * (len(a) - len(b)) + b
        if len(a) < len(b):
            a = '0' * (len(b) - len(a)) + a

        result = ''
        carry = 0
        for i in range(len(a) - 1, -1, -1):
            r = carry
            r += 1 if a[i] == '1' else 0
            r += 1 if b[i] == '1' else 0
            result = ('1' if r % 2 == 1 else '0') + result
            carry = 0 if r < 2 else 1  # Compute the carry.

        if carry != 0: result = '1' + result
        return result