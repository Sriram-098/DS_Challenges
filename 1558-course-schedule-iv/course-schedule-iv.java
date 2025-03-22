class Solution {
    public List<Boolean> checkIfPrerequisite(int numCourses, int[][] prerequisites, int[][] queries) {
        List<Boolean> ans=new ArrayList<>();
        ArrayList<ArrayList<Integer>> adj=new ArrayList<>();
        for(int i=0;i<numCourses;i++){
            adj.add(new ArrayList<>());
        }
        for(int i=0;i<prerequisites.length;i++){
            int u=prerequisites[i][0];
            int v=prerequisites[i][1];
            adj.get(u).add(v);
        }
        
        for(int i=0;i<queries.length;i++){
            Stack<Integer> st=new Stack<>();
            boolean visited[]=new boolean[numCourses];
            dfs(queries[i][0],st,visited,adj);
            int flag=0;
             while(!st.isEmpty()){
                 if(st.peek()==queries[i][1]){
                    ans.add(true);
                    flag=1;
                 }
                 st.pop();
             }
             if(flag==0){
             ans.add(false);}
        }
        return ans;
    }
    public static void dfs(int n,Stack<Integer> st,boolean visited[],ArrayList<ArrayList<Integer>> adj){
        visited[n]=true;
        for(int x:adj.get(n)){
            if(visited[x]==false){
                dfs(x,st,visited,adj);
            }
        }
        st.push(n);
    }
}