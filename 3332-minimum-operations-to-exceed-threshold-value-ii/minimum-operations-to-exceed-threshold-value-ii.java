class Solution {
    public int minOperations(int[] nums, int k) {
        PriorityQueue<Long> pq=new PriorityQueue<>();
        for(int i=0;i<nums.length;i++){
            pq.add((long)nums[i]);
        }
        int count=0;
        while(!pq.isEmpty() && pq.size()>=2){
            long first=pq.poll();
            long second=pq.poll();
            if(first <k ){
                long ans=(Math.min(first,second)*2)+Math.max(first,second);
                pq.add(ans);
                count++;
            }else{
                break;
            }
            
        }
        return count;
    }
}