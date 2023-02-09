class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        int i = 0;
        int j = 0;
        int t = 0 ;
        int mx = 0;
        while(j < nums.size())
        {
            if(nums[j]==0){
              if(k>0){
                t++;
                k--;
                j++;
                
              }
              else if(k<=0){
                k = (nums[i]==0)?k+1 : k ;
              i++;
              }
             
            }
            else{
              j++;
            }
           mx = max(mx,j-i);
        }
        return mx;
    }
};
