class Solution {
public:
    bool carPooling(vector<vector<int>>& trips, int capacity) {
         vector<int> timestamp(1001);
        
        for (auto t : trips) {
            timestamp[t[1]] += t[0];
            timestamp[t[2]] -= t[0];
        }
        
        int curr_capacity = 0;
        for (int i = 0; i < 1001; i++) {
            curr_capacity += timestamp[i];
            if (curr_capacity > capacity) {
                return false;
            }
        }
        
        return true;
    }
};
