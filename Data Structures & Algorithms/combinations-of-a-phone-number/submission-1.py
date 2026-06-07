class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        mapping = {
            '2' : ['a','b','c'],
            '3' : ['d','e','f'],
            '4' : ['g','h','i'],
            '5' : ['j','k','l'],
            '6' : ['m','n','o'],
            '7' : ['p','q','r','s'],
            '8' : ['t','u','v'],
            '9' : ['w','x','y','z']
        }
        if len(digits) == 0:
            return []
        def dfs(i, arr):
            letters = mapping[digits[i]]
            for l in letters:
                arr.append(l)
                if i == len(digits) - 1:
                    res.append("".join(arr))
                    arr.pop()
                    continue
                dfs(i + 1, arr)
                arr.pop()
        dfs(0,[])
        return res

            
            