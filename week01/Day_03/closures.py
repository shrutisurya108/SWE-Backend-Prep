# Closures
# make_greeting(greeting) returns a function that takes name and returns f"{greeting}, {name}!".
# make_accumulator() returns a function; each call acc(x) adds x to a running total and returns it (acc(5) → 5, acc(3) → 8). Needs nonlocal.
# Sort ["banana", "Apple", "cherry"] case-insensitively with a lambda. Then sort by length, longest first.
# Explain in a comment why [lambda: i for i in range(3)] returns [2, 2, 2] when called, and fix it.

def make_greeting(greeting):
    def f(name):
        return f"{greeting}, {name}!"
    return f

try_f = make_greeting("Hello")
assert (try_f("S")) == "Hello, S!"

def make_accumulator():
    total = 0
    def acc(x):
        nonlocal total
        total += x
        return total
    return acc

try_acc = make_accumulator()
assert (try_acc(5)) == 5
assert (try_acc(3)) == 8

sorted_fruits = sorted(["banana", "apple", "Cherry", "Blueberry"], key= lambda fruit: (fruit.lower(), -len(fruit)))
assert (sorted_fruits) == ["apple", "Blueberry", "banana", "Cherry"]

# [lambda: i for i in range(3)] returns [2, 2, 2] when called because the lambda remembers only the variable and not its value.
# This is called late binding, and the variable's value is looked up only at last when called, and in each call, omly its latest value 2 is visible.
# fix:
# [lambda i=i: i for i in range(3)]
# This way, it creates a default argument where each time i gets values 0,1,2 (early binding), or, the values are frozen at evaluation time.
# so when called, it prints the expected values.