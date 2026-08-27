class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        

        
        # need to go through tasks to find what needs to be enqueued
        # when enqueue into heap include (protime, index)
        """
        res = 1, 4, 3, 2
        [[1,5],[2,4],[3,2],[4,1]]
        [2,4],[3,2],
        """
        for i, a in enumerate(tasks):
            e, p = a
            tasks[i] = [e, p, i]
        tasks.sort()
        ptr = 0
        heap = [] #minheap
        res = []
        #check cpu time
        #if nothing to enqueue at this cpu time, skip to nearest enqueue time
        #put things on the heap with enqueue before or at this time
        #process top of heap element
        #repeat until heap is empty
        time = 0

        while ptr < len(tasks) or heap:
            if not heap:
                time = max(time, tasks[ptr][0])
            while ptr < len(tasks) and tasks[ptr][0] <= time:
                heapq.heappush(heap, (tasks[ptr][1], tasks[ptr][2])) # processtime, index
                ptr += 1
            
                
            protime, index = heapq.heappop(heap)
            time += protime
            res.append(index)
            
        return res