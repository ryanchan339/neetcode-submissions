class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        """
        jsmith@ -> 1
        jnewyork -> 1
        john00 -> 1
        """
        parent = [-1 for _ in range(len(accounts))]
        def find(n):
            if parent[n] < 0:
                return n
            parent[n] = find(parent[n])
            return parent[n]
            

        def union(a, b):
            pa, pb = find(a), find(b)
            if pa == pb:
                return
            if parent[pa] < parent[pb]:
                
                parent[pa] += parent[pb]
                parent[pb] = pa
            else:
                parent[pb] += parent[pa]
                parent[pa] = pb
        etoi = {} # email -> index
        itoa = {} # index -> emails
        for i in range(len(accounts)):
            acc = accounts[i]
            for j in range(1, len(acc)):
                e = acc[j]
                if e not in etoi:
                    etoi[e] = i
                else:
                    union(etoi[e], i)
        for e, i in etoi.items():
            lead = find(i)
            if lead not in itoa:
                itoa[lead] = []
                itoa[lead].append(accounts[lead][0])
            itoa[lead].append(e)
        res = []
        for v in itoa.values():
            res.append([v[0]] + sorted(v[1:]))

        return res

        