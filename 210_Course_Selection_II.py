# Completed July, 15 2026 | 10 minutes

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        from collections import defaultdict

        graph = defaultdict(list)
        taken = []
        count = [0] * numCourses

        for post, pre in prerequisites:
            graph[pre].append(post)
            count[post] += 1

        from collections import deque
        queue = deque([])

        for cours in range(numCourses):
            if not count[cours]:
                queue.append(cours)

        while queue:
            current = queue.popleft()
            taken.append(current)
            for course_no in range(len(graph[current])):
                count[graph[current][course_no]] -= 1
                if not count[graph[current][course_no]]:
                    queue.append(graph[current][course_no])

        if len(taken) == numCourses:
            return taken
        return []