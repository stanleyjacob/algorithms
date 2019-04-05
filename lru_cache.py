class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.curr_data_dict = collections.OrderedDict()
        
    def get(self, key: int) -> int:
        if key not in self.curr_data_dict:
            return -1
        else:
            val = self.curr_data_dict[key]
            self.curr_data_dict.move_to_end(key, last = True)
            return val

    def put(self, key: int, value: int) -> None:
        if len(self.curr_data_dict) == self.cap:
            self.curr_data_dict.popitem(last = False)
        
        self.curr_data_dict[key] = value
        self.curr_data_dict.move_to_end(key, last = True)
