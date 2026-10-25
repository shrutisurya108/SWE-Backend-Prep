# Day 1 Review — Setup + Python Basics

**Score: 8.5 / 10** · Strong start. All the logic is correct and your daily check answers are interview-quality. Points were lost on: one infinite-loop bug, shadowing a built-in name, a missing complexity analysis, and some style habits that interviewers will notice.

**Verdict: ✅ Move on to Day 2.**

---

## 🔴 Must-Fix (bugs and habits interviewers penalize)

### 1. ex4 — Infinite loop on negative input
```python
n = -5
while n != 0:
    n = n // 10   # -5//10 = -1, then -1//10 = -1 ... forever
```
Floor division toward −∞ (yesterday's lesson!) means a negative `n` never reaches 0. The prompt said "non-negative", but **real code must validate its input**. Interviewers often test with negatives, 0 and huge numbers.

### 2. ex4 — Shadowing the built-in `sum`
`sum = 0` replaces Python's `sum()` function for the rest of the file. Any later `sum([1, 2])` crashes with `TypeError: 'int' object is not callable`. The same goes for `list`, `dict`, `str`, `id`, `input`, `max`, `min` and `type`. Use names like `total` or `digit_sum`.

**Fixed ex4:**
```python
def digit_sum(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    total = 0
    while n > 0:          # `> 0` is also a safer loop guard than `!= 0`
        total += n % 10
        n //= 10
    return total

print(digit_sum(int(input("Enter a non-negative integer: "))))
```
*Edge case:* `digit_sum(0)` returns 0. Correct, because the loop is simply skipped.

### 3. LeetCode — No complexity written
The submission template asked for complexity on both problems, and it's missing from both. In interviews, **a correct solution without stating its complexity is an incomplete answer.** Make it a habit starting today:
- **412 Fizz Buzz:** Time O(n), extra space O(1). The output list is O(n), but it's required output and usually not counted.
- **1480 Running Sum:** Time O(n), space O(n) for the new list. The in-place version is O(1) extra space (see below).

---

## 🟡 Improvements (style and robustness)

**ex1 — `int()` rejects `"36.6"`.** Temperatures are decimals, so use `float(temp)`.

**ex2 — ✅ Correct.** Two small notes:
- `split()` with no argument splits on *any* whitespace and ignores repeated spaces. `split(' ')` breaks if the log has two spaces somewhere. Prefer `split()`.
- Index-based parsing is fragile: if the log format changes, every index shifts. Real systems use structured (JSON) logs or regex. You'll learn `re` on Day 4.

**ex3 — `server = None` is never used.** Delete dead code. The prompt also asked you to route a single given `user_id` first.
> 💡 **Real-world preview:** `user_id % num_servers` has a big flaw. If you go from 4 to 5 servers, almost every user moves to a different server, which means a huge data migration. The fix is **consistent hashing**, a top-5 system design topic (Day 21–22).

**ex5 — ✅ Correct.** Two refinements:
```python
result = st.lower() == st[::-1].lower()   # a comparison already IS a bool; no if/else needed
```
Rule: `if cond: x = True else: x = False` should always be written as `x = cond`. Your loop also works; a more readable version is `for ch in reversed(st):`.

**ex6 — ✅ Logic is correct.** Three things to level up:
1. **Naming:** Python uses `snake_case` (PEP 8): `has_digit`, not `hasDigit`. Using camelCase in a Python interview is a small "not fluent in Python" signal.
2. **`any()` replaces each helper function with one line:** `any(ch.isdigit() for ch in pwd)`.
3. **Avoid `exit()` inside logic.** It's meant for the interactive shell, and it kills the whole program, so you can't test or reuse the code. Return the result instead:

```python
def validate_password(pwd: str) -> str:
    if len(pwd) < 8:
        return "Password must be at least 8 characters long"
    if not any(ch.isdigit() for ch in pwd):
        return "Password must contain at least 1 digit"
    if not any(ch.isupper() for ch in pwd):
        return "Password must contain at least 1 uppercase letter"
    if not any(ch.islower() for ch in pwd):
        return "Password must contain at least 1 lowercase letter"
    return "valid"

print(validate_password(input("Enter the password: ")))
```
Now it's testable: `assert validate_password("abc") != "valid"`. You'll write real tests with pytest on Day 5. (Also, "atleast" should be "at least". User-facing text matters in real products.)

**LC 412 — ✅ Accepted.** `range(0, n)` with `j = i + 1` is roundabout. Iterate what you need directly:
```python
for i in range(1, n + 1):
    if i % 15 == 0: answer.append("FizzBuzz")
    elif i % 3 == 0: answer.append("Fizz")
    elif i % 5 == 0: answer.append("Buzz")
    else: answer.append(str(i))
```
**Hint answer:** the 15 case must come first because any number divisible by 15 is also divisible by 3, so the `% 3` branch would catch it first and you'd output "Fizz".

**LC 1480 — ✅ Accepted.** Name your loop variable `num`, not `i`. `i` signals an index, and misleading names cause bugs. Here is the **O(1) extra space** follow-up (an interviewer may ask "can you avoid the extra list?"):
```python
def runningSum(self, nums: list[int]) -> list[int]:
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]
    return nums
```
⚠️ Trade-off to *say out loud*: this **mutates the caller's input**. That's fine if the interviewer allows it, but in production code mutating inputs causes surprising bugs. Always ask: *"Is it okay to modify the input?"*

---

## 📊 About "Beats 100%"

Nice, but **don't chase LeetCode runtime percentiles.** For small inputs, runtime is mostly server noise: resubmit the same code and you might "beat 40%". Interviewers grade Big-O, correctness, edge cases and communication, not milliseconds. Your memory numbers (19 MB) are mostly the Python interpreter itself.

---

## ✅ Daily Check

| Q | Verdict | Notes |
|---|---|---|
| 1 | ✅ Perfect | Correct values and correct Java behavior (-3 and -1). |
| 2 | ✅ Perfect | |
| 3 | ✅ Good | Add the Big-O: repeated `+=` can be **O(n²)** total, `join` is **O(n)**. (CPython sometimes optimizes `+=` in place, but you can't rely on it, so interviewers expect `join`.) |
| 4 | 🟡 Right answer, fuzzy reason | Precise version: `bool()` on a string only checks **whether it's empty**; it never reads the content. Any non-empty string, including `"False"` and `"0"`, is `True`. |
| 5 | ✅ Perfect | Small terminology note: it's a **list**, not an array. In Python, "array" means the `array` module or NumPy. |
| 6 | ✅ Excellent | Interview-ready. Add one concrete example: `0.1` has no exact binary representation, just like 1/3 has no exact decimal one. |

---

## 🧠 Takeaways for Tomorrow
1. Always write complexity next to every solution.
2. Never use built-in names as variables.
3. Think about edge cases: empty, zero, negative, huge, and whitespace input.
4. Write functions that **return** values instead of printing or exiting, so they can be tested.
