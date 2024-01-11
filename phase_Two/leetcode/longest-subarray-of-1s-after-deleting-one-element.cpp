class Solution {
public:
    int longestSubarray(vector<int>& nums) {
          int i = 0;
        int j = 0;  
        int k =1 ; 
        int mx = 0;
        while(j < nums.size())
        {
            if(nums[j]==0){
              if(k>0){
              
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
        return mx-1;
    }
};