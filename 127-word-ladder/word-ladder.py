class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordset=set(wordList)
        q=deque()
        q.append((beginWord,1))
        if endWord not in wordset:
            return 0
        while q:
            word,steps=q.popleft()
            for i in range(len(word)):
                alpha="abcdefghijklmnopqrstuvwxyz"
                for letter in alpha:
                    newword=word[:i]+letter+word[i+1:]
                    if newword == endWord:
                        return steps+1
                    if newword in wordset:
                        wordset.remove(newword)
                        q.append((newword,steps+1))
        return 0
                
        