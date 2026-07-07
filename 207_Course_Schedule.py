# Completed July, 6 2026 | 62 minutes

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import deque, defaultdict

        # Prerequisite : Courses
        course_load = defaultdict(list)

        # Number of prereqs.
        prereqs = [0] * numCourses

        # Courses that are now "taken":
        taken = 0

        for course in prerequisites:
            course_load[course[1]].append(course[0])
            prereqs[course[0]] += 1

        # Setup the
        queue = deque()

        for course in range(numCourses):
            if prereqs[course] == 0:
                queue.append(course)

        # If there are still values in the queue...
        while queue and taken < numCourses:
            takes = len(queue)
            for course in range(takes):
                for ready in course_load[queue.popleft()]:
                    prereqs[ready] -= 1
                    if not prereqs[ready]:
                        queue.append(ready)

            taken += takes

        return taken >= numCourses