# Completed June, 11 2026 | 52 minutes

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        import heapq

        count = {}
        heap = []

        # Highest counts are in negative
        for task in tasks:
            count[task] = count.get(task, 0) - 1
        for letter, times in count.items():
            heap.append((times, letter))
        heapq.heapify(heap)

        time = 0

        saves = []
        heapq.heapify(saves)

        while saves or heap:
            if heap:
                # This is the (time, letter) tuple
                high = heapq.heappop(heap)
                high = list(high)
                (high)[0] += 1
                high = tuple(high)

                if high[0]:
                    heapq.heappush(saves, (time + n + 1, high))

            time += 1

            while saves and saves[0][0] <= time:
                renewed = heapq.heappop(saves)
                heapq.heappush(heap, renewed[1])

        return time