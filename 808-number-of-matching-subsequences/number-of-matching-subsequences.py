from collections import deque
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        bucket=defaultdict(deque)
        for i in range(len(words)):
            bucket[words[i][0]].append(words[i])
        count=0
        for i in s:
            queue_array=bucket[i]
            for j in range(len(queue_array)):
                ele=queue_array.popleft()
                if len(ele[1:])==0:
                    count+=1
                else:
                    bucket[ele[1]].append(ele[1:])
        return count

        
        