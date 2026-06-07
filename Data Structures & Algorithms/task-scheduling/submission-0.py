class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        counts
        A : 3
        B : 3
        C : 2
        cooldown
        A : 0
        B : 0
        C : 0
        """
        res = 0
   
        counts = {}
        cooldown = {}
        for t in tasks:
            counts[t] = counts.get(t, 0) + 1
            cooldown[t] = 0
        i = 0
        while True:
            
            i += 1
            #add check if everything is zero
            #print("iteration", i)
            if not counts:
                break
            #print("cooldown", cooldown)
            #print("counts",counts)
            currMax = 0
            currTask = "A"
            for t, c in list(cooldown.items()):
                if c == 0 and counts[t] > currMax:
                    currMax = counts[t]
                    currTask = t
            if currMax > 0:
                counts[currTask] -= 1
                cooldown[currTask] = n + 1
                if counts[currTask] == 0:
                    del counts[currTask]
                    del cooldown[currTask]
            res += 1
            for t, c in cooldown.items():
                if c != 0:
                    cooldown[t] -= 1

        return res