class Solution {
public:
    static bool cbrt(long long x, int& n){
        if(x > n) return false;
        if(x == n) return true;
        return cbrt(x*3, n);
    }
    bool isPowerOfThree(int n) {
        return cbrt(1,n);
    }
};