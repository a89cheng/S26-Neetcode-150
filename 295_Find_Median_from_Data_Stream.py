# Completed June, 15 2026 | 33 minutes

class MedianFinder:
    import heapq

    def __init__(self):
        self.top_half = []
        self.bottom_half = []

        heapq.heapify(self.top_half)
        heapq.heapify(self.bottom_half)

    def addNum(self, num: int) -> None:
        # Need to always keep it balanced, or the bottom half

        # If BOTH are empty, push to top half
        if not self.top_half and not self.bottom_half:
            heapq.heappush(self.top_half, num)
        # At this point, there should always be something at the top half
        else:
            if num > self.top_half[0]:
                heapq.heappush(self.top_half, num)
            else:
                heapq.heappush(self.bottom_half, -num)

        # I need to rebalance since they should always only be off by 1:
        if len(self.top_half) > len(self.bottom_half) + 1:
            first_top = heapq.heappop(self.top_half)
            heapq.heappush(self.bottom_half, -first_top)
        elif len(self.top_half) + 1 < len(self.bottom_half):
            last_bottom = heapq.heappop(self.bottom_half)
            heapq.heappush(self.top_half, -last_bottom)

        # Example [-5,-4,-1] [6,8,10]
        # it goes 1,4,5,6,8,10 and the 2 first indices are counted for even

    def findMedian(self) -> float:
        if len(self.top_half) == len(self.bottom_half):
            return (-self.bottom_half[0] + self.top_half[0]) / 2
        else:
            if len(self.top_half) > len(self.bottom_half):
                return self.top_half[0]
            else:
                return -self.bottom_half[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()