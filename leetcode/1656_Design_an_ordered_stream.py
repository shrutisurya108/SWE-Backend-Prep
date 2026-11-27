class OrderedStream:
# Aprroach 2: using a pointer and a list
    def __init__(self, n: int):
        # Time complexity for init = O(n), n operations to create a stream_list of size n
        # Space complexity for init = O(n), to store stream_list of size n
        self.n = n
        self.stream_list = [None] * self.n
        self.current = 0

    def insert(self, idKey: int, value: str) -> list[str]:
        # Time complexity for insert = O(n), n operations to iterate stream_list of size n
        # Space complexity for insert = O(1), no extra space needed, return_list is expected output
        indx = idKey-1
        self.stream_list[indx] = value
        return_list = []

        if indx == self.current:
            for i in range(indx, self.n):
                if self.stream_list[i] is not None:
                    return_list.append(self.stream_list[i])
                else:
                    self.current = i
                    break
            return return_list
        else:
            return []


# # Approach 1
#     def __init__(self, n: int):
#         # Time complexity for init operation = O(n) for the stream_list
#         # Space complexity for init = O(n) for the stream_list
#         self.n = n
#         self.stream_list = [None] * self.n
#         self.last = -1


#     def insert(self, idKey: int, value: str) -> list[str]:
#         # Time complexity for insert operation = O(n),
#         # in worst case, self.last = -1, so the iteration happens n times
#         # Space complexity for insert = O(1), return_list is the output
#         self.stream_list[idKey-1] = value
#         return_list = []

#         if self.n == 1:
#             return_list.append(value)
#             return return_list

#         for i in range(self.last+1, self.n):
#             if i < idKey-1:
#                 if self.stream_list[i] is None:
#                     return []

#             elif i == idKey-1:
#                 return_list.append(value)

#             elif i > idKey-1:
#                 if self.stream_list[i] is not None:
#                     return_list.append(self.stream_list[i])
#                 else:
#                     break

#         return return_list

# # Your OrderedStream object will be instantiated and called as such:
# # obj = OrderedStream(n)
# # param_1 = obj.insert(idKey,value)