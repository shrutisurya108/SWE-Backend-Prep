# 1
# BankAccount: balance stored as integer cents behind a read-only balance property;
# deposit(cents) and withdraw(cents) raise ValueError for non-positive amounts or insufficient funds;
# keep a history list of ("deposit", 500) tuples (watch the class-attribute trap!); __repr__.
# Add a @classmethod from_dollars(owner, dollars: str) that converts "12.34" to 1234 cents without float (hint: decimal.Decimal, or split on ".").
class BankAccount:
    def __init__(self, owner, balance=0, history=None):
        self.owner = owner
        self._balance = balance
        if history is None:
            self.history = []

    @property
    def balance(self):
        return self._balance

    def deposit(self, cents):
        if cents < 0:
            raise ValueError("Non-positive amount for deposit!")
        self._balance += cents
        self.history.append(("deposit", cents))

    def withdraw(self, cents):
        if cents > self._balance:
            raise ValueError("Insufficient funds!")
        self._balance -= cents
        self.history.append(("withdraw", cents))

    def __repr__(self):
        return f"{type(self).__name__}(owner: {self.owner}, balance: {self.balance}, history: {self.history})"

    @classmethod
    def from_dollars(cls, owner, dollars: str):
        if '.' not in dollars:
            cents = int(dollars)*100
        else:
            cents = (int("".join(dollars.split('.'))))
        return cls(owner, cents)

a = BankAccount(1, 100)
assert(repr(a)) == "BankAccount(owner: 1, balance: 100, history: [])"
a.deposit(200)
assert(repr(a)) == "BankAccount(owner: 1, balance: 300, history: [('deposit', 200)])"
a.withdraw(150)
assert(repr(a)) == "BankAccount(owner: 1, balance: 150, history: [('deposit', 200), ('withdraw', 150)])"
# a.withdraw(200) # Checked their Value error, showing correctly
# a.deposit(-2)
b = BankAccount.from_dollars(2, "20.00")
assert(repr(b)) == "BankAccount(owner: 2, balance: 2000, history: [])"

# 2
# Money as a frozen dataclass with cents and currency;
# implement __add__ with a currency check. Show that two equal Money objects deduplicate in a set.
from dataclasses import dataclass
@dataclass(frozen=True)
class Money:
    cents: int
    currency: str

    def __add__(self, new_money):
        if new_money.currency != self.currency:
            raise ValueError("Currency does not match!")
        else:
            return(Money(self.cents+new_money.cents, self.currency))

m1 = Money(100, '$')
m2 = Money(200, '$')
m3 = m1+m2
assert m3 == Money(300, '$')
assert(m3.cents) == 300
m4 = Money(100, 'Euro')
# m5 = m1+m4              # Confirmed that it prints Currency does not match!

money_set = set()
assert (len(money_set)) == 0
money1 = Money(40, '$')
money_set.add(money1)
assert (len(money_set)) == 1
money2 = Money(40, '$')
money_set.add(money2)
assert len(money_set) == 1
# this shows that 2 objects with exactly same attributes are treated as same/equal, and deduplicated when both added to a set


# 3
# Notifiers: abstract Notifier with send; EmailNotifier, SMSNotifier (truncate to 160 chars), and your own SlackNotifier.
# Write notify_all(notifiers, message) that returns a list of results.
# Then an OrderService that receives a notifier via __init__ (composition).
from abc import ABC, abstractmethod
class Notifier(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailNotifier(Notifier):
    def send(self, message):
        return (f"Email sent: {message}")

class SMSNotifier(Notifier):
    def send(self, message):
        return (f"SMS sent: {message[:160]}")

class SlackNotifier(Notifier):
    def send(self, message):
        return (f"Slack msg sent: {message}")

def notify_all(notifiers, message):
    result = []
    for channel in notifiers:
        result.append(channel.send(message))
    return result
[]
assert(notify_all([EmailNotifier(), SMSNotifier()], "Limit reached!")) == ["Email sent: Limit reached!", "SMS sent: Limit reached!"]

class OrderService:
    def __init__(self, notifier):
        self.notifier = notifier

service1 = OrderService(EmailNotifier())
service2 = OrderService(SMSNotifier())
service3 = OrderService(SlackNotifier())

# Please review the exercise 3 implementation. I have not completely understood how to implement this.


# 4
# Build your own HashMap (this ties Block A and B together; it's a real interview question at Amazon/Microsoft):
# Chaining: self.buckets = [[] for _ in range(8)] (why not [[]] * 8?)
# put(key, value) (update if the key exists), get(key) (raise KeyError if missing), remove(key)
# __len__, __contains__, __getitem__/__setitem__ so m["a"] = 1 and m["a"] work
# Resize to double the buckets when len / buckets > 0.75, re-inserting every pair
# Bucket index: hash(key) % len(self.buckets)
# In a comment: time complexity of get on average and worst case, and why resizing is amortized O(1)



# 5
# class Cart:
#     items = []
#     def add(self, item):
#         self.items.append(item)

# c1, c2 = Cart(), Cart()
# c1.add("book")
# print(c2.items)
# This will print "book" for both c1 and c2, because a mutable items (list) was used a class variable,
# so different objects c1 and c2 both have access to the same items list, and both can see the changes made to it.
# To correct this, we should create an empty list while instantiating the objects
class Cart:
    def __init__(self, items=None):
        if items is None:
            self.items = []

    def add(self, item):
        self.items.append(item)

c1, c2 = Cart(), Cart()
c1.add("book")
assert (c2.items) == []

# Daily Check Questions
# 1. Walk through what happens inside a dict when you do d["cat"] = 7, then d["cat"]. What's a collision, and how is it handled?
# Answer: When we do d["cat"] = 7, python calculates a hash of the key cat to find a suitable bucket/address
#                              where to store the associated value 7 and stores the value 7 there.
# When we do d["cat"], Python calculates the hash value of key "cat", gets the address to look up
#                               and returns the value present at that address.
# A collision happens when more two or more keys have the same output from hash function, or the hash value,
#                               so the values all get same address/bucket
# In case of collision, it can be handled using open-chaining, in which case, all the items with same hash value are stored
# in a list at the same address and would be traversed serially (it would be a smaller list compared to the original number of items,
#                                 so lookup would be faster but not O(1))
# Another method is closed chaining, in which Python uses internal algorithms to find the next available spot for the item with same hash value.


# 2. Why is dict insert O(1) amortized, and what's the worst case?
# For dict storage, space is allocated at the time of dict creation.
# Insert in a dict is O(1) for general cases because it only needs to calculate a hash value from the key to calculate the target
# address for storage. When after multiple inserts the originally allocated space is exhausted, the storage space is doubled and
# all the items currently in dict have to be copied from older storage to the new storage space.
# This does not happen for all inserts, but only a few. In worst case, an insert could trigger space increasing and copying of dict items,
# Making a dict insert O(n) operation in worst case
# Therefore, in general, a dict insert operation is considered O(1) amortized.


# 3. In Two Sum, why check for the complement before inserting the current number?
# 4. Group Anagrams: complexity with the sorted-string key vs the count-tuple key? Why must the count key be a tuple?
# 5. Why is Top K Frequent's bucket sort O(n)? What makes it possible here when general sorting can't beat O(n log n)?


# 6.  Difference between a class attribute and an instance attribute? Show the bug that mixing them up causes.
# Class attributes are the variables that are on the class level, so all objects created from that class have the same reference
# and can access that variable. This means if 1 object changes that variable, that change will be visible for all objects of that class.
# Instance attributes are at object level, any changes to tha variable are restricted within that object only and no other object
# of the class can access it.
# for example:
class Shopping:
    shopping_cart = []
    def add_item_to_cart(self, item):
        Shopping.shopping_cart.append(item)
shopper1 = Shopping()
shopper1.add_item_to_cart("Boots")
shopper2 = Shopping()
shopper2.add_item_to_cart("Jackets")
# In this code we expect that shopper1's cart should have only Boots and shopper2's cart should have only Jackets since they are separate
# shoppers created from same Shopping class. But actually, since shopping_cart is a class attribute of Shopping class, any object created
# from this class will share access to shopping_cart, so shopper1 and shopper2 both will see ["Boots", "Jackets"] in their shopping_cart
# causing a bug.


# 7. When would you use @classmethod vs @staticmethod? Give a real example of each.
# We should use @classmethod when the functions need to do something as the time of consructor initialization.
# We should use static method when the function does not depend on any class or instance variable at all,
# but should remain as a part of the class only for the logic.

# I have not understood these concepts well enough to clearly give examples.


# 8. What's the difference between __repr__ and __str__? What happens to __hash__ when you define __eq__?
# __repr__ gives a more developer friendly representation of any object, while __str__ gives a more user friendly view
# when we define __eq__ , Python disables the __hash__ to avoid collision, and we have to define __hash__ too.

# 9. Composition vs inheritance: which does OrderService(notifier) use, and why is it easier to test?
# Not clear enough to answer this question.

# 10. Catch-up drills C1–C4: your complexities.
# Present in same directory/Day03_Submission.md
