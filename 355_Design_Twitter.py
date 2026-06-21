# Completed June, 15 2026 | 68 minutes

class Twitter:
    import heapq

    def __init__(self):
        self.twitter = {}
        self.users = {}
        self.counter = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.twitter[userId] = self.twitter.get(userId, [])
        self.twitter[userId].append((self.counter, tweetId))
        self.counter -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        users = {userId}
        if userId in self.users:
            users = users | self.users[userId]

        heap = []

        for uuid in users:
            if uuid in self.twitter:
                for post in self.twitter[uuid]:
                    heapq.heappush(heap, post)

        results = []

        while heap and len(results) < 10:
            recent = heapq.heappop(heap)
            results.append(recent[1])

        return results

    def follow(self, followerId: int, followeeId: int) -> None:
        # Just the following
        if followerId not in self.users:
            self.users[followerId] = set()
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Just the following
        if followerId in self.users:
            self.users[followerId].discard(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

