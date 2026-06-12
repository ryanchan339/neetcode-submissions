class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = {}
        dp[""] = True
        wordDict = set(wordDict)
        def dfs(word):
            if word in dp:
                return dp[word]
            
            for i in range(len(word)):
                if word[:i + 1] in wordDict:
                    if dfs(word[i + 1: ]):
                        dp[word] = True
                        return True
            dp[word] = False
            return False
        return dfs(s)

