# Completed April, 23 2026 | 27 minutes

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        letters = {}
        part = {}


        for i in range(len(s1)):
            if s1[i] not in letters:
                letters[s1[i]] = 1
            else:
                letters[s1[i]] += 1

        left = 0

        for right in range(len(s2)):
            if s2[right] not in part:
                part[s2[right]] = 1
            else:
                part[s2[right]] += 1

            if right - left + 1 > len(s1):
                part[s2[left]] -= 1
                #This is the part I messed up; deleting
                #the key of the window!
                if part[s2[left]] == 0:
                    del part[s2[left]]
                left += 1

            if part == letters:
                return True

        return False

