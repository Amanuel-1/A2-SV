class Solution {
public:
    int pivotIndex(vector<int>& nums) {
       int total =0,i=0,pre = 0,post=0;
       total =accumulate(nums.begin(),nums.end(),0);
        pre =0;
        post = total - nums[0];

      while(i<nums.size()){
           
            
            post = total - pre-nums[i];
             cout  <<pre <<" " << post <<endl;
          
          if(pre ==post)return i;
             pre += nums[i] ;
          i++;
      }
     return -1 ;
    }
};
