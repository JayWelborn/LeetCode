import random

class RandomizedSet:

    def __init__(self):
        self.value_list = []
        self.value_index_map = {}   

    def insert(self, val: int) -> bool:
        if val in self.value_index_map:
            return False
        
        self.value_list.append(val)
        self.value_index_map[val] = len(self.value_list) - 1
        return True

    def remove(self, val: int) -> bool:
        if not val in self.value_index_map:
            return False
        
        # replace the item and index_map entry for this val with the last value in our list
        prev_index = self.value_index_map[val]
        new_value = self.value_list[-1]
        self.value_list[prev_index] = self.value_list[-1]
        self.value_index_map[new_value] = prev_index
        
        # remove last item from value list since we moved it to previous item's index
        self.value_list.pop()
        del self.value_index_map[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.value_list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
