# Day 3 — Arrays & Hashing + Python OOP (Fri Oct 23 · ~7.5 hrs)

| Time | Block |
|---|---|
| 0:00–0:45 | **Catch-up:** Day 2 fixes + closure/Big-O drills |
| 0:45–1:30 | **A1.** How hash maps work + the 4 hashing patterns |
| 1:30–3:30 | **A2.** LeetCode (6 problems + 1 stretch) |
| — | Break (lunch) |
| 3:30–5:30 | **B1.** OOP: classes, methods, inheritance, dunder methods, `@property`, dataclasses |
| 5:30–6:45 | **B2.** Practice exercises (incl. build your own HashMap) |
| 6:45–7:30 | Daily check + commit + submit |

Work goes in `week01/Day_03/`; LeetCode goes in `leetcode/` as `0001_two_sum.py` etc.

---

# Catch-up (45 min)

1. **Apply the Day 2 review fixes** (`Day02_Review.md`, Git section) and push them.
2. **Re-solve from scratch, without looking:** LC 1512 (one-pass version) and LC 771 (set version). Write complexity on both.
3. **Big-O drills** — write time complexity for each:
   ```python
   # C1
   while n > 0:
       n //= 3
   # C2
   for i in range(n):
       j = 1
       while j < n:
           j *= 2
   # C3
   for x in a:
       if x in set_b:      # set_b is a set of size m
           print(x)
   # C4
   for i in range(n):
       for j in range(i, n):
           for k in range(10):
               print(i, j, k)
   ```
4. **Closures** — in `week01/Day_03/closures.py`:
   - `make_greeting(greeting)` returns a function that takes `name` and returns `f"{greeting}, {name}!"`.
   - `make_accumulator()` returns a function; each call `acc(x)` adds `x` to a running total and returns it (`acc(5) → 5`, `acc(3) → 8`). Needs `nonlocal`.
   - Sort `["banana", "Apple", "cherry"]` case-insensitively with a lambda. Then sort by length, longest first.
   - Explain in a comment why `[lambda: i for i in range(3)]` returns `[2, 2, 2]` when called, and fix it.

---

# Block A — Arrays & Hashing

## A1.1 How a hash map works (interview favorite: "how does a dict work internally?")

A hash map is an **array of slots** plus a **hash function**.

```
put("cat", 7):
  1. hash("cat")            → 8273645123  (some big integer)
  2. 8273645123 % 8 slots   → index 3
  3. store ("cat", 7) at slot 3

get("cat"):
  same two steps → index 3 → found. No scanning → O(1)
```

**Collisions:** two keys can land on the same slot. Two fixes:
- **Chaining:** each slot holds a small list of (key, value) pairs. Java's `HashMap` does this.
- **Open addressing:** if a slot is taken, probe the next slot. Python's `dict` does this.

**Load factor = items / slots.** As it rises, collisions rise. When it passes a threshold (~0.66 in Python, 0.75 in Java), the table **resizes**: it allocates about 2× the slots and re-inserts everything. That one resize is O(n), but it happens so rarely that the average cost per insert is still O(1). This is called **amortized O(1)**, the same reason `list.append` is O(1).

**Worst case O(n):** if every key collides, which takes a bad hash function or deliberately crafted input. That's why Python randomizes string hashing per process ("hash DoS" protection).

**Why keys must be hashable/immutable:** if a key changed after insertion, its hash would change and you'd look in the wrong slot. (You explained this well yesterday.)

**Real world:** Redis, Memcached, DNS caches, DB hash indexes, and the session store in a web server are all hash maps. Distributed caches spread one giant hash map across machines with consistent hashing (Day 22).

## A1.2 The 4 hashing patterns

| Pattern | When you see… | Tool |
|---|---|---|
| **1. Seen-before** | "duplicate", "exists", "first repeated" | `set` |
| **2. Frequency count** | "anagram", "most frequent", "same characters" | `dict` / `Counter` |
| **3. Complement lookup** | "two numbers that sum to…", "pair with difference k" | `dict`: value → index |
| **4. Group by key** | "group together items that are equivalent" | `dict`: key → list |

**`collections.Counter`** (an extra tool; Day 4 covers `collections` fully):
```python
from collections import Counter
c = Counter("banana")          # Counter({'a': 3, 'n': 2, 'b': 1})
c["z"]                         # 0 — missing keys return 0, no KeyError
c.most_common(2)               # [('a', 3), ('n', 2)]
Counter("abc") == Counter("cab")   # True — perfect for anagrams
```
**Interview tip:** first write the logic by hand with a dict, then mention "in production I'd use `Counter`". That shows you understand both the mechanism and the idiom.

### Pattern 3 worked example — Two Sum (the most-asked interview problem)
"Find two indices whose values add to `target`."
- **Brute force:** check every pair → O(n²).
- **Key insight:** for each `num`, the partner you need is `target - num` (its *complement*). Instead of searching for it, **remember every number you've seen** in a dict (value → index) and check in O(1).
```
nums = [2, 7, 11, 15], target = 9
i=0, num=2: need 7. seen={} → no.      seen={2:0}
i=1, num=7: need 2. seen has 2 at 0 → return [0, 1]
```
Write the code yourself in A2. Notice that you check *before* inserting. Why does that matter for `nums=[3, 3], target=6`, and for `nums=[3], target=6`?

### Pattern 4 worked example — Group Anagrams
Anagrams share the same **canonical key**. Two choices:
- `key = "".join(sorted(word))` → "eat", "tea", "ate" all become "aet". Cost O(k log k) per word.
- `key = tuple of 26 letter counts` → O(k) per word. Must be a **tuple**, not a list, because dict keys must be hashable.

### Bucket sort idea (for Top K Frequent)
Frequencies can only be 1…n. So make a list `buckets` of length n+1, where `buckets[f]` holds every number that appears `f` times. Walk the buckets from high to low and collect k numbers. That's **O(n), with no sorting**. A heap gives O(n log k); you'll learn heaps on Day 14.

## A2. LeetCode

**Process for every problem** (practice it aloud, as in an interview):
1. Restate the problem + ask one clarifying question (empty input? duplicates? negatives?)
2. Brute force + its complexity
3. Optimized idea → which hashing pattern?
4. Code
5. Trace one example by hand + edge cases
6. Final complexity

| # | Problem | Diff | Pattern / Hint |
|---|---|---|---|
| 217 | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | Easy | Seen-before. Also note the one-liner with `len(set(...))`; which exits earlier? |
| 242 | [Valid Anagram](https://leetcode.com/problems/valid-anagram/) | Easy | Frequency. Write a dict version + a `Counter` version. Early exit on length? |
| 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | Easy | ⭐ Complement. Brute + optimized. |
| 49 | [Group Anagrams](https://leetcode.com/problems/group-anagrams/) | Medium | Group by key. Try **both** keys; give the complexity of each in terms of n words, k max length. |
| 347 | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | Medium | ⭐ Count + sort (O(n log n)) first, then bucket sort (O(n)). |
| 238 | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | Medium | No division allowed. Answer[i] = (product of everything left of i) × (product of everything right of i). Build left products in one pass, right in another. |
| 128 ⭐ stretch | [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) | Medium | O(n) required. Put all numbers in a set. Only start counting from `x` if `x - 1` is **not** in the set. Why does that make it O(n) and not O(n²)? |

Stuck rule: 20 min on Easy / 35 min on Medium → re-read the hint → still stuck → read the solution, write in a comment *what idea you were missing*, and re-solve it Monday.

---

# Block B — Object-Oriented Programming

**Why OOP for backend work:** the Pydantic models, SQLAlchemy tables, FastAPI dependencies and service classes you'll build from Week 2 are all classes. LLD interviews (parking lot, LRU cache) are pure OOP.

## B1.1 Class, object, `__init__`, `self`
```python
class BankAccount:
    def __init__(self, owner: str, balance_cents: int = 0):
        self.owner = owner                  # instance attributes: each object gets its own
        self.balance_cents = balance_cents

    def deposit(self, amount_cents: int) -> None:
        if amount_cents <= 0:
            raise ValueError("Deposit must be positive")
        self.balance_cents += amount_cents

acct = BankAccount("Asha")      # creates an object, calls __init__
acct.deposit(500)               # Python turns this into BankAccount.deposit(acct, 500)
```
- A **class** is a blueprint; an **object/instance** is one thing built from it.
- `self` is just the object the method was called on. Python passes it automatically. That's the whole secret.
- `__init__` *initializes* an already-created object; it isn't technically the constructor (`__new__` is). Rarely matters, but it's a nice interview detail.

## B1.2 Class attributes vs instance attributes (classic bug)
```python
class User:
    count = 0                    # class attribute: ONE copy shared by all instances
    roles = []                   # ❌ shared mutable list, same trap as mutable defaults!

    def __init__(self, name):
        self.name = name         # instance attribute
        User.count += 1

a, b = User("a"), User("b")
a.roles.append("admin")
b.roles                          # ['admin']  ← b is an admin too!
```
Fix: create mutable attributes inside `__init__`: `self.roles = []`.

## B1.3 Three kinds of methods
```python
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):              # instance method: needs the object
        return self.celsius * 9 / 5 + 32

    @classmethod
    def from_fahrenheit(cls, f):          # gets the CLASS: alternative constructors
        return cls((f - 32) * 5 / 9)

    @staticmethod
    def is_valid(celsius):                # gets neither: a plain helper that lives in the class
        return celsius >= -273.15

t = Temperature.from_fahrenheit(212)      # Temperature(100.0)
```
**Real world:** `@classmethod` alternative constructors are everywhere: `datetime.fromtimestamp(...)`, `User.from_json(payload)`.

## B1.4 Encapsulation and `@property`
Python has no `private` keyword. By convention:
- `_balance`: "internal, don't touch from outside" (honor system)
- `__balance`: name-mangled to `_BankAccount__balance`, mostly to avoid clashes in subclasses

`@property` lets you **validate on assignment** while keeping simple attribute syntax:
```python
class Product:
    def __init__(self, name, price_cents):
        self.name = name
        self.price_cents = price_cents      # goes through the setter below!

    @property
    def price_cents(self):
        return self._price_cents

    @price_cents.setter
    def price_cents(self, value):
        if value < 0:
            raise ValueError("Price can't be negative")
        self._price_cents = value

    @property
    def price_display(self):                # computed, read-only
        return f"${self._price_cents / 100:.2f}"

p = Product("Mouse", 2599)
p.price_display          # '$25.99'
p.price_cents = -5       # ValueError — invalid state is impossible
```
**Why it matters:** an object that can never be invalid is the core idea behind Pydantic models in FastAPI.

## B1.5 Inheritance, `super()`, polymorphism
```python
class Notifier:
    def __init__(self, recipient):
        self.recipient = recipient

    def send(self, message):
        raise NotImplementedError("Subclasses must implement send()")

class EmailNotifier(Notifier):
    def __init__(self, recipient, subject_prefix="[App]"):
        super().__init__(recipient)          # run the parent's __init__ first
        self.subject_prefix = subject_prefix

    def send(self, message):                 # override
        return f"EMAIL to {self.recipient}: {self.subject_prefix} {message}"

class SMSNotifier(Notifier):
    def send(self, message):
        return f"SMS to {self.recipient}: {message[:160]}"

for n in [EmailNotifier("a@x.com"), SMSNotifier("+1716555")]:
    print(n.send("Your order shipped"))     # polymorphism: same call, different behavior
```
**Polymorphism** means calling code doesn't care which type it has, only that it has `.send()`. Adding a `SlackNotifier` later requires **zero** changes to the loop. This is the Open/Closed principle (SOLID, Day 24).

`isinstance(obj, Notifier)` checks type including parents. Python also uses **duck typing**: "if it has `.send()`, I can use it."

**Abstract base class** (forces subclasses to implement methods):
```python
from abc import ABC, abstractmethod
class Notifier(ABC):
    @abstractmethod
    def send(self, message): ...
Notifier("x")    # TypeError: can't instantiate abstract class
```

### Composition vs inheritance
- **Inheritance = "is-a":** an `EmailNotifier` *is a* `Notifier`.
- **Composition = "has-a":** an `OrderService` *has a* `Notifier` and *has a* `PaymentGateway`.
```python
class OrderService:
    def __init__(self, notifier: Notifier):
        self.notifier = notifier          # injected, so you can swap in a fake one in tests

    def place_order(self, order_id):
        # ... save order ...
        return self.notifier.send(f"Order {order_id} placed")
```
**Rule:** prefer composition. Deep inheritance trees get brittle. Passing dependencies in (`notifier=`) is called **dependency injection**, and it's exactly what FastAPI's `Depends()` does (Day 8).

## B1.6 Dunder (magic) methods
They let your objects work with Python's built-in syntax.
```python
class Money:
    def __init__(self, cents, currency="USD"):
        self.cents = cents
        self.currency = currency

    def __repr__(self):                 # for developers/logs: unambiguous
        return f"Money({self.cents}, {self.currency!r})"

    def __str__(self):                  # for end users: print(), f-strings
        return f"{self.cents / 100:.2f} {self.currency}"

    def __eq__(self, other):            # ==
        return (self.cents, self.currency) == (other.cents, other.currency)

    def __hash__(self):                 # needed to be a dict key/set item once __eq__ is defined
        return hash((self.cents, self.currency))

    def __add__(self, other):           # +
        if self.currency != other.currency:
            raise ValueError("Currency mismatch")
        return Money(self.cents + other.cents, self.currency)

    def __lt__(self, other):            # <, which also makes sorted() work
        return self.cents < other.cents
```
| Dunder | Triggered by |
|---|---|
| `__repr__` / `__str__` | `repr(x)`, debugger, logs / `print(x)` |
| `__eq__`, `__lt__` | `==`, `<`, `sorted()` |
| `__hash__` | dict keys, sets |
| `__len__`, `__contains__` | `len(x)`, `in` |
| `__getitem__`, `__setitem__` | `x[key]`, `x[key] = v` |
| `__iter__` | `for item in x` |
| `__add__` | `+` |

**Rule:** if you define `__eq__`, Python sets `__hash__` to `None` (unhashable) unless you also define it. Objects that are equal **must** have equal hashes.

## B1.7 Dataclasses — less boilerplate
```python
from dataclasses import dataclass, field

@dataclass
class Order:
    order_id: int
    customer: str
    items: list[str] = field(default_factory=list)   # ✅ new list per object (never `= []`)
    status: str = "pending"

o = Order(1, "Asha")
o                     # Order(order_id=1, customer='Asha', items=[], status='pending')  — free __repr__
o == Order(1, "Asha") # True — free __eq__

@dataclass(frozen=True)          # immutable → hashable → usable as dict key
class Point:
    x: int
    y: int
```
Use a dataclass for "mostly data" objects (DTOs, config, events). Use a regular class when there's real behavior and invariants. Pydantic models (Day 8) look almost identical, but they also validate types at runtime.

---

## B2. Practice Exercises (`week01/Day_03/oop_exercises.py`)

Add `assert` tests under each one, as you did yesterday.

1. **`BankAccount`:** balance stored as integer cents behind a read-only `balance` property; `deposit(cents)` and `withdraw(cents)` raise `ValueError` for non-positive amounts or insufficient funds; keep a `history` list of `("deposit", 500)` tuples (watch the class-attribute trap!); `__repr__`. Add a `@classmethod from_dollars(owner, dollars: str)` that converts `"12.34"` to 1234 cents **without float** (hint: `decimal.Decimal`, or split on `"."`).
2. **`Money` as a frozen dataclass** with `cents` and `currency`; implement `__add__` with a currency check. Show that two equal `Money` objects deduplicate in a set.
3. **Notifiers:** abstract `Notifier` with `send`; `EmailNotifier`, `SMSNotifier` (truncate to 160 chars), and your own `SlackNotifier`. Write `notify_all(notifiers, message)` that returns a list of results. Then an `OrderService` that receives a notifier via `__init__` (composition).
4. **Build your own `HashMap`** (this ties Block A and B together; it's a real interview question at Amazon/Microsoft):
   - Chaining: `self.buckets = [[] for _ in range(8)]` (why not `[[]] * 8`?)
   - `put(key, value)` (update if the key exists), `get(key)` (raise `KeyError` if missing), `remove(key)`
   - `__len__`, `__contains__`, `__getitem__`/`__setitem__` so `m["a"] = 1` and `m["a"]` work
   - Resize to double the buckets when `len / buckets > 0.75`, re-inserting every pair
   - Bucket index: `hash(key) % len(self.buckets)`
   - In a comment: time complexity of `get` on average and worst case, and why resizing is amortized O(1)
5. **Bug hunt:** what does this print, why, and how do you fix it?
   ```python
   class Cart:
       items = []
       def add(self, item):
           self.items.append(item)

   c1, c2 = Cart(), Cart()
   c1.add("book")
   print(c2.items)
   ```

---

## Daily Check

1. Walk through what happens inside a dict when you do `d["cat"] = 7`, then `d["cat"]`. What's a collision, and how is it handled?
2. Why is dict insert O(1) *amortized*, and what's the worst case?
3. In Two Sum, why check for the complement **before** inserting the current number?
4. Group Anagrams: complexity with the sorted-string key vs the count-tuple key? Why must the count key be a tuple?
5. Why is Top K Frequent's bucket sort O(n)? What makes it possible here when general sorting can't beat O(n log n)?
6. Difference between a class attribute and an instance attribute? Show the bug that mixing them up causes.
7. When would you use `@classmethod` vs `@staticmethod`? Give a real example of each.
8. What's the difference between `__repr__` and `__str__`? What happens to `__hash__` when you define `__eq__`?
9. Composition vs inheritance: which does `OrderService(notifier)` use, and why is it easier to test?
10. Catch-up drills C1–C4: your complexities.

---

## 📤 How to Submit
Push to GitHub, then send:
```
DAY 3 SUBMISSION
Repo link + commit(s): __
Catch-up: done? C1–C4 answers + closures.py location
LeetCode: list solved; flag any where you read the solution
Daily check: in Day03_Submission.md
Where I got stuck: __
```
Next: Day 4 covers Strings + prefix sums and advanced Python (exceptions, generators, decorators, context managers), then **Skill Questionnaire 1: Python**.
