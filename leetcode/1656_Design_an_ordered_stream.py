class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.stream_list = [None] * self.n
        self.last = -1
        

    def insert(self, idKey: int, value: str) -> list[str]:
        self.stream_list[idKey-1] = value
        return_list = []

        if self.n == 1:
            return_list.append(value)
            return return_list

        for i in range(self.last+1, self.n):
            if i < idKey-1:
                if self.stream_list[i] is None:
                    return []

            elif i == idKey-1:
                return_list.append(value)

            elif i > idKey-1:
                if self.stream_list[i] is not None:
                    return_list.append(self.stream_list[i])
                else:
                    break

        return return_list

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)