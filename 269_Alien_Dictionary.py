# Completed July 29, 2026 | 109 minutes

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        from collections import defaultdict, deque

        # Graph
        graph = defaultdict(set)
        # Count of how many letters before you, default 0
        counts = defaultdict(int)
        letters = set()

        for word in words:
            for ch in word:
                letters.add(ch)

        prev = words[0]

        # This is only by the first word
        for i in range(1, len(words)):
            curr = words[i]
            if curr == prev:
                continue
            elif len(curr) < len(prev) and prev[:len(curr)] == curr[:]:
                return ""
            else:
                for k in range(min(len(prev), len(curr))):
                    if curr[k] != prev[k]:
                        if curr[k] not in graph[prev[k]]:
                            counts[curr[k]] += 1
                            graph[prev[k]].add(curr[k])
                        break
            prev = curr

        queue = deque([])
        ans = ""

        # Build up the queue
        for letter in letters:
            if not counts[letter]:
                queue.append(letter)

        # Not sure if the second loop is necessary...
        while queue:
            curr = queue.popleft()
            ans = ans + curr

            for letter in graph[curr]:
                counts[letter] -= 1
                if not counts[letter]:
                    queue.append(letter)

        if len(ans) != len(letters):
            return ""
        return ans