# D1
for i in range(n):
    for j in range(5):
        print(i, j)

Time Complexity = O(5n) = O(n)
Space Complexity = O(1)

# D2
for x in a: print(x)
for y in b: print(y)

Time Complexity = O(a+b)
Space Complexity = O(1)

# D3
i = 1
while i < n:
    i *= 2

Time Complexity = O(log n), because n multiplies by 2 in every loop
Space Complexity = O(1)

# D4
for i in range(n):
    if i in some_list:    # some_list has n elements
        print(i)

Time Complexity = O(n^2)
Space Complexity = O(1)

# D5
for i in range(n):
    for j in range(i):
        print(i, j)

Time Complexity = 1+2+3+4........n = n(n-1)/2 = O(n^2)
Space Complexity = O(1)

# D6
result = []
for x in nums:            # len(nums) = n
    result.append(x * 2)

Time Complexity = O(n)
Space Complexity = O(n)

# Leetcode concerns

771: Could solve the brute force method , but could not optimize
1920: Could not solve for space complexity O(1)

# Bug hunt
Bug hunt: explain what this prints and why, then fix it:
grid = [[0] * 2] * 2
grid[0][1] = 5
print(grid)

When a 2D list is created in this way, although a user's intention might be to create 2 rows and 2 columns with value 0 in each cell,
but it actually creates 1 row with value 0 in it, and then the same row is referenced again by the "*2"
so when grid[0][1]=5 is done, is also changes the value of grid[1][1] to 5
The output will therefore be:
[[0,5],[0,5]]

# Daily Check
1. Answered with D5 above
2. x in my_set is O(1) because it uses hasing to store and look up values, but x in my_list is O(n) because it traverses the list items one by one. hash(x) computes a slot index directly, so there's no scanning. Tomorrow covers internals.
3. Tuples are immutable and therefore hashable, so they can be used as dict keys, because dict hashes the items using the key values. There 
is no risk of any change in dict keys being tuples as they will not be modified in future. However, lists are mutable, so they cannot be used
as dict keys because it may change in future, causing a change in hash location and previous hashed location will not be accessed. So it is 
important that mutable objects should not be used as dict keys.
4. In def f(items=[]), the argument is a mutable object. The list will be created once during function definition, and when the function is 
called by different users, it does not create an individual user's copy of the list, but uses the same list for all users calling the function.
For fix: def f(items=None): if items is None: items = [].
5. In a problem with n <= 10^5, O(n^2) solution is not acceptable. because it would be 10^10 ops in worst case, which will give time limit exceeded error.
6. *args becomes a tuple and **kwargs becomes a dict.
7. nums.sort() modifies nums in place, and sorted(nums) creates another copy of nums that store the sorted items. nums = nums.sort() sets nums to None, because .sort() returns None
8. To remove duplicates from a list while preserving order, we can use dict.fromkeys() to create a dictionary where only the unique items
remain as dict keys in order as they were input into the dictionary, and then convert it into a list.
In the step of creating a dictionary, it would be O(n) time complexity, then creating a list from the dict keys would again be O(n) complexity.
So, together the operation is O(2n) = O(n).
Another approach is using a set+list. Create a set of seen items parallely alognside creating a new list of items. This way only the first occurrence of every item will be added to the list (hence ordered) because of matching against the seen set.