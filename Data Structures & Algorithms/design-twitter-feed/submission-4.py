class Twitter:

    def __init__(self):
        self.following = {} # userid -> set() userids
        self.posts = {} # userid -> [] time, tweetids
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.posts:
            self.posts[userId] = []
        self.posts[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        follow_list = None
        if userId in self.following:
            follow_list = self.following[userId].copy()
            for f in follow_list:
                if f in self.posts:
                    post_list = self.posts[f]
                    for p in post_list:
                        heap.append(p)
        if userId in self.posts:
            for p in self.posts[userId]:
                heap.append(p)
        heapq.heapify_max(heap)
        res = []
        for i in range(10):
            if not heap:
                break
            res.append(heapq.heappop_max(heap)[1])

        self.time += 1
        return res
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followerId not in self.following:
            self.following[followerId] = set()
        self.following[followerId].add(followeeId)
        self.time += 1

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].discard(followeeId)
        self.time += 1


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)