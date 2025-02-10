class Solution {
    public String clearDigits(String s) {
        Stack<Character> st=new Stack<>();
        char arr[]=s.toCharArray();
        for(int i=0;i<s.length();i++){
            if(Character.isLetter(s.charAt(i))){
                st.push(s.charAt(i));
            }
            else{
                if(!st.isEmpty()){
                    st.pop();
                }
            }
        }
        StringBuilder ans=new StringBuilder();
        while(!st.isEmpty()){
            ans.append(st.pop());
        }
        return ans.reverse().toString();
    }
}