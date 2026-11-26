class MyHashSet:

    def __init__(self):
        self.hashset = []

    def add(self, key: int) -> None:  # add operation takes O(n) time, no extra space
        found = False
        for i in self.hashset:
            if i == key:
                found=True
        if not found:
            self.hashset.append(key)

    def remove(self, key: int) -> None: # remove operation takes O(n) time, no extra space
        for i in self.hashset:
            if i==key:
                self.hashset.remove(i)

    def contains(self, key: int) -> bool: # containes operation takes O(n) time, no extra space
        for i in self.hashset:
            if i == key:
                return True
        return False




# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)