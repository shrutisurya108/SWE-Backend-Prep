# Big-O drills

# C1
while n > 0:
    n //= 3
Time complexity for C1 = O(log n) (log n with base 3) because n divides by 3 in every loop

# C2
for i in range(n):
    j = 1
    while j < n:
        j *= 2
num of times the code runs: Outer loop runs n times, inner loop runs log j times, where max value of j would be n-1
Time complexity for C2 = O (n log n) (worst case)


# C3
for x in a:
    if x in set_b:      # set_b is a set of size m
        print(x)
Time complexity of C3 = O(n), n=size of a
Because the outer loop runs n times, and in each loop, look up in set_b takes O(1) time.

# C4
for i in range(n):
    for j in range(i, n):
        for k in range(10):
            print(i, j, k)

The outermost loop runs n times
The inner loop runs n+(n-1)+(n-2)+....1 = n(n-1)/2 times
The innermost loop runs (10*(n(n-1)/2)) times
Time complexity of C4 = O(n^2)

# Leetcode 242
Follow up question: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
My answer: The unicode characters can also be included in the dict of character-counts, just like other alphabets/characters