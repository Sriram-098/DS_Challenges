class Solution {
    public int maximumSum(int[] nums) {
        HashMap<Integer,Integer> map=new HashMap<>();
        int maxi=-1;
        for(int i=0;i<nums.length;i++){
           int sum_digits=f(nums[i]);
           if(map.containsKey(sum_digits)){
             int ans=map.get(sum_digits);
             if(nums[i]>map.get(sum_digits)){
                map.put(sum_digits,nums[i]);
             }
             ans+=nums[i];
             maxi=Math.max(maxi,ans);
           }
           else{
            map.put(sum_digits,nums[i]);
           }
        }
        return maxi;
    }
    public static int f(int n){
        int ans=0;
        while(n>0){
            int rem=n%10;
            ans+=rem;
            n=n/10;
        }
        return ans;
    }
}