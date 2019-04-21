
class StreamChecker:

    def __init__(self, words: List[str]):
        self.internal_set = set()
        
        self.internal_set_full = [] # dictionary to find ith letter, row 0 is dictionary of all first letters
        # list of dicts
        
        for curr_word in words:
            self.internal_set.add(curr_word)
            
            for i, letter in enumerate(curr_word):
                if not len(self.internal_set_full) > i:
                    self.internal_set_full.append(set(letter))
                else:
                    self.internal_set_full[i].add(letter)
        # print(self.internal_set_full)
        self.queries = ['']
    
    def check_queries(self, letter):
        
        found_in_dict = False
        
        cpy_query = self.queries.copy()
        for j in range(len(cpy_query)):
            curr_query = cpy_query[j]
            new_query = curr_query + letter

            added_letter_index = len(curr_query)
            if len(self.internal_set_full) > added_letter_index and \
                letter in self.internal_set_full[added_letter_index]:

                self.queries.append(new_query)
                if new_query in self.internal_set:
                    found_in_dict = True
                        
        return found_in_dict
    
    def query(self, letter: str) -> bool:
        return self.check_queries(letter)
#         cpy_query = self.queries.copy()
#         for i in range(len(cpy_query) - 1, -1, -1):
#             curr_query = cpy_query[i]
#             if curr_query in self.internal_set:
#                 return True
#             else:
#                 for j in range(len(curr_query)):
#                     if len(self.internal_set_full) <= j:
#                         self.queries.remove(curr_query)
#                         break
                        
#                     if len(self.internal_set_full) > j and \
#                         curr_query[j] not in self.internal_set_full[j]:
                        
#                         self.queries.remove(curr_query)
#                         break
                        
#         return False


# obj = StreamChecker(words)
# param_1 = obj.query(letter)
