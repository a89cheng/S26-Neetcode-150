# Completed July 22, 2026 | 42 minutes

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        from collections import deque

        order = []
        wordList = set(wordList)
        seen = {beginWord}

        if endWord not in wordList:
            return 0

        graph = deque([])
        graph.append(beginWord)

        length = len(beginWord)

        layer = 1
        while graph:
            layer += 1
            n = len(graph)
            for x in range(n):
                curr = graph.popleft()
                for letter in list(map(chr, range(97, 123))):
                    for idx in range(length):
                        if f"{curr[:idx]}{letter}{curr[idx + 1:]}" in wordList:
                            if f"{curr[:idx]}{letter}{curr[idx + 1:]}" == endWord:
                                return layer
                            if f"{curr[:idx]}{letter}{curr[idx + 1:]}" not in seen:
                                graph.append(f"{curr[:idx]}{letter}{curr[idx + 1:]}")
                                seen.add(f"{curr[:idx]}{letter}{curr[idx + 1:]}")

        return 0