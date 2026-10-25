# Day 2 Review — Big-O + Data Structures & Functions

**Score: 7 / 10** · Your Python exercises are clean and your data-structure reasoning (hashing, tuples as keys, `*args/**kwargs`) is solid. Points were lost on Big-O analysis: two drill mistakes, the constraints question, and three LeetCode complexities that were mislabeled. That's normal for Day 2. Big-O is the one skill every interview round grades, so we drill it again tomorrow.

**Verdict: ✅ Move on to Day 3**, starting with a 45-minute catch-up block (it's already in `Day03_Lesson.md`).

I cloned your repo and ran your code. Every claim below was tested.

---

## 🔴 Must-Fix

### 1. Big-O drills: D2 and D3 are wrong

**D2 — your answer O(2n) = O(n). Correct: O(a + b).**
`a` and `b` are **different inputs** with different sizes. If `a` has 10 items and `b` has 10 million, calling both "n" hides that. This was Rule 3 in the lesson. Interviewers specifically check this: "you said n, but which n?"

**D3 — your answer O(n/2) = O(n). Correct: O(log n).**
`i` **doubles** each step; it doesn't add 2. Trace it for n = 1000:

```
i = 1 → 2 → 4 → 8 → 16 → 32 → 64 → 128 → 256 → 512 → 1024 (stop)
```
That's **10 steps**, not 500. The question to ask is: "how many times can I double 1 before reaching n?" The answer is log₂(n). Any loop where the variable is **multiplied or divided** each step is O(log n). Any loop where it's **added to or subtracted from** is O(n).

| Loop update | Steps to reach n | Big-O |
|---|---|---|
| `i += 1` | n | O(n) |
| `i += 2` | n/2 | O(n) |
| `i *= 2` | log₂ n | O(log n) |
| `n //= 2` | log₂ n | O(log n) |

**D5 — right answer, wrong reasoning.** "O(n·i)" isn't valid, because `i` changes every iteration; it's not a fixed size. Count the actual work:

```
i = 0 → inner runs 0 times
i = 1 → 1 time
i = 2 → 2 times
...
i = n−1 → n−1 times
Total = 0 + 1 + 2 + … + (n−1) = n(n−1)/2 = 0.5n² − 0.5n  →  O(n²)
```
Memorize this sum: **1 + 2 + … + n = n(n+1)/2**. It comes up constantly, since every "compare each pair once" loop has this shape.

### 2. Daily Check Q5 (the one you got stuck on)

**"`n ≤ 10⁵`. Is O(n²) acceptable?" → No.** Here's the reasoning, step by step:

1. Plug in the worst case: n² = (10⁵)² = **10¹⁰ operations**.
2. Python does roughly 10⁷ simple operations per second.
3. 10¹⁰ ÷ 10⁷ = **1,000 seconds ≈ 17 minutes**. LeetCode's time limit is a few seconds, so you get "Time Limit Exceeded".
4. So you need O(n log n) (10⁵ × 17 ≈ 1.7×10⁶ ops, instant) or O(n).

**Do this every time you read a problem:** look at the max n, check the constraints table (A1.5 in the Day 2 lesson), and know your target complexity *before* you write code. In an interview, saying *"n is up to 10⁵, so O(n²) won't pass and I'm aiming for O(n log n) or better"* is a strong signal.

### 3. LC 1512 — your optimized version gives wrong answers

Your active code is the brute force (it `return`s first), so LeetCode accepted that. Your Approach 2 never ran. I ran it:

```
[1,2,3,1,1,3] → your answer 3, expected 4
[1,1,1,1]     → your answer 3, expected 6
```
**The bug:** `count - 1` isn't the number of pairs. If a value appears `c` times, every pair of those positions counts. For `[1,1,1,1]` the pairs are (0,1), (0,2), (0,3), (1,2), (1,3), (2,3), so 6. The formula is "c choose 2" = **c·(c−1)/2**. It's the same 0+1+2+…+(c−1) sum as D5.

**Even better, one pass:** each new copy of a value forms a pair with *every earlier copy*.
```python
def numIdenticalPairs(self, nums: list[int]) -> int:
    seen = {}
    pairs = 0
    for num in nums:
        pairs += seen.get(num, 0)        # pair with every earlier copy
        seen[num] = seen.get(num, 0) + 1
    return pairs
# Time O(n) | Space O(k), k = number of distinct values
```
Trace `[1,1,1,1]`: pairs += 0, 1, 2, 3 → **6** ✅.

**Lesson:** always run your optimized version against the examples before calling it done. Unreachable code after a `return` is never tested.

### 4. LC 771 — "Approach 2 is O(n)" is wrong, and here's the optimization you were looking for

`stone in jewels` searches a **string**, so it's O(m) per check (lesson A1.3, "hidden costs"). Total is O(n·m), the same as your Approach 1. The fix is the one-line idea from the hint: turn `jewels` into a **set** first, so each check is O(1).

```python
def numJewelsInStones(self, jewels: str, stones: str) -> int:
    jewel_set = set(jewels)                        # O(m), built once
    return sum(stone in jewel_set for stone in stones)   # O(n), O(1) per check
# Time O(n + m) | Space O(m)
```
`sum(...)` over booleans works because `True == 1` and `False == 0`.
**General pattern (you'll use it all of Day 3):** if you're doing `x in something` inside a loop, ask "can `something` be a set or dict?"

### 5. Bug hunt (Exercise 7) — explanation right, output format wrong, fix missing
Your explanation is correct: both rows are the same list object. But:
- The output is `[[0, 5], [0, 5]]`. `print` shows the list structure, not a grid.
- You didn't give the fix. Interview answers always end with the fix:
```python
grid = [[0] * 2 for _ in range(2)]   # comprehension builds a NEW row each iteration
```
Why `[0] * 2` inside is safe: it repeats references to the int `0`, but ints are immutable. Assigning `row[1] = 5` replaces that slot instead of changing a shared object.

### 6. Day 1 review fixes were never applied
`412.py`, `ex4.py` (still shadows `sum`, still loops forever on negatives) and `ex6.py` are unchanged. Applying review feedback is the habit this whole loop is built on, and it's what a "fix" commit on GitHub shows. The Git steps are at the bottom of this file.

---

## 🟡 Improvements

**LC 1365 — ✅ Correct, and clever.** Sorting descending and decrementing for duplicates works; I tested `[8,1,2,2,3]` and `[7,7,7]`. Two notes:
- **Complexity is O(n log n), not O(n).** `sorted()` dominates. A step that sorts can never be O(n) overall.
- Simpler version: sort **ascending**. The index where a value *first* appears equals the count of smaller numbers.
```python
def smallerNumbersThanCurrent(self, nums):
    first_index = {}
    for i, num in enumerate(sorted(nums)):
        if num not in first_index:          # keep the FIRST position only
            first_index[num] = i
    return [first_index[num] for num in nums]
# Time O(n log n) | Space O(n)
```
- **Bonus O(n):** constraints say `0 ≤ nums[i] ≤ 100`, so count occurrences into a 101-slot list, then take prefix sums. Values in a small known range can skip sorting. That's the idea behind counting sort (you'll meet it again in Top K Frequent tomorrow).

**LC 1672 — Complexity is O(m·n), not O(n²).** There are `m` customers and `n` banks, which are different sizes (same lesson as D2). Pythonic one-liner: `return max(sum(customer) for customer in accounts)`. Your Approach 1 computed `sum(customer)` twice; store it in a variable.

**LC 1920 — O(1) space follow-up.** This one is a math trick, so don't worry that you didn't find it. The idea is to store two numbers in one slot. Since every value is `< n`, `a + n*b` holds both: `% n` gets `a` back and `// n` gets `b`.
```python
def buildArray(self, nums):
    n = len(nums)
    for i in range(n):
        nums[i] += n * (nums[nums[i]] % n)   # % n reads the ORIGINAL value even if it was already updated
    for i in range(n):
        nums[i] //= n                        # keep only the new value
    return nums
# Time O(n) | Space O(1) extra
```
Tested on `[0,2,1,5,3,4]` → `[0,1,2,4,5,3]` ✅. Rarely asked; know it exists.

**LC 1929 — commented Approach 1 has a bug:** `n` is never defined, so `ans[i+n]` raises `NameError`. Approach 3 (`nums * 2`) is the right answer. Two of your comments say "approach 2" under approach 3; keep labels accurate.

**LeetCode file layout.** Code after a `return` never runs, so your "Approach 2" blocks are untested. Put each approach in its own method:
```python
class Solution:
    def numIdenticalPairs(self, nums):          # LeetCode calls this one
        ...
    def numIdenticalPairs_brute(self, nums):     # kept for reference
        ...
```

**build_url — works, but by accident.** `query` is `{}` when empty, never `None`, so `if query_dict is not None` is *always* True. With no query args your code adds `?` and then `url[:-1]` chops it off. The test passed for the wrong reason. Use truthiness (Day 1, 2.5): `if query:`. Real code also has to **URL-encode** values. I ran yours with `q="red shoes & socks"` and got `...?q=red shoes & socks`, which a server will split at `&` into two broken parameters.
```python
from urllib.parse import urlencode

def build_url(base, *paths, **query):
    url = "/".join([base.rstrip("/"), *paths])
    if query:
        url += "?" + urlencode(query)    # 'red shoes & socks' → 'red+shoes+%26+socks'
    return url
```

**top_n_employees — returns tuples, but the task asked for names.** Your test passed because you asserted tuples. Return `[name for name, _ in result]`. Your `key=lambda e: (-e[1], e[0])` is exactly right. Note that you *did* use a lambda correctly here; the section below will make it click.

**Small things:** `text.strip().split()` doesn't need `strip()`, because `split()` already ignores outer whitespace. In `group_by_city`, `user["city"]` is better than `.get("city")` here, since a user missing a city should fail loudly instead of being grouped under `None`.

---

## ✅ Daily Check

| Q | Verdict | Notes |
|---|---|---|
| 1 | 🟡 | Answer right, reasoning off. See Must-Fix 1 (D5). |
| 2 | ✅ | Add *how*: `hash(x)` computes a slot index directly, so there's no scanning. Tomorrow covers internals. |
| 3 | ✅ Excellent | Exactly the right explanation: a key changing after insertion would leave it in the wrong slot. |
| 4 | 🟡 | Problem explained well, but **no fix given**. Fix: `def f(items=None): if items is None: items = []`. |
| 5 | ❌ | See Must-Fix 2. |
| 6 | ✅ | |
| 7 | ✅ | Add the classic bug: `nums = nums.sort()` sets `nums` to `None`, because `.sort()` returns `None`. |
| 8 | ✅ | O(2n) should be written as **O(n)**. Drop constants (Rule 1). Also mention the set + list approach from your Exercise 2. |

---

## 🧠 Lambdas and Closures, Explained Slowly

You said these were confusing. Here's a step-by-step version. Run every snippet.

### Part 1: Lambda = a function without a name

These two are **exactly the same**:
```python
def get_salary(employee):
    return employee[1]

get_salary = lambda employee: employee[1]
```
Read `lambda employee: employee[1]` as *"a function that takes `employee` and returns `employee[1]`"*. Limits: one expression, no statements, no `return` keyword (the expression *is* the return value).

**Why it exists:** some functions, like `sorted`, `max` and `min`, accept *another function* as `key`. They call it on each item to decide what to compare:
```python
employees = [("Bo", 500), ("Al", 900), ("Cy", 500)]

sorted(employees, key=lambda e: e[1])
# sorted calls the lambda on each item:
#   ("Bo",500) → 500    ("Al",900) → 900    ("Cy",500) → 500
# then sorts by those results: [("Bo",500), ("Cy",500), ("Al",900)]

sorted(employees, key=lambda e: (-e[1], e[0]))
# ("Bo",500) → (-500,"Bo")   ("Al",900) → (-900,"Al")   ("Cy",500) → (-500,"Cy")
# tuples compare element by element: -900 first, then (-500,"Bo") before (-500,"Cy")
# → [("Al",900), ("Bo",500), ("Cy",500)]
```
That's your `top_n_employees`. You already wrote it correctly. The `-` turns "highest salary first" into "smallest number first", which is the default sort order.

**Rule of thumb:** a lambda is just a short `def` you write inline because you need it once, right there.

### Part 2: Functions are values

```python
def shout(s):
    return s.upper()

f = shout          # no parentheses: f now points to the same function object
f("hi")            # 'HI'
shout              # <function shout at 0x...>   ← the function itself
shout("hi")        # 'HI'                         ← CALLING it
```
A function can be stored in a variable, passed to another function (like `key=`), or **returned from another function**. That last one is where closures come from.

### Part 3: Closure = an inner function that remembers variables from where it was created

```python
def make_multiplier(factor):
    def multiply(x):
        return x * factor      # factor isn't defined inside multiply...
    return multiply            # return the function itself (no parentheses)

double = make_multiplier(2)
triple = make_multiplier(3)
double(10)   # 20
triple(10)   # 30
```
**Step by step:**
1. `make_multiplier(2)` runs. Inside it, `factor = 2`.
2. It defines `multiply`, which *uses* `factor`.
3. It returns `multiply`, and `make_multiplier` finishes.
4. Normally `factor` would disappear now. But `multiply` still needs it, so Python **keeps `factor = 2` attached to that function**. That bundle (function + remembered variables) is a **closure**.
5. `make_multiplier(3)` creates a *separate* closure with its own `factor = 3`.

You can see the remembered value: `double.__closure__[0].cell_contents` → `2`.

### Part 4: `nonlocal` — when the closure needs to *change* the remembered variable

```python
def make_counter():
    count = 0
    def increment():
        nonlocal count     # "count belongs to make_counter, not me"
        count += 1
        return count
    return increment

c1 = make_counter()
c1(); c1(); c1()     # 1, 2, 3
c2 = make_counter()
c2()                 # 1  ← its own separate count
```
Without `nonlocal`, `count += 1` means "create a *new local* `count`", and Python raises `UnboundLocalError` because it's read before it's assigned. **Reading** an outer variable needs nothing (Part 3); **reassigning** it needs `nonlocal`.

### Part 5: Where you'll actually use closures

- **Decorators (Day 4):** `@retry(times=3)` and `@app.get("/users")` in FastAPI are closures. The outer function remembers settings and returns a wrapped function.
- **Callbacks and configuration:** `make_rate_limiter(max_per_second=10)` returns a function that remembers its limit and its own counter.
- **`key=` functions that need a parameter:** `sorted(points, key=lambda p: distance(p, origin))`. The lambda is itself a closure, since it remembers `origin`.

### The one classic trap (asked in interviews)
```python
funcs = [lambda: i for i in range(3)]
[f() for f in funcs]      # [2, 2, 2] — not [0, 1, 2]!
```
Closures remember the **variable**, not its value at creation time. All three lambdas look up `i` when *called*, and by then the loop has finished with `i = 2`. Fix: freeze the value as a default argument, which is evaluated at creation time: `lambda i=i: i`.

You'll practice all of this in tomorrow's catch-up block.

---

## 🔧 Git: apply the fixes

```bash
cd SWE-Backend-Prep

# 1. Consistent LeetCode names. git mv keeps the file's history
git mv leetcode/412.py  leetcode/0412_fizz_buzz.py
git mv leetcode/1480.py leetcode/1480_running_sum.py
git mv leetcode/1365.py leetcode/1365_smaller_numbers_than_current.py
git commit -m "Rename LeetCode files to number_name format"

# 2. Apply Day 1 + Day 2 fixes (ex4, ex6, 412, 1512, 771, build_url, top_n_employees)
#    Add "# Time: O(...) | Space: O(...)" at the top of every LeetCode file
git add .
git commit -m "Apply Day 1 and Day 2 review fixes"
git push
```
Optional: `4e33cd7 Day 02 work` is one big commit. From Day 3, commit after each block, e.g. `Day 3: arrays & hashing LeetCode`, then `Day 3: OOP exercises`.

**Your `.gitignore` is good.** It's GitHub's full Python template and already covers `.env`, `.venv` and `.vscode/`.
