class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        L = len(beginWord)
        all_combo_dict = defaultdict(list)

        for word in wordList:
            for i in range(L):
                wildcard = word[:i] + "*" + word[i + 1:]
                all_combo_dict[wildcard].append(word)
        
        queue = deque([(beginWord, 1)]) #(current_word, level)
        visited = set([beginWord])

        while queue:
            current_word, level = queue.popleft()

            for i in range(L):
                wildcard = current_word[:i] + "*" + current_word[i+1:]
                for neighbor in all_combo_dict[wildcard]:
                    if neighbor == endWord:
                        return level + 1
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, level + 1))
                    
                #optional: clear visited wildcard group to save memory
                all_combo_dict[wildcard] = []
        return 0