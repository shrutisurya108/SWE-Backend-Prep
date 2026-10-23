# Day 2 — Big-O + Python Data Structures & Functions (Tue Oct 20 · ~7 hrs)

| Time | Block |
|---|---|
| 0:00–0:30 | GitHub setup + push Day 1 (see `GitHub_Daily_Workflow.md`) |
| 0:30–1:30 | **A1.** Big-O lesson + analysis drills |
| 1:30–3:00 | **A2.** LeetCode (6 problems) |
| — | Break (lunch) |
| 3:00–4:45 | **B1.** Lists, tuples, dicts, sets, comprehensions |
| 4:45–6:00 | **B2.** Functions, args/kwargs, scope, lambdas |
| 6:00–6:45 | **B3.** Practice exercises |
| 6:45–7:00 | Daily check + push to GitHub + submit |

---

# Block A — Big-O Complexity

## A1.1 What Big-O means
Big-O describes **how the running time (or memory) grows as input size `n` grows**, in the worst case. It ignores machine speed and focuses on the *shape* of the growth.

**Rules:**
1. **Drop constants:** O(2n) → O(n). O(500) → O(1).
2. **Keep only the dominant term:** O(n² + n) → O(n²).
3. **Different inputs get different letters:** looping over `a` then `b` is O(a + b); nested loops over them are O(a · b), **not** O(n²).
4. **Sequential steps add, nested steps multiply.**

## A1.2 The common classes (fastest → slowest)

| Big-O | Name | Example | n = 1,000,000 ≈ ops |
|---|---|---|---|
| O(1) | Constant | dict lookup, list index | 1 |
| O(log n) | Logarithmic | binary search | 20 |
| O(n) | Linear | one loop over the list | 10⁶ |
| O(n log n) | Linearithmic | sorting | 2×10⁷ |
| O(n²) | Quadratic | nested loops over the same list | 10¹² ❌ |
| O(2ⁿ) | Exponential | all subsets | impossible |
| O(n!) | Factorial | all permutations | impossible |

**Real world:** a feed service with 1M users. An O(n²) "find duplicate accounts" job does about 10¹² operations, which takes **hours or days** in Python. An O(n) version with a set finishes in under a second. This exact difference is what interviewers want you to notice.

## A1.3 Reading code
```python
def f1(nums):                 # O(n)
    total = 0
    for x in nums:
        total += x
    return total

def f2(nums):                 # O(n²) — nested loops over the same input
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

def f3(n):                    # O(log n) — n is halved each step
    steps = 0
    while n > 1:
        n //= 2
        steps += 1
    return steps

def f4(nums):                 # O(n log n) — sorting dominates the O(n) loop
    nums = sorted(nums)
    for x in nums:
        print(x)
```
**Hidden costs** (a common interview trap): `x in some_list` is O(n), `list.pop(0)` is O(n), and string slicing `s[a:b]` is O(b − a). One line of code is not always O(1)!

## A1.4 Space complexity
Extra memory the algorithm uses, beyond the input. `f1` is O(1) space; `sorted(nums)` creates a copy, so `f4` is O(n) space. Recursion also uses stack space (O(depth)). You'll see this on Day 11.

## A1.5 Use constraints to guess the target complexity
LeetCode and interviewers give constraints like `1 <= n <= 10^5`. Python handles roughly **10⁶–10⁷ simple operations per second**:

| Max n | Target complexity |
|---|---|
| ≤ 10 | O(n!) — permutations OK |
| ≤ 20 | O(2ⁿ) — subsets OK |
| ≤ 500 | O(n³) |
| ≤ 10⁴ | O(n²) |
| ≤ 10⁶ | O(n log n) or O(n) |
| > 10⁸ | O(log n) or O(1) |

## A1.6 Drills: write the time and space complexity for each
```python
# D1
for i in range(n):
    for j in range(5):
        print(i, j)

# D2
for x in a: print(x)
for y in b: print(y)

# D3
i = 1
while i < n:
    i *= 2

# D4
for i in range(n):
    if i in some_list:    # some_list has n elements
        print(i)

# D5
for i in range(n):
    for j in range(i):
        print(i, j)

# D6
result = []
for x in nums:            # len(nums) = n
    result.append(x * 2)
```
(D5 is a classic: think about 0 + 1 + 2 + … + (n−1).)

## A2. LeetCode (6 problems)

For **every** problem, write the time and space complexity as a comment. For ⭐ problems, write **both** a brute-force and an optimized version, with complexity for each. Interviewers love "start brute force, then optimize".

| # | Problem | Diff | Concept / Hint |
|---|---|---|---|
| 1929 | [Concatenation of Array](https://leetcode.com/problems/concatenation-of-array/) | Easy | Warm-up. Try a one-liner too. |
| 1920 | [Build Array from Permutation](https://leetcode.com/problems/build-array-from-permutation/) | Easy | Indexing. Try a list comprehension. |
| 1672 | [Richest Customer Wealth](https://leetcode.com/problems/richest-customer-wealth/) | Easy | 2-D list. Complexity uses two letters (m × n). |
| 771 | [Jewels and Stones](https://leetcode.com/problems/jewels-and-stones/) | Easy | ⭐ Brute: `in` on a string. Optimized: a **set**. |
| 1512 | [Number of Good Pairs](https://leetcode.com/problems/number-of-good-pairs/) | Easy | ⭐ Brute: nested loops O(n²). Optimized: dict of counts, O(n). |
| 1365 | [How Many Numbers Are Smaller Than the Current Number](https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/) | Easy | ⭐ Brute O(n²). Optimized: sort + dict of first positions. |

---

# Block B — Python Data Structures & Functions

## B1.1 Lists — ordered, mutable, allow duplicates
```python
nums = [5, 2, 8]
nums.append(1)        # [5, 2, 8, 1]        O(1) amortized
nums.insert(0, 9)     # [9, 5, 2, 8, 1]     O(n) — shifts everything
nums.pop()            # removes 1           O(1)
nums.pop(0)           # removes 9           O(n) — use collections.deque for queues
nums.remove(2)        # first occurrence    O(n)
nums.sort()           # in place            O(n log n)
sorted(nums)          # returns NEW list
nums.reverse(); nums[::-1]
nums.index(8); nums.count(5); len(nums)
nums.extend([7, 7])   # add many

matrix = [[0] * 3 for _ in range(3)]   # ✅ correct 2-D list
bad    = [[0] * 3] * 3                 # ❌ 3 references to the SAME row!
bad[0][0] = 1                          # → [[1,0,0],[1,0,0],[1,0,0]]  classic bug

copy1 = nums[:]                        # shallow copy
import copy; deep = copy.deepcopy(matrix)   # deep copy for nested lists
```

## B1.2 Tuples — ordered, **immutable**
```python
point = (3, 4)
x, y = point                  # unpacking
a, b = b, a                   # swap (builds a tuple under the hood)
single = (5,)                 # the comma makes it a tuple; (5) is just 5
locations = {(0, 0): "origin"}   # tuples are hashable → usable as dict keys / set items
```
**When to use:** fixed records (coordinates, DB rows, returning multiple values from a function). Immutability makes them safe to share.

## B1.3 Dictionaries — key → value, O(1) average lookup
```python
user = {"id": 42, "name": "Asha", "role": "admin"}
user["name"]                  # 'Asha'   KeyError if missing
user.get("email")             # None     safe
user.get("email", "n/a")      # default
user["email"] = "a@x.com"     # add / update
del user["role"]
"id" in user                  # True — O(1)

for key, value in user.items():
    print(key, value)
user.keys(); user.values()

# Counting pattern (you'll use this in 50+ LeetCode problems)
counts = {}
for word in ["get", "post", "get"]:
    counts[word] = counts.get(word, 0) + 1     # {'get': 2, 'post': 1}

# Grouping pattern
groups = {}
for name, dept in [("A", "eng"), ("B", "ops"), ("C", "eng")]:
    groups.setdefault(dept, []).append(name)   # {'eng': ['A','C'], 'ops': ['B']}

merged = {**defaults, **overrides}   # later keys win — how config overrides work
merged = defaults | overrides        # same thing (Python 3.9+)
```
- Keys must be **hashable** (immutable): str, int, tuple. A list can't be a key.
- Dicts **keep insertion order** (guaranteed since Python 3.7).
- **How it's O(1):** a hash table. `hash(key)` gives an index into an array, so there's no scanning. The worst case (many collisions) is O(n), but that's rare. *Interview question:* "How does a hash map work internally?" We go deep on this tomorrow.

**Real world:** JSON API responses become dicts. Caches like Redis are giant distributed dicts.

## B1.4 Sets — unique items, O(1) membership
```python
seen = {1, 2, 3}
empty = set()                 # NOT {} — that's an empty dict!
seen.add(4); seen.discard(9)  # discard doesn't error if missing
2 in seen                     # O(1)  vs  O(n) for a list

a, b = {1, 2, 3}, {2, 3, 4}
a | b    # union         {1, 2, 3, 4}
a & b    # intersection  {2, 3}
a - b    # difference    {1}
a ^ b    # symmetric     {1, 4}

list(set([3, 1, 3]))          # dedupe — but ORDER IS LOST
list(dict.fromkeys([3, 1, 3]))   # dedupe AND keep order → [3, 1]
```
**Real world:** "users who liked post A **and** post B" is an intersection. Blocklists and "already processed this event ID" checks use sets.

## B1.5 Which one should I use?

| Need | Use |
|---|---|
| Ordered collection that changes | `list` |
| Fixed record / dict key | `tuple` |
| Look up by key | `dict` |
| "Have I seen this?" / uniqueness | `set` |
| Queue (FIFO) | `collections.deque` (Day 4) |

## B1.6 Comprehensions
```python
squares = [x * x for x in range(5)]                 # [0, 1, 4, 9, 16]
evens   = [x for x in nums if x % 2 == 0]           # filter
labels  = ["even" if x % 2 == 0 else "odd" for x in nums]   # if/else goes BEFORE for
lookup  = {u["id"]: u for u in users}               # dict comprehension — id → user
unique_domains = {email.split("@")[1] for email in emails}  # set comprehension
pairs   = [(i, j) for i in range(3) for j in range(3)]      # nested
total   = sum(x * x for x in nums)                  # generator expression (no list built)
```
Rule: use a comprehension when it fits on one readable line; otherwise use a normal loop.

---

## B2. Functions

### B2.1 Basics, defaults, keyword arguments, type hints
```python
def greet(name: str, greeting: str = "Hello") -> str:
    """Return a greeting. (This is a docstring — write one for public functions.)"""
    return f"{greeting}, {name}!"

greet("Asha")                       # positional
greet(greeting="Hi", name="Asha")   # keyword — order doesn't matter

def min_max(nums):
    return min(nums), max(nums)     # returns a tuple
lo, hi = min_max([3, 1, 9])
```
A function with no `return` returns `None`.

### B2.2 ⚠️ The mutable default argument trap (very common interview question)
```python
def add_item(item, cart=[]):        # ❌ the list is created ONCE, when the function is defined
    cart.append(item)
    return cart

add_item("a")    # ['a']
add_item("b")    # ['a', 'b']  ← data leaks between calls!

def add_item(item, cart=None):      # ✅ correct pattern
    if cart is None:
        cart = []
    cart.append(item)
    return cart
```
In a web server, this bug can leak one user's data into another user's request.

### B2.3 `*args` and `**kwargs`
```python
def log(level, *messages, **context):
    # messages → tuple of extra positional args
    # context  → dict of extra keyword args
    print(level, " ".join(messages), context)

log("ERROR", "db", "timeout", user_id=42, retry=3)
# ERROR db timeout {'user_id': 42, 'retry': 3}

nums = [1, 2, 3]
print(*nums)               # unpacking into a call → print(1, 2, 3)
config = {"sep": " | "}
print("a", "b", **config)  # → a | b
```
**Real world:** decorators, logging libraries and web frameworks (FastAPI, Django) use `*args/**kwargs` everywhere to forward arguments they don't know in advance.

**Parameter order:** `def f(positional, default=1, *args, keyword_only, **kwargs)`

### B2.4 Scope: LEGB
Python looks up names in this order: **L**ocal → **E**nclosing function → **G**lobal (module) → **B**uilt-in. That's why shadowing `sum` in yesterday's ex4 broke the built-in: your global `sum` was found before the built-in one.
```python
count = 0
def increment():
    global count        # needed to REASSIGN a global (avoid this in real code)
    count += 1

def counter():
    n = 0
    def inc():
        nonlocal n      # reassign the enclosing function's variable
        n += 1
        return n
    return inc          # a closure: inc "remembers" n

c = counter(); c(); c()   # 1, then 2
```

### B2.5 Functions are objects; lambdas
```python
def shout(s): return s.upper()
f = shout; f("hi")                      # functions can be stored and passed around

users = [("Asha", 31), ("Ben", 25), ("Cy", 28)]
sorted(users, key=lambda u: u[1])                 # sort by age
sorted(users, key=lambda u: (-u[1], u[0]))        # age descending, then name
max(users, key=lambda u: u[1])                    # oldest user
```
Lambdas are one-expression anonymous functions. Use them for `key=` arguments; for anything longer, use `def`.

---

## B3. Practice Exercises

Write each as a **function that returns a value** (applying yesterday's lesson), with a few `print` or `assert` tests underneath.

1. **`word_frequency(text)`:** return a dict of word → count, case-insensitive. `"GET post get"` → `{'get': 2, 'post': 1}`.
2. **`dedupe_keep_order(items)`:** remove duplicates, keeping first-seen order, in O(n). Don't use `dict.fromkeys`; use a set + list so you understand the mechanism.
3. **`group_by_city(users)`:** input is a list of dicts like `{"name": "Asha", "city": "Buffalo"}`; return `{city: [names]}`.
4. **`invert(d)`:** swap keys and values: `{"a": 1, "b": 2}` → `{1: "a", 2: "b"}`. Then answer in a comment: what goes wrong if two keys share the same value?
5. **`build_url(base, *paths, **query)`:** `build_url("https://api.x.com", "v1", "users", limit=10, page=2)` → `"https://api.x.com/v1/users?limit=10&page=2"`. With no query args, there's no `?`.
6. **`top_n_employees(employees, n)`:** list of `(name, salary)` tuples; return the top `n` names by salary, with ties broken alphabetically by name. Use `sorted` with a `key`.
7. **Bug hunt:** explain what this prints and why, then fix it:
   ```python
   grid = [[0] * 2] * 2
   grid[0][1] = 5
   print(grid)
   ```

---

## Daily Check

1. What is the time complexity of D5 in the drills, and why?
2. Why is `x in my_set` O(1) but `x in my_list` O(n)?
3. Why can a tuple be a dict key but a list can't?
4. What's wrong with `def f(items=[])`, and what's the fix?
5. A problem has `n <= 10^5`. Is an O(n²) solution acceptable? Explain with numbers.
6. What do `*args` and `**kwargs` become inside the function?
7. What's the difference between `nums.sort()` and `sorted(nums)`?
8. How would you remove duplicates from a list **while preserving order**? Give the complexity.

---

## 📤 How to Submit
```
DAY 2 SUBMISSION
Time spent: __
GitHub repo link: __
Big-O drills D1–D6: __
LeetCode: (code + complexity for each; brute + optimized for ⭐)
Exercises 1–7: (code)
Daily check: 1)… 8)…
Where I got stuck: __
```
Next: Day 3 covers Arrays & Hashing (Two Sum, Group Anagrams, Top K Frequent…) and Python OOP.
