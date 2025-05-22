class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        freq=Counter(s)
        st=[]
        store=set()
        for ch in s:
            freq[ch]-=1
            if ch in store:
                continue
            while st and st[-1]>ch and freq[st[-1]]>0:
                removed=st.pop()
                store.remove(removed)
            
            st.append(ch)
            store.add(ch)
        print(st,s)
        return "".join(st)

        