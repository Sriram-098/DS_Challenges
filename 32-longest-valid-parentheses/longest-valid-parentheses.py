class Solution:
    def longestValidParentheses(self, s: str) -> int:
        st=[-1]
        maxlen=0
        for i,char in enumerate(s):
            if char=="(":
                st.append(i)
            else:
                st.pop()
                if not st:
                    st.append(i)
                else:
                    maxlen=max(maxlen,i-st[-1])
        return maxlen
            