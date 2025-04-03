class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        count=0
        for i in range(len(strs[0])):
            st=strs[0][i]
            for j in range(len(strs)):
                if i>=len(strs[j]) or strs[j][i]!=st:
                    print(count)
                    return strs[0][0:count]
            count+=1
        print(count)

        return strs[0][0:count]


        

        