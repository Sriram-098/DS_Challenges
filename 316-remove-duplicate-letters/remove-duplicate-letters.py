class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        freq=Counter(s)
        st=[]
        se=set()
        for i in range(len(s)):
            freq[s[i]]-=1
            if s[i] in se:
                continue

            while st and st[-1]>s[i] and freq[st[-1]]>=1:
                popped=st.pop()
                se.remove(popped)
            
            se.add(s[i])
            st.append(s[i])
            print(s,st)
        return "".join(st)
        
        # freq=Counter(s)
        # se=set()
        # st=[]
        # for i in range(len(s)):
        #     freq[s[i]]-=1
        #     if s[i] in se:
        #         continue
        #     while st and st[-1]>s[i] and freq[st[-1]]>=1:
        #         popped=st.pop()
        #         se.remove(popped)
                

        #     st.append(s[i])
        #     se.add(s[i])
        # print(st)
        # return "".join(st)