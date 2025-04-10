class Solution {
    
    public List<List<String>> solveNQueens(int n) {
        List<List<String>> res=new ArrayList<>();
        char [][]arr=new char[n][n];
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                arr[i][j]='.';
            }
        }
        solve(0,n,arr,res);
        return res;
       
    }
    boolean su(int i,int j,char[][]arr){
        while(i>=0){
            if(arr[i][j]=='Q'){
                return false;
            }
            i--;
        }
        return true;
        
    }
    boolean lu(int i,int j,char[][]arr){
         while(i>=0&&j>=0){
            if(arr[i][j]=='Q'){
                return false;
            }
            i--;
             j--;
        }
        return true;
    }
    boolean ru(int i,int j,int n,char[][]arr){
         while(i>=0&&j>=0 && j<n){
            if(arr[i][j]=='Q'){
                return false;
            }
            i--;
             j++;
        }
        return true;
        
    }
    List<String> construct(char[][]arr){
      List<String> res =new ArrayList<>();
        for(int i=0;i<arr.length;i++){
            res.add(new String(arr[i]));
        }
        return res;
    }
    void solve(int i,int n,char[][]arr,List<List<String>> res){
        if(i==n){
            res.add(construct(arr));
            return;
        }
        for(int j=0;j<n;j++){
            if(su(i,j,arr)&&lu(i,j,arr)&&ru(i,j,n,arr)){
                arr[i][j]='Q';
                solve(i+1,n,arr,res);
                arr[i][j]='.';
            }
        }
    }
}
