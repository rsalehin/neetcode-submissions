class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        def get_neighbors(word):
            neighbors = []
            for i in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    if ch != word[i]:
                        new_word = word[:i] + ch + word[ i + 1 :]
                        if new_word in wordList:
                            neighbors.append(new_word)
            return neighbors
        #Set up BFS
        queue = deque()
        queue.append((beginWord, 1))
        visited = set()
        visited.add(beginWord)

        while queue:
            word, steps = queue.popleft()
            for neighbor in get_neighbors(word):
                if neighbor == endWord:
                    return steps + 1
                if neighbor not in visited:
                    queue.append((neighbor, steps + 1))
                    visited.add(neighbor)
                    wordList.remove(neighbor)
        return 0
        
        