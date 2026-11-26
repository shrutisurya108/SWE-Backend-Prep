class MyQueue:

    def __init__(self):
        self.s1 = []        # This serves as the queue implementation
        self.s2 = []

    def push(self, x: int) -> None: # This operation takes O(1) time
        self.s1.append(x)           # Simulates stack and queue behaviour of adding the item at the last

    def pop(self) -> int:           # This operation takes O(n) time, implements queue behaviour
        while(len(self.s1)>0):
            self.s2.append(self.s1.pop())
        pop_val = self.s2.pop()
        while(len(self.s2)>0):
            self.s1.append(self.s2.pop())
        return pop_val

    def peek(self) -> int:         # This operation takes O(n) time, implements queue behaviour
        while(len(self.s1)>0):
            self.s2.append(self.s1.pop())
        peek_val = self.s2.pop()
        self.s1.append(peek_val)
        while(len(self.s2)>0):
            self.s1.append(self.s2.pop())
        return peek_val

    def empty(self) -> bool:     # This operation takes O(1) time
        return len(self.s1)==0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()