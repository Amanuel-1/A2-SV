class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        maxSum = 0
        sum = 0
        # Compute the sum of the last k cards
        for i in range(len(cardPoints) - k, len(cardPoints)):
            sum += cardPoints[i]
        maxSum = max(maxSum, sum)
        # Compute the other sums
        for i in range(len(cardPoints) - k + 1, len(cardPoints) + 1):
            sum = sum - cardPoints[i - 1] + cardPoints[(i - 1 + k) % len(cardPoints)]
            maxSum = max(maxSum, sum)
        return maxSum