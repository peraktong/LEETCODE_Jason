from collections import defaultdict


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        # use a queue: use index to represent the level for each word and find the shortest path:
        # edge case check
        if endWord not in wordList:
            return 0
        L = len(beginWord)
        # BFS: Let's replace each char in word with * once per time.
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                # key is h*t and value is the list of word which has the same character as h*t
                all_combo_dict[word[:i] + "*" + word[i + 1:]].append(word)
        # Queue
        queue = collections.deque([(beginWord, 1)])
        # dictionary for visited nodes
        visited = {beginWord: True}
        while queue:
            current_word, level = queue.popleft()
            for i in range(L):
                intermediate_word = current_word[:i] + "*" + current_word[i + 1:]
                # then we check all words with the same intemedia word:
                for word in all_combo_dict[intermediate_word]:
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level + 1))
                # This is because we use all words in all_combi_dict at this h*t which is unique
                # we do not need to use this step... only to save memory:
                #all_combo_dict[intermediate_word] = []
        return 0

# Always check the memory consumption:


