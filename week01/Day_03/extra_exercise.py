"""1. Point(x, y) with __eq__, __hash__, __add__ and __repr__.
Prove it works by putting Point(1, 2) twice in a set and getting length 1.
"""
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, otherPoint):
        if self.x == otherPoint.x and self.y == otherPoint.y:
            return True
        return False

    def __add__(self, otherPoint):
        return Point(self.x + otherPoint.x, self.y + otherPoint.y)

    def __repr__(self):
        return f"{type(self.__name__())}, x= {self.x}, y={self.y}"

    def __hash__(self):
        return hash((self.x, self.y))

p1 = Point(1,2)
p2 = Point(2,3)
p3 = Point(1, 2)
assert (p1==p2) == False
assert (p1==p3) == True
points_set = set()
points_set.add(p1)
points_set.add(p1)
assert (len(points_set)) == 1

"""
Ex 2. Big-O analysis. For each function below, write the time and space complexity with a one-line reason (in a comment, no running).


def a(nums):
    total = 0
    for x in nums: total += x
    for x in nums: total -= x
    return total
# Time complexity = O(n), The loop iterates n times for 1st for loop and then again n times for 2nd for loop
# Space complexity = O(1), no extra space is used except x and total (the output)


def b(n):
    i = 1
    while i < n:
        i *= 2
# Time complexity = O(log n) (with base 2), The number of loop iterations reduces by half every time
# Space complexity = O(1), no extra space is used except i


def c(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            print(nums[i], nums[j])
# Time complexity = O(n^2), The outer loop iterates n times inner loop executes n-1 times, so total of n(n-1) iterations
# Space complexity = O(1), no extra space is used except i and j


def d(nums):
    out = []
    for x in nums:
        if x not in out:
            out.append(x)
    return out
# Time complexity = O(nm), The for loop iterates n times,
# and in each iteration, "if x not in out" runs m times (m=length of out, which at max will be n), so total of n*m iterations
# In worst case, when m=n, time complexity = O(n^2)
# Space complexity = O(n), the size of out will be n at max.

def e(words):
    return sorted(words)[:3]
# Time complexity = O(n log n), Sorting the elements of words takes O(n log n) times
# String slicing takes O(1) time
# Space complexity = O(n), because sorted() creates a new sorted array

def f(matrix):                       # m rows, n columns
    return [sum(row) for row in matrix]
# Time complexity = O(nm), each row sum takes m iteration, and sum operation runs for n columns, so total of n*m iterations
# Space complexity = O(m), each row sum becomes 1 element in the output list, so m rows give m elements in the result list

def g(s):
    result = ""
    for ch in s:
        result = ch + result
    return result
# Time complexity = O(n), The for loop iterates n times, n=number of characters in s
# Space complexity = O(n), In every iteration of for loop, new string is created and concatenated to, so total of n new strings are created

def h(nums, queries):                # n = len(nums), q = len(queries)
    lookup = set(nums)
    return [x in lookup for x in queries]
# Time complexity = O(q+n), The conversion of nums to a set takes n iterations, and then each lookup takes O(1) time since it is a set
# and total of q lookups are done, so, total iterations = q+n
# Space complexity = O(n+q), because a new set is created which can have n items in worst case (all items distinct),
# and return list is of size q
"""

"""
Ex 6. Stack class. Stack with push, pop, peek, is_empty and __len__, backed by a list.
pop/peek on an empty stack raise IndexError("stack is empty"). In each method's docstring, state its Big-O.
"""
class Stack:
    def __init__(self):
        """Stack initilization, takes O(1) time and O(1) space"""
        self.stack=[]

    def push(self, val):
        """Stack push operation, takes O(1) to add the value at the end of stack, takes no extra space, O(1) space complexity"""
        self.stack.append(val)

    def pop(self):
        """Stack pop operation, takes O(1) time to pop last element, no extra space, O(1) space complexity"""
        if self.stack.is_empty():
            raise IndexError("stack is empty")
        return self.stack.pop()

    def peep(self):
        """Stack peek operation, takes O(1) to find and return the last element, no extra space, O(1) space complexity"""
        if self.stack.is_empty():
            raise IndexError("stack is empty")
        return self.stack[-1]

    def is_empty(self):
        """Stack is_empty check, takes O(1) times because finding length using len() takes constant time, no extra space, O(1) space complexity"""
        return len(self.stack)==0

    def __len__(self):
        """Stack len() function, takes O(1) time to return length, no extra space, O(1) space complexity"""
        return len(self.stack)