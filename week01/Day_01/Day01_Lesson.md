# Day 1 — Setup + Python Basics (Mon Oct 19 · 2 hours)

| Time | Block |
|---|---|
| 0:00–0:20 | Setup |
| 0:20–1:05 | Lesson (read + run every snippet yourself) |
| 1:05–1:40 | Practice exercises |
| 1:40–1:55 | LeetCode (2 problems) |
| 1:55–2:00 | Daily check + submit |

---

## 1. Setup (20 min)

1. **Python:** install the latest stable 3.x from python.org (Windows: tick **"Add Python to PATH"**). Verify:
   ```bash
   python --version      # or python3 --version on Mac/Linux
   ```
2. **VS Code** + the **Python** extension (by Microsoft).
3. **Git:** install from git-scm.com, then verify with `git --version`. (We use it properly on Day 5.)
4. **LeetCode:** create a free account.
5. Make a folder `swe-prep/day01/`, create `hello.py`:
   ```python
   print("Hello, future engineer!")
   ```
   Run it from the terminal: `python hello.py`

---

## 2. Lesson (45 min)

### 2.1 How Python runs
Python is **interpreted** and **dynamically typed**: you don't declare types, and code runs line by line (compiled to bytecode first, then executed by the CPython VM).
*Interview question:* "Is Python compiled or interpreted?" → Both: source → bytecode (`.pyc`) → interpreted by the VM.

### 2.2 Variables and core types
```python
name = "Asha"          # str
age = 24               # int  (arbitrary size, no overflow!)
gpa = 3.8              # float
is_hired = False       # bool
manager = None         # NoneType — "no value"

print(type(age))       # <class 'int'>
```
A variable is a **name pointing to an object**, not a box holding a value:
```python
a = [1, 2]
b = a          # b points to the SAME list
b.append(3)
print(a)       # [1, 2, 3]  ← surprises beginners; classic interview trap
```

### 2.3 Operators (know these cold)
```python
7 / 2     # 3.5   true division, always float
7 // 2    # 3     floor division
7 % 2     # 1     remainder (modulo)
2 ** 10   # 1024  power
-7 // 2   # -4    floors toward −infinity, NOT toward 0 (C/Java give -3!)
-7 % 2    # 1     result takes sign of the divisor in Python

0.1 + 0.2 == 0.3          # False! floating-point precision
abs((0.1 + 0.2) - 0.3) < 1e-9   # correct way to compare floats

x = [1]; y = [1]
x == y    # True  → same VALUE
x is y    # False → different OBJECTS. Use `is` only for None: `if x is None`
```
**Real world:** `%` is everywhere in backends. Sharding: `server = user_id % num_servers` decides which database server stores a user. Money is never stored as float; use integer cents or `decimal.Decimal` (asked at PayPal / JP Morgan style interviews).

### 2.4 Strings
```python
s = "backend"
s[0]       # 'b'
s[-1]      # 'd'          negative index counts from the end
s[1:4]     # 'ack'        slice [start:stop) — stop is excluded
s[::-1]    # 'dnekcab'    reverse
len(s)     # 7

s.upper(), s.replace("end", "!"), "a,b,c".split(",")   # 'BACKEND', 'back!', ['a','b','c']
"-".join(["2026", "10", "19"])                          # '2026-10-19'
"  hi  ".strip()                                        # 'hi'

user, n = "Asha", 3
print(f"{user} has {n} open tickets")   # f-strings: use these for formatting/logging
```
**Strings are immutable:** `s[0] = "B"` raises `TypeError`. Building a string with `+=` in a loop creates a new string each time (O(n²) worst case); collect parts in a list and `"".join(parts)` (O(n)). Interviewers notice this.

### 2.5 Input and type conversion
```python
raw = input("Enter age: ")   # ALWAYS returns str
age = int(raw)               # ValueError if raw is "abc"
float("3.5"), str(42), bool(""), bool("0")   # 3.5, '42', False, True (!)
```
**Truthiness:** falsy values are `0, 0.0, "", [], {}, set(), None, False`. Everything else is truthy. So `if items:` means "if list is not empty".

### 2.6 Conditionals
```python
status = 404
if status < 300:
    print("success")
elif status < 500:
    print("client error")
else:
    print("server error")

# Chained comparison & ternary
if 200 <= status < 300: ...
label = "ok" if status == 200 else "fail"
```
Indentation **is** the syntax (4 spaces). `and` / `or` short-circuit: `user and user.name` won't crash if `user` is `None`.

### 2.7 Loops
```python
for i in range(5):          # 0..4
    print(i)
for i in range(2, 10, 3):   # 2, 5, 8
    print(i)
for ch in "api":            # iterate any sequence
    print(ch)
for idx, ch in enumerate("api"):   # index + value — use this, not range(len(...))
    print(idx, ch)

retries = 0
while retries < 3:          # real pattern: retrying a failing network call
    print("attempt", retries + 1)
    retries += 1

for n in range(10):
    if n == 2: continue     # skip this iteration
    if n == 5: break        # exit the loop
```

---

## 3. Practice Exercises (35 min)

Write each in `day01/ex1.py` … `ex6.py`. No `import`s needed.

1. **Temperature converter:** read Celsius from input, print Fahrenheit rounded to 1 decimal (`F = C * 9/5 + 32`).
2. **Log parser (real backend task):** given
   `line = "2026-10-19 15:37:02 ERROR [payment-service] Card declined for user_id=4821"`
   extract and print `date`, `level`, `service` (without brackets) and `user_id` as an **int**. Use `split` and slicing only.
3. **Shard router:** given `user_id` and `num_servers = 4`, print which server (0–3) stores that user. Then print the server for user IDs 1 to 10 in a loop.
4. **Sum of digits (classic):** given a non-negative integer like `98765`, return the digit sum **using `%` and `//` in a `while` loop**, without converting to a string.
5. **Reverse a string two ways:** (a) slicing, (b) a loop that builds a list and uses `"".join`. Then check if a word is a **palindrome**, ignoring case (`"Racecar"` → True).
6. **Password validator (real signup feature):** a password is valid if length ≥ 8, it has at least one digit, one uppercase letter and one lowercase letter. Print `"valid"` or the **first** rule that fails. Hint: `ch.isdigit()`, `ch.isupper()`, `ch.islower()`.

---

## 4. LeetCode (15 min)

| # | Problem | Difficulty | Hint |
|---|---|---|---|
| 412 | [Fizz Buzz](https://leetcode.com/problems/fizz-buzz/) | Easy | Check the 15 case **first**. Why does order matter? |
| 1480 | [Running Sum of 1d Array](https://leetcode.com/problems/running-sum-of-1d-array/) | Easy | Keep a running total. Can you do it in O(1) extra space by modifying the input? |

For each: write the time and space complexity as a comment (even a guess; we formalize Big-O tomorrow).

---

## 5. Daily Check (5 min, answer briefly)

1. What do `-7 // 2` and `-7 % 2` return in Python, and why might that differ from Java?
2. Difference between `==` and `is`? When should you use `is`?
3. Why is `"".join(parts)` preferred over `+=` in a loop when building a string?
4. What does `bool("False")` return? Why?
5. After `a = [1]; b = a; b.append(2)`, what is `a`? Explain.
6. Why shouldn't you store money as `float` in a payments system?

---

## 📤 How to Submit

Paste this into the chat:
```
DAY 1 SUBMISSION
Time spent: __
Exercises: (paste code for ex1–ex6)
LeetCode 412: (code + complexity)
LeetCode 1480: (code + complexity)
Daily check answers: 1)… 6)…
Where I got stuck / what confused me: __
```
You'll get `Day01_Review.md` with fixes, explanations and model solutions, then `Day02_Lesson.md` (full day, ~7 hrs).

## Daily check answers:
Daily check answers: 
1) In python, -7//2 return the floor division inclined towards negative infinity, which is -4, -7%2 return the remainder with sign of the divisor, which is 1.
In Java, -7//2 would return -3 as it truncates the output towards 0, and -7%2 would return -1
2) The "==" checks for the equality of values between the given operands, whereas 'is' keyword checks if the 2 operands point to the same object. 'is' should be used in case of singleton values like 'None'.
3) For string concatenation, using "+=" repeatedly is not efficient because each time in the loop a new string is created and previous value is allocated and then the new string is created, but using "".join() concatenates them more efficiently.
4) It will return True, because a non-empty string is a True value if no more evaluation is to be done on it. A boolean check on string value only if it empty or not, it does not care about its value such as "false" or "0".
5) a will be [1,2] because b and a both point to the same array object, so a change in b will also reflect in a.
6) Money values can be in decimal, which when converted internally in computers are stored in binary formats, during which some precision errors can be introduced in the values if stored in float format. In payments system, a single digit error in precision can also cause a lot of trouble. Therefore, we should store it either as an integer format (in cents, a minor unit) or the Decimal module to store its exact decimal representation, this way, no precision errors can be introduced in the values.

## Where I got stuck / what confused me: 
I understood mostly all the concepts. I looked up deeper explanations for the core concepts.