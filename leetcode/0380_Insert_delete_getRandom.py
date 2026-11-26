import random
class RandomizedSet:

    def __init__(self):
        self.set_dict = {}
        self.set_list = []

    def insert(self, val: int) -> bool:  # This operation takes O(1) time and O(1) space
        if val in self.set_dict:
            return False
        self.set_dict[val] = len(self.set_list)
        self.set_list.append(val)
        return True

    def remove(self, val: int) -> bool:  # # This operation takes O(1) time and O(1) space
        if val not in self.set_dict:
            return False
        ind_to_remove = self.set_dict.get(val)
        new_val_getting_that_index = self.set_list[-1]
        self.set_list[ind_to_remove] = new_val_getting_that_index
        self.set_dict[new_val_getting_that_index] = ind_to_remove
        self.set_list.pop()
        self.set_dict.pop(val)
        return True

    def getRandom(self) -> int:  # This operation takes O(1) time and O(1) space
        return random.choice(self.set_list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()