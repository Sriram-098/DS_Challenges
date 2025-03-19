class Solution {
public:
    int minOperations(vector<int>& nums) {
        int r=0;
        int count=0;
        while(r<nums.size()){

            if (nums[r]==0){
                if(r+2<nums.size()){
                    for(int i=r;i<r+3;i++){
                        nums[i]=1-nums[i];
                    }
                    count++;
                }
            }
            r+=1;
        }
        for(int i=0;i<nums.size();i++){
            if(nums[i]==0){
                return -1;
            }
        }
        return count;
    }
};