class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        j = len(digits) - 1
        rem = 0
        add = 0

        while j >= 0:
            add = 1 if j == len(digits) - 1 else 0
            num = (digits[j] + rem + add) % 10
            rem = 0 if digits[j] + rem + add == num else 1
            digits[j] = num
            j -= 1

        if rem == 1:
            digits.insert(0, rem)

        return digits