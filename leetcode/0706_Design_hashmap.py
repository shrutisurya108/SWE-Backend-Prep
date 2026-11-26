class MyHashMap:

    def __init__(self):
        self.hashmap = []

    def put(self, key: int, value: int) -> None:  # put operation takes O(n) time, no extra space
        found = False
        for i in range(len(self.hashmap)):
            if self.hashmap[i][0]==key:
                self.hashmap[i][1] = value
                found = True
        if not found:
            self.hashmap.append([key, value])

    def get(self, key: int) -> int:  # get operation takes O(n) time, no extra space
        for i in self.hashmap:
            if i[0]==key:
                return i[1]
        return -1

    def remove(self, key: int) -> None:  # remove operation takes O(n) time, no extra space
        for i in self.hashmap:
            if i[0]==key:
                self.hashmap.remove(i)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)