class Solution {
    public String shortestCommonSupersequence(String s1, String s2) {
        int ind1=s1.length();
        int ind2=s2.length();
      //  int val=f(ind1-1,ind2-1,str1,str2);
       
        int dp[][]=new int[ind1+1][ind2+1];;
        for(int i=0;i<=ind1;i++){
            dp[i][0]=0;
        } 
        for (int j = 0; j <= ind2; j++) {
            dp[0][j] = 0;
        } 
        
        for(int i=1;i<=ind1;i++){
            for(int j=1;j<=ind2;j++){
                
        
            if(s1.charAt(i-1)==s2.charAt(j-1)){
                dp[i][j]= 1+dp[i-1][j-1];
            }else{
            dp[i][j]= Math.max(dp[i-1][j],dp[i][j-1]);
            }
                
            }
        }
        String s="";
        
        
        while(ind1>0 && ind2>0){
            if(s1.charAt(ind1-1)==s2.charAt(ind2-1)){
                s+=s1.charAt(ind1-1);
                ind1--;
                ind2--;
                
            }else if(dp[ind1-1][ind2]<dp[ind1][ind2-1]){
                s+=s2.charAt(ind2-1);
                ind2--;
            }else{
            s+=s1.charAt(ind1-1);
                ind1--;
            }
        }
        while(ind1>0){
            s+=s1.charAt(ind1-1);
            ind1--;
        }
         while(ind2>0){
            s+=s2.charAt(ind2-1);
            ind2--;
        }
        StringBuilder st=new StringBuilder(s);
        return st.reverse().toString();
        
        
                 
        
    }
    int f(int ind1,int ind2,String s1,String s2){
        if(ind1<0||ind2<0){
            return 0;
        }
            if(s1.charAt(ind1)==s2.charAt(ind2)){
                return 1+f(ind1-1,ind2-1,s1,s2);
            }
        return Math.max(f(ind1-1,ind2,s1,s2),f(ind1,ind2-1,s1,s2));
    }
}