import queue

class Graph:
    def __init__(self, word, val = 0):
        self.curr_word = word
        self.val = val
    
    @staticmethod
    def sub_dist(word1, word2):
        running_diff = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                running_diff += 1
            if running_diff > 1:
                return running_diff
        return running_diff
    
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
            
        currGraph = Graph(beginWord, 1)
        unvisited_set = set(wordList)
        
        next_visit_queue = queue.Queue()
        next_visit_queue.put(currGraph)
        
        while not next_visit_queue.empty():
            
            currGraphNode = next_visit_queue.get()
            outer_word = currGraphNode.curr_word
            for curr_word in unvisited_set.copy():
                if Graph.sub_dist(curr_word, outer_word) == 0:
                    unvisited_set.remove(curr_word)
                    
                if Graph.sub_dist(curr_word, outer_word) == 1:
                    newGraphNode = Graph(curr_word, currGraphNode.val + 1)
                    unvisited_set.remove(curr_word)
                    next_visit_queue.put(newGraphNode)
            
                    if curr_word == endWord:
                        return currGraphNode.val + 1
            # print(next_visit_queue)
        return 0
