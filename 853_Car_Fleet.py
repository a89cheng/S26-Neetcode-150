# Completed May 14, 2026 | 20 minutes

class Solution:
    def carFleet(self, target: int, position: List[int],
                 speed: List[int]) -> int:
        if len(position) == 1:
            return 1

        sorted_zipped = sorted(zip(position, speed))
        theoretical = []

        for pair in sorted_zipped:
            time = (target - pair[0]) / pair[1]
            theoretical.append(time)

        counter = 1
        theoretical.reverse()

        for time in range(1, len(position)):
            if theoretical[time] > theoretical[time - 1]:
                counter += 1
            else:
                theoretical[time] = theoretical[time - 1]

        return counter

