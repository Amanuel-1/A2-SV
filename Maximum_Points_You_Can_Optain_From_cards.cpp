class Solution {
public:
    int maxScore(vector<int>& cardPoints, int k) {
       int maxSum = 0;
    int sum = 0;
    // Compute the sum of the last k cards
    for (int i = cardPoints.size() - k; i < cardPoints.size(); i++) {
        sum += cardPoints[i];
    }
    maxSum = max(maxSum, sum);
    // Compute the other sums
    for (int i = cardPoints.size() - k + 1; i <= cardPoints.size(); i++) {
        sum = sum - cardPoints[i - 1] + cardPoints[(i - 1 + k) % cardPoints.size()];
        maxSum = max(maxSum, sum);
    }
    return maxSum;

    }
};
